# 1. Soma e Média de 15 Números

**Entrada:** valores inteiros (`num`)

**Processamento:**
- soma de todos os valores digitados (`sum`)
- contagem de números digitados (`count`)
- cálculo da média (`avg`)

**Saída:** apresentar (`sum`) e (`avg`)

## Algoritmo

1. Declarar e inicializar as variáveis `num = 0`, `count = 0`, `sum = 0` do tipo inteiro e `avg = 0.0` do tipo real.
2. Para `count` no intervalo de `1` até `15`, executar:
   1. Tentar ler um valor inteiro e armazenar em `num`.
   2. Somar `num` em `sum`.
   3. Em caso de erro na leitura (valor não inteiro), apresentar mensagem de entrada inválida.
3. Calcular a média dos valores: `avg = sum / 15`.
4. Apresentar uma linha separadora.
5. Apresentar o valor da soma dos números (`sum`).
6. Apresentar o valor da média dos números (`avg`).

---

# 2. Média de Idades e Contagem de Pessoas com Peso Superior a 80 kg

**Entrada:** idade (`age`) e peso (`weight`)

**Processamento:**
- soma das idades (`agesum`)
- contagem de pessoas com peso superior a 80 kg (`heavy`)
- cálculo da média das idades (`avgage`)

**Saída:** apresentar (`heavy`) e (`avgage`)

## Algoritmo

1. Declarar e inicializar as variáveis `age = 0`, `agesum = 0`, `count = 0`, `heavy = 0` do tipo inteiro e `weight = 0.0`, `avgage = 0.0` do tipo real.
2. Para `count` no intervalo de `1` até `10`, executar:
   1. Tentar ler um valor inteiro e armazenar em `age`.
   2. Tentar ler um valor real e armazenar em `weight`.
   3. Somar `age` em `agesum`.
   4. Se `weight` for maior que `80`, incrementar `heavy` em `1`.
   5. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Calcular a média das idades: `avgage = agesum / 10`.
4. Apresentar uma linha separadora.
5. Apresentar o número de pessoas com peso superior a 80 kg (`heavy`).
6. Apresentar a média das idades (`avgage`).

---

# 3. Contagem de Números em Intervalos Específicos

**Entrada:** valores inteiros (`num`)

**Processamento:**
- contagem de números maiores que 10 (`biggerthan10`)
- contagem de números menores que 5 (`lessthan5`)
- contagem de números entre 7 e 15 (`btwn7n15`)

**Saída:** apresentar (`biggerthan10`), (`lessthan5`) e (`btwn7n15`)

## Algoritmo

1. Declarar e inicializar as variáveis `count = 0`, `num = 0`, `biggerthan10 = 0`, `lessthan5 = 0`, `btwn7n15 = 0` do tipo inteiro.
2. Para `count` no intervalo de `1` até `9`, executar:
   1. Tentar ler um valor inteiro e armazenar em `num`.
   2. Se `num` for maior que `10`, incrementar `biggerthan10` em `1`.
   3. Se `num` for menor que `5`, incrementar `lessthan5` em `1`.
   4. Se `num` for maior ou igual a `7` e menor ou igual a `15`, incrementar `btwn7n15` em `1`.
   5. Em caso de erro na leitura (valor não inteiro), apresentar mensagem de entrada inválida.
3. Apresentar uma linha separadora.
4. Apresentar a quantidade de números maiores que `10` (`biggerthan10`).
5. Apresentar a quantidade de números menores que `5` (`lessthan5`).
6. Apresentar a quantidade de números entre `7` e `15` (`btwn7n15`).

---

# 4. Média de Idades por Sexo e Geral

**Entrada:** idade (`age`) e sexo (`sex`)

**Processamento:**
- soma das idades de todas as pessoas (`allavg`)
- soma das idades dos homens (`maleavg`)
- soma das idades das mulheres (`femavg`)
- cálculo das médias

**Saída:** apresentar média geral, média masculina e média feminina

