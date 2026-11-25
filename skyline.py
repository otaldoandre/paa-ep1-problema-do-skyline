"""
Projeto e Análise de Algoritmos - EP1: Problema do Skyline

Integrantes:
    - André Alves Paula da Costa - 834681
    - Nome Completo (RA 000000)
    - Nome Completo (RA 000000)

"""

import sys

from arquivos import ler_edificios, escrever_silhueta
from imagem_svg import gerar_svg


def silhuetaEdificio(edificio):
    """

    Devolve a silhueta de um único edifício (caso base da Divisão e Conquista).

    Parâmetros:
        edificio -> tripla (e, h, d) de inteiros, com 0 ≤ e < d e h > 0
            e -> coordenada horizontal esquerda
            h -> altura
            d -> coordenada horizontal direita

    Retorno:
        Lista com dois pares: [(e, h), (d, 0)].

    ----

    O edifício ocupa o intervalo [e, d): inclui a esquerda e exclui a direita.
    Por isso a altura volta a 0 exatamente em x = d.

    """
    raise NotImplementedError


def unirSilhuetas(s1, s2):
    """

    Une duas silhuetas em uma só, tomando em cada posição a maior das duas
    alturas.

    Parâmetros:
        s1 -> silhueta: lista de pares (x, h), com x estritamente crescente
        s2 -> silhueta no mesmo formato de s1

    Retorno:
        Silhueta da união, no mesmo formato.

    ----

    Convenções da silhueta (Seção 1 do enunciado do EP1):
        - x estritamente crescente;
        - sem dois pares consecutivos com a mesma altura;
        - intervalos sem edifícios aparecem com altura 0;
        - começa com altura positiva e termina com altura 0.

    Se s1 e s2 mudam de altura no mesmo x, as duas mudanças são
    consideradas antes de registrar a altura resultante.

    Complexidade: O(p + q), sendo p e q os números de pares de s1 e s2.

    """
    raise NotImplementedError


def skyline(edificios):
    """

    Calcula a silhueta de um conjunto de edifícios por Divisão e Conquista.

    Parâmetros:
        edificios -> lista de triplas (e, h, d), em qualquer ordem

    Retorno:
        Silhueta: lista de pares (x, h) onde a altura do contorno muda.
        Lista vazia se não houver edifícios.

    ----

    Etapas:
        1. Casos básicos: 0 edifícios -> []; 1 edifício -> silhuetaEdificio.
        2. Divisão: duas metades cujos tamanhos diferem em no máximo 1.
        3. Conquista: skyline de cada metade, recursivamente.
        4. Combinação: unirSilhuetas das duas silhuetas.

    Complexidade esperada pelo enunciado: O(n log n).

    """
    raise NotImplementedError


def main(argv):
    """

    Ponto de entrada do programa: lê a entrada, calcula a silhueta,
    grava a saída e, se pedido, gera a imagem SVG.

    Parâmetros:
        argv -> argumentos da linha de comando (sys.argv)
            argv[1] -> arquivo de entrada
            argv[2] -> arquivo de saída
            argv[3] -> arquivo SVG (opcional)

    Retorno:
        Nenhum.

    ----

    Uso:
        python skyline.py entrada.txt saida.txt
        python skyline.py entrada.txt saida.txt imagem.svg

    Quando o terceiro argumento é dado, gerar o SVG é obrigatório.

    """
    raise NotImplementedError


if __name__ == "__main__":
    main(sys.argv)
