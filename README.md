# paa-ep1-problema-do-skyline

Aqui vão algumas instruções para rodar o projeto.

## 1. Instalar o Python 3.15.2

O professor vai corrigir com **Python 3.15.2** no Windows 11, então todo mundo tem que usar essa versão (se possível!).

1. Baixe e instale o installer em https://www.python.org/downloads/release/python-3152/
2. Abra o terminal de novo e confira:

```powershell
py -0                 # o 3.15 tem que aparecer na lista
py -3.15 --version    # deve mostrar Python 3.15.2
```

> Se você tiver o Python install manager, pode instalar com `py install 3.15.2`.

## 2. Clonar e criar o ambiente virtual

```powershell
git clone [<url-do-repositorio>](https://github.com/otaldoandre/paa-ep1-problema-do-skyline.git)
cd paa-ep1
py -3.15 -m venv .venv
.venv\Scripts\activate
python --version      # deve mostrar Python 3.15.2
```

O projeto não tem dependências externas, então não há nada para instalar com `pip`.

No **VS Code**: `Ctrl+Shift+P` → **Python: Select Interpreter** → escolha o `.venv`. Assim o terminal integrado já abre com o ambiente ativado.

> A pasta `.venv` não vai para o Git. Cada um cria a sua aí.
 o Git.

## 3. Estrutura do projeto até agora

| Arquivo | O que tem                                                                                      |
| --- |------------------------------------------------------------------------------------------------|
| `skyline.py` | Arquivo principal: `skyline`, `unirSilhuetas`, `silhuetaEdificio` e `main`                     |
| `arquivos.py` | Leitura da entrada e escrita da saída                                                          |
| `imagem_svg.py` | Geração do SVG                                                                                 |
| `testes/` | Casos de teste e script que roda todos eles                                                    |
| `README.txt` | README da entrega (instruções e análise pedidas no enunciado, ainda não foi feito, obviamente) |

## 4. Combinados

- As funções obrigatórias mantêm o nome do enunciado (camelCase). Funções auxiliares em `snake_case` (convenção correta do Python...).
- Todo arquivo `.py` começa com o cabeçalho com nomes e RAs.

## 5. Prazos e to-do list

**Entrega no AVA: 12/12/2026** (oficial). Meta (sugestão): **10/12**. Cada dia de atraso tira 1 ponto.

Vai aí uma sugestão de como podemos dividir o trabalho:

| Marco | Data |
| --- | --- |
| Código e testes prontos | 30/11 |
| README.txt pronto | 04/12 |
| Gravar o vídeo | 06/12 |
| Entregar | 10/12 |


Lembrando que temos o EP2 para entregar, que é mais complicado e trabalhoso que o EP1!!
### Código

- [ ] `silhuetaEdificio`
- [ ] `unirSilhuetas` (mudanças no mesmo x nas duas silhuetas, sem pontos redundantes, O(p + q))
- [ ] `skyline` recursivo (casos básicos, divisão em metades, conquista, união)
- [ ] `ler_edificios` e `escrever_silhueta` (n = 0 gera só a linha `0`)
- [ ] `main` com o terceiro argumento (SVG) opcional
- [ ] `gerar_svg` (contorno + preenchimento, proporções, vãos visíveis; entrada vazia = só a linha de base)

### Testes (entrada + saída esperada)

- [x] Exemplo do enunciado
- [ ] Entrada vazia
- [ ] Um único edifício
- [ ] Edifícios separados
- [ ] Sobreposição parcial
- [ ] Edifício inteiramente contido em outro
- [ ] Edifícios de mesma altura
- [ ] Edifícios que começam ou terminam na mesma coordenada
- [ ] Um edifício começando onde outro termina
- [ ] Edifícios repetidos
- [ ] Entradas em ordens diferentes
- [ ] `rodar_testes.py` comparando as saídas e conferindo as convenções

### Entrega

- [ ] README.txt: instruções de execução e dos testes
- [ ] README.txt: análise (casos básicos, divisão, recursão, união, correção, recorrência, tempo e espaço com a pilha)
- [ ] README.txt e vídeo: quais ferramentas de IA foram usadas e como
- [ ] Cabeçalho de todos os `.py` com nomes, RAs e link do vídeo
- [ ] Testar no Windows com Python 3.15.2
- [ ] Vídeo: todos aparecem e se identificam, ~5 a 7 min cada, máx. 20 min, demo com entrada, saída e SVG
- [ ] Enviar no AVA (só uma pessoa) com o link do vídeo