## Algoritmo

1. Declarar e inicializar as variáveis `count = 0`, `age = 0`, `sex = 0` do tipo inteiro e `allavg = 0.0`, `maleavg = 0.0`, `femavg = 0.0` do tipo real.
2. Para `count` no intervalo de `1` até `12`, executar:
   1. Tentar ler um valor inteiro e armazenar em `age`.
   2. Tentar ler um valor inteiro e armazenar em `sex` (1 para masculino, 2 para feminino).
   3. Se `sex` for igual a `1`, somar `age` em `maleavg`.
   4. Senão, se `sex` for igual a `2`, somar `age` em `femavg`.
   5. Somar `age` em `allavg`.
   6. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Calcular a média geral: `allavg / 12`.
4. Calcular a média das idades dos homens: `maleavg / 12`.
5. Calcular a média das idades das mulheres: `femavg / 12`.
6. Apresentar uma linha separadora.
7. Apresentar a média geral das idades.
8. Apresentar a média das idades dos homens.
9. Apresentar a média das idades das mulheres.

---

# 5. Média de Valores até Número Negativo

**Entrada:** valores inteiros (`num`)

**Processamento:**
- soma dos valores digitados (`sum`)
- contagem de valores válidos (`count`)
- cálculo da média (`avg`)

**Saída:** apresentar (`avg`)

## Algoritmo

1. Declarar e inicializar as variáveis `num = 0`, `sum = 0`, `count = 0` do tipo inteiro.
2. Enquanto verdadeiro, executar:
   1. Tentar ler um valor inteiro e armazenar em `num`.
   2. Se `num` for menor que `0`:
      1. Apresentar mensagem de encerramento.
      2. Interromper o laço.
   3. Somar `num` em `sum`.
   4. Incrementar `count` em `1`.
   5. Em caso de erro na leitura (valor não inteiro), apresentar mensagem de entrada inválida.
3. Calcular a média dos valores: `avg = sum / count`.
4. Apresentar uma linha separadora.
5. Apresentar a média dos números digitados (`avg`).

---

# 6. Pesquisa de Satisfação com Contagem de Avaliações

**Entrada:** avaliação (`review`) e decisão de continuar (`yesorno`)

**Processamento:**
- contagem de avaliações em cada nível (`ruim`, `razoavel`, `satisf`, `bom`, `otimo`)
- validação da entrada de avaliação
- controle de repetição com base na decisão do usuário

**Saída:** apresentar a quantidade de avaliações em cada nível

## Algoritmo

1. Declarar e inicializar as variáveis `review = 0`, `yesorno = 0`, `ruim = 0`, `razoavel = 0`, `satisf = 0`, `bom = 0`, `otimo = 0` do tipo inteiro.
2. Apresentar mensagem inicial explicando a pesquisa de satisfação.
3. Enquanto verdadeiro, executar:
   1. Apresentar a tabela de opções de avaliação (1 a 5).
   2. Ler um valor inteiro e armazenar em `review`.
   3. Se `review` não estiver entre `1` e `5`, apresentar mensagem de avaliação inválida e continuar o laço.
   4. Se `review` for igual a `1`, incrementar `ruim` em `1`.
   5. Senão, se `review` for igual a `2`, incrementar `razoavel` em `1`.
   6. Senão, se `review` for igual a `3`, incrementar `satisf` em `1`.
   7. Senão, se `review` for igual a `4`, incrementar `bom` em `1`.
   8. Senão, se `review` for igual a `5`, incrementar `otimo` em `1`.
   9. Ler um valor inteiro e armazenar em `yesorno` (1 para continuar, 0 para encerrar).
   10. Se `yesorno` for igual a `1`, continuar o laço.
   11. Caso contrário, interromper o laço.
4. Apresentar uma linha separadora.
5. Apresentar o grau de satisfação com a contagem de cada nível:
   - `ruim`
   - `razoavel`
   - `satisf`
   - `bom`
   - `otimo`