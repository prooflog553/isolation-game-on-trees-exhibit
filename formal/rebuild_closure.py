"""Fresh Windows source-only closure builder; no historical object or results reuse.
Uses recorded archive manifest and options after source hashes are checked.
"""
import argparse, concurrent.futures, datetime, hashlib, json, os, pathlib, subprocess, sys, time, uuid

root = pathlib.Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description='Verify or build a frozen Lean source closure')
parser.add_argument('target', choices=('D9', 'D10'))
parser.add_argument('lean', type=pathlib.Path, nargs='?', help='Path to the Lean 4.19.0 executable')
parser.add_argument('--verify-only', action='store_true', help='Check source hashes without running Lean')
args = parser.parse_args()
target = args.target
source = root / 'source_d9_d10' / target / 'src'
manifest = json.loads((source.parent / 'DOTS_SOURCE_BUILD_MANIFEST.json').read_text(encoding='utf-8-sig'))
entries = {e['module']: e for e in manifest['source_entries']}
assert len(entries) == (1566 if target == 'D9' else 1006)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
paths = {n: source.joinpath(*n.split('.')).with_suffix('.lean') for n in entries}
for n, p in paths.items():
    if not p.is_file() or sha(p) != entries[n]['sha256']:
        raise RuntimeError(f'source mismatch: {n}')
if list(source.rglob('*.olean')):
    raise RuntimeError('source tree contains olean')
if args.verify_only:
    print(f'{target}: verified all {len(entries)} source hashes')
    sys.exit(0)
if args.lean is None:
    parser.error('the Lean executable is required for a build')
lean = args.lean.resolve(strict=True)
deps = {n: {x for x in manifest['imports'][n] if x in entries} for n in entries}
run = root / ('run-' + target + '-' + uuid.uuid4().hex)
run.mkdir(); lib = run / 'lib'; lib.mkdir(); logs = run / 'logs'; logs.mkdir()
env = os.environ.copy(); env['LEAN_PATH'] = str(lib); env['LEAN_SRC_PATH'] = str(source); env['LEAN_NUM_THREADS'] = '1'
env.pop('LD_PRELOAD', None)
done = {}; pending = set(entries); active = {}; start = datetime.datetime.now(datetime.timezone.utc).isoformat()

def build(n):
    dest = lib.joinpath(*n.split('.')).with_suffix('.olean'); dest.parent.mkdir(parents=True, exist_ok=True)
    options = ['-DautoImplicit=false', '-DmaxSynthPendingDepth=3', '-Dpp.unicode.fun=true'] if n.startswith('Mathlib.') else []
    cmd = [str(lean), '-j1', '-R', str(source), *options, '-o', str(dest), str(paths[n])]
    rec = {'module':n, 'kind':entries[n]['kind'], 'source_sha256':sha(paths[n]), 'argv':cmd, 'cwd':str(source), 'start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    t = time.monotonic()
    with (logs/(n+'.stdout.txt')).open('wb') as out, (logs/(n+'.stderr.txt')).open('wb') as err:
        try: rec['exit_code'] = subprocess.run(cmd, cwd=source, env=env, stdout=out, stderr=err).returncode
        except OSError as ex: rec['exit_code'] = None; rec['error'] = str(ex)
    rec.update(end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), seconds=round(time.monotonic()-t,3), object_sha256=sha(dest) if dest.is_file() else None)
    rec['pass'] = rec['exit_code'] == 0 and dest.is_file() and sha(paths[n]) == entries[n]['sha256']
    (logs/(n+'.status.json')).write_text(json.dumps(rec, indent=2),encoding='utf-8')
    return rec

def save(terminal=False):
    (run/'progress.json').write_text(json.dumps({'target':target,'start_utc':start,'updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'total':len(entries),'passed':sum(v['pass'] for v in done.values()),'failed':sum(not v['pass'] for v in done.values()),'pending':len(pending),'active':list(active.values()),'terminal':terminal,'lean':str(lean),'lean_sha256':sha(lean),'LEAN_PATH':str(lib),'LEAN_SRC_PATH':str(source)},indent=2),encoding='utf-8')

halt = False
workers = int(os.environ.get('LEAN_BUILD_WORKERS', '2'))
if workers < 1:
    parser.error('LEAN_BUILD_WORKERS must be positive')
with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
    while pending or active:
        if not halt:
            ready=sorted(n for n in pending if deps[n].issubset(done) and all(done[d]['pass'] for d in deps[n]))
            for n in ready[:workers-len(active)]:
                pending.remove(n); active[pool.submit(build,n)] = n
        save()
        if not active: break
        finished,_=concurrent.futures.wait(active,timeout=20,return_when=concurrent.futures.FIRST_COMPLETED)
        for future in finished:
            n=active.pop(future); done[n]=future.result(); print(json.dumps({'module':n,'pass':done[n]['pass'],'completed':len(done),'total':len(entries)}),flush=True)
            if not done[n]['pass']: halt=True
save(True)
sys.exit(0 if len(done)==len(entries) and all(x['pass'] for x in done.values()) else 1)
