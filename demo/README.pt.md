# Jogar o jogo de isolamento

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

[English](README.md) · [Página inicial em português](../README.pt.md) · [Tabuleiro on-line](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html?lang=pt) · [Construção D10](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html?lang=pt)

Baixe o [tabuleiro HTML independente](index.html) e abra-o no navegador, sem instalação. Escolha uma árvore e quem começa. Você pode clicar em um vértice, selecioná-lo com Tab e pressionar Enter ou Espaço, ou usar os botões de jogadas válidas. A partida é preservada ao trocar de idioma.

Cada jogada cobre o vértice escolhido e seus vizinhos e deve cobrir pela primeira vez uma extremidade de uma aresta laranja. Um vértice já coberto ainda pode ser escolhido se satisfizer essa condição. Os contornos azuis indicam todas as jogadas ótimas de quem joga. O número em cada botão inclui aquela jogada e indica quantas restam se ambos jogarem de forma ótima.

O painel de estratégia mostra os valores iniciais para os dois possíveis primeiros jogadores e uma continuação ótima a partir da posição atual. Em caso de empate, a prévia e a opção de jogar uma jogada ótima escolhem o vértice de menor número.

| Árvore | D começa | S começa | O que experimentar |
|---|---:|---:|---|
| P5 | 1 | 2 | Jogue 2 e depois o vértice 3, já coberto. |
| P9 | 3 | 4 | Compare a abertura livre de D com a abertura obrigatória no centro 5. |
| D8 · 22 vértices | 9 | 10 | Confira o valor de D antes de acrescentar a folha. |
| D8 · 23 vértices | 10 | 10 | Uma folha adicional eleva o valor de D para 10. |

A verificação no navegador em 25 de novembro de 2026 completou as oito partidas ótimas e examinou 141.420 estados alcançáveis e 1.335.806 transições legais. Também testou teclado, ponteiro, desfazer, reiniciar, troca de idioma e layouts de 320 e 375 pixels.

[Guia de reprodução (inglês)](../REPRODUCE.md)
