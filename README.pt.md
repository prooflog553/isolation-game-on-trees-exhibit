# O jogo de isolamento em árvores

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Português**

![Limiar de diâmetro entre 9 e 10](assets/diameter-threshold.svg)

**Quantas jogadas pode durar uma partida numa árvore?** Para o limite estudado aqui, a passagem do diâmetro 9 para o 10 muda a resposta.

## Regras do jogo

Dois jogadores escolhem vértices alternadamente. Cada escolha marca o vértice selecionado e todos os seus vizinhos. Uma jogada é válida se marcar pela primeira vez ao menos uma extremidade de uma aresta que antes da jogada tinha as duas extremidades sem marca. É permitido escolher um vértice já marcado. O jogo termina quando não sobra nenhuma aresta com ambas as extremidades sem marcar. Dominator procura minimizar o número de jogadas, enquanto Staller procura maximizá-lo.

No caminho 1–2–3–4–5, jogar em 2 marca 1, 2 e 3. Em seguida, jogar em 3 é válido: isso marca 4, uma extremidade da última aresta com ambas as extremidades sem marca, e encerra a partida.

## Resultados

- **Diâmetro de no máximo 9.** No jogo usual, com todos os vértices inicialmente sem marca e Dominator a jogar primeiro, o valor do jogo numa árvore finita de $n$ vértices é no máximo $\lceil 3n/7\rceil$. O mesmo limite não foi estabelecido quando Staller começa.
- **Diâmetro exatamente 10.** Para cada inteiro $k\ge1$, existe uma árvore com $210k$ vértices cujo valor é pelo menos $91k$, independentemente de quem começa. O limite anterior daria $\lceil 3(210k)/7\rceil=90k$. Isso não afirma que o valor é exatamente $91k$ nem que o contraexemplo de 210 vértices é o menor possível.

## A virada da pesquisa: uma única folha

Ligamos os vértices centrais de três caminhos disjuntos de sete vértices a um novo centro. A árvore tem 22 vértices e a partida dura 9 jogadas sob jogo ótimo quando Dominator começa. Ao acrescentar uma folha ao centro, o diâmetro permanece 8, mas a árvore passa a ter 23 vértices e o valor sobe para 10. Para esse tamanho, arredondar a cota para baixo dá 9 e falha; arredondar para cima dá 10. O contraexemplo levou à mudança da conjectura, mas a conta para duas árvores não prova o novo limite no caso geral.

## Das tentativas à demonstração

No caminho de nove vértices, começar pelo centro leva a quatro jogadas com continuação ótima, enquanto uma abertura livre de Dominator permite terminar em três. O exemplo descarta uma estratégia geral de abertura, não o limite que se pretendia demonstrar.

A construção de diâmetro 10 liga em estrela os centros de $14k$ módulos de 15 vértices. A prova final controla primeiro a fase central e depois o jogo restante. Para diâmetro 9, certificados finitos tratam os casos locais e estratégias para 14 famílias cobrem uma quantidade arbitrária de ramos comuns.

A pessoa responsável orientou a pesquisa e solicitou revisões críticas; os sistemas de IA propuseram e revisaram construções e argumentos. Os programas em Python verificam exemplos e certificados finitos; o Lean verifica enunciados formalizados. Os registros de pesquisa disponíveis têm lacunas.

Em D9, um contraexemplo em florestas pré-marcadas descartou a regra geral de que adicionar um caminho de sete vértices aumenta o valor em no máximo três. Esse exemplo local deve ser distinguido do teorema para árvores conexas inicialmente sem marca. Em D7, também se corrigiu a correspondência do vértice marcado em um grafo auxiliar e se demonstraram separadamente os casos pequenos antes assumidos.

## Explorar e verificar

- [Artigo completo (PDF, inglês)](manuscript/Isolation_Game_Research_Report.pdf) · [Mapa das provas (inglês)](EVIDENCE_MAP.md)
- [História da pesquisa (inglês)](RESEARCH.md) · [Guia de reprodução (inglês)](REPRODUCE.md) · [Fontes e compilação em Lean (inglês)](formal/README.md)
- [Tabuleiro interativo (inglês/chinês)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [Construção D10 (inglês/chinês)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)
- [Guia do tabuleiro (português)](demo/README.pt.md)
- [Licenças e avisos (inglês)](LICENSE_SCOPE.md)


*Curadoria e manutenção do arquivo: Cen Yi (岑弈).*
