import FourteenCounterexampleReduction
import T03OuterRootFamilyBounds
import WhiteT00OuterRootBounds
import WhiteT07OuterRootBounds
import WhiteT10OuterRootBounds
import WhiteT15OuterRootBounds
import R11ID8577Ceiling
import R10White88OuterRootBounds
import R12White315OuterRootBounds
import R13White1015OuterRootBounds

/-!
SOURCE_ONLY / NOT ELABORATED / NOT NATIVE / NOT ACCEPTED.
This candidate has no Lean result. Pending source providers are not accepted
objects. The corresponding dependency gate must open before any future build.
No slot was requested, acquired, or used in preparing this source.
-/
namespace IsolationGame.FourteenDiameterNineClosure
set_option maxRecDepth 8192
set_option maxHeartbeats 2000000

open FourteenResidual FourteenCounterexample

/-- SOURCE CANDIDATE ONLY. Exact fourteen-constructor assembly using the
literal all-Nat endpoints. Each branch changes to the full raw-list graph and
carrier, so neither a numerical order match nor finite p/q testing is used.
This declaration is not accepted while any family or build/audit gate is shut. -/
theorem fourteen_ceiling_obligations : FourteenCeilingObligations := by
  intro k p q
  cases k with
  | r00 =>
    change isolationNumber (TwoCoreOpening.graph [0] [8] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [0] [8] p q)+6)/7
    exact ReceiverOuterRootApplications.r00_ordinary_ceil p q
  | r01 =>
    change isolationNumber (TwoCoreOpening.graph [3] [8] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [3] [8] p q)+6)/7
    exact T03OuterRootApplications.r01_ordinary_ceil p q
  | r02 =>
    change isolationNumber (TwoCoreOpening.graph [3] [12] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [3] [12] p q)+6)/7
    exact T03OuterRootApplications.r02_ordinary_ceil p q
  | r03 =>
    change isolationNumber (TwoCoreOpening.graph [7] [8] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [7] [8] p q)+6)/7
    exact ReceiverOuterRootApplications.r03_ordinary_ceil p q
  | r04 =>
    change isolationNumber (TwoCoreOpening.graph [8] [10] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [8] [10] p q)+6)/7
    exact ReceiverOuterRootApplications.r04_ordinary_ceil p q
  | r05 =>
    change isolationNumber (TwoCoreOpening.graph [8] [15] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [8] [15] p q)+6)/7
    exact ReceiverOuterRootApplications.r05_ordinary_ceil p q
  | r06 =>
    change isolationNumber (TwoCoreOpening.graph [10] [12] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [10] [12] p q)+6)/7
    exact ReceiverOuterRootApplications.r06_ordinary_ceil p q
  | r07 =>
    change isolationNumber (TwoCoreOpening.graph [15] [15] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [15] [15] p q)+6)/7
    exact ReceiverOuterRootApplications.r07_ordinary_ceil p q
  | r08 =>
    change isolationNumber (TwoCoreOpening.graph [15] [16] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [15] [16] p q)+6)/7
    exact ReceiverOuterRootApplications.r08_ordinary_ceil p q
  | r09 =>
    change isolationNumber (TwoCoreOpening.graph [15] [19] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [15] [19] p q)+6)/7
    exact ReceiverOuterRootApplications.r09_ordinary_ceil p q
  | r10 =>
    change isolationNumber (TwoCoreOpening.graph [8] [8,8] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [8] [8,8] p q)+6)/7
    exact CompositeOuterRootApplications.r10_ordinary_ceil p q
  | r11 =>
    change isolationNumber (TwoCoreOpening.graph [8] [1,8] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [8] [1,8] p q)+6)/7
    exact R11ID8577.ordinary_ceil p q
  | r12 =>
    change isolationNumber (TwoCoreOpening.graph [15] [3,15] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [15] [3,15] p q)+6)/7
    exact CompositeOuterRootApplications.r12_ordinary_ceil p q
  | r13 =>
    change isolationNumber (TwoCoreOpening.graph [15] [10,15] p q) ≤
      (3*Fintype.card (TwoCoreOpening.Vertex [15] [10,15] p q)+6)/7
    exact CompositeOuterRootApplications.r13_ordinary_ceil p q

/-- Proposed final consumer for every finite actual tree of diameter at most
nine. It uses the independently accepted actual-counter reduction, with the
fourteen literal obligations supplied by the candidate assembly above.
SOURCE ONLY: no global theorem is claimed accepted by this file's existence. -/
theorem diameter_nine_ordinary_ceiling
    {V : Type} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) (hT : G.IsTree) (hDiam : G.diam ≤ 9) :
    isolationNumber G ≤ MinimalCeil9.ceil3n7 (Fintype.card V) :=
  FourteenCounterexample.diameter_nine_ceiling_of_fourteen
    fourteen_ceiling_obligations G hT hDiam

/-- Same ordinary ceiling in explicit natural-division notation. -/
theorem diameter_nine_ordinary_ceil_formula
    {V : Type} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) (hT : G.IsTree) (hDiam : G.diam ≤ 9) :
    isolationNumber G ≤ (3*Fintype.card V+6)/7 :=
  diameter_nine_ordinary_ceiling G hT hDiam

#print axioms fourteen_ceiling_obligations
#print axioms diameter_nine_ordinary_ceiling
#print axioms diameter_nine_ordinary_ceil_formula

end IsolationGame.FourteenDiameterNineClosure
