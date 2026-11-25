"""
Projeto e Análise de Algoritmos - EP1: Problema do Skyline

Integrantes:
    - André Alves Paula da Costa - 834681
    - Nome Completo (RA 000000)
    - Nome Completo (RA 000000)

"""


def ler_edificios(caminho):
    """

    Lê o arquivo de entrada e devolve a lista de edifícios.

    Parâmetros:
        caminho -> caminho do arquivo de entrada (UTF-8)

    Retorno:
        Lista de triplas (e, h, d) de inteiros, na ordem do arquivo.

    ----

    Formato do arquivo:
        primeira linha -> n ≥ 0, o número de edifícios
        n linhas seguintes -> três inteiros "e h d" separados por espaço

    Edifício (e, h, d):
        e -> coordenada horizontal esquerda
        h -> altura
        d -> coordenada horizontal direita
    Os valores são inteiros, com 0 ≤ e < d e h > 0.

    """
    raise NotImplementedError


def escrever_silhueta(caminho, silhueta):
    """

    Grava a silhueta no arquivo de saída.

    Parâmetros:
        caminho  -> caminho do arquivo de saída (UTF-8)
        silhueta -> lista de pares (x, h)

    Retorno:
        Nenhum.

    ----

    Formato do arquivo:
        primeira linha -> k, o número de pares
        k linhas seguintes -> dois inteiros "x h" separados por espaço

    Para silhueta vazia (n = 0), o arquivo tem só a linha "0".

    """
    raise NotImplementedError
