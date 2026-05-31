# 1. Pesquisa Salarial e Média de Filhos

**Entrada:** salário (`sal`) e quantidade de filhos (`children`)

**Processamento:**

- soma dos salários (`avgsal`)
- soma da quantidade de filhos (`avgchild`)
- identificação do maior salário (`rich`)
- contagem de pessoas com salário abaixo de R$1200 (`poor`)
- cálculo das médias
- cálculo da porcentagem de pessoas com salário abaixo de R$1200

**Saída:** apresentar média salarial, média de filhos, maior salário e porcentagem de pessoas com salário abaixo de R$1200

## Algoritmo

1. Declarar e inicializar as variáveis `sal = 0.0`, `children = 0.0`, `poor = 0.0`, `rich = 0.0`, `avgsal = 0.0`, `avgchild = 0.0` do tipo real e `count = 0` do tipo inteiro.
2. Para `count` no intervalo de `1` até `20`, executar:
   1. Tentar ler um valor real e armazenar em `sal`.
   2. Tentar ler um valor real e armazenar em `children`.
   3. Se `sal` for maior que `rich`, armazenar `sal` em `rich`.
   4. Se `sal` for menor que `1200`, incrementar `poor` em `1`.
   5. Somar `sal` em `avgsal`.
   6. Somar `children` em `avgchild`.
   7. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Calcular a média salarial: `avgsal = avgsal / 20`.
4. Calcular a média de filhos: `avgchild = avgchild / 20`.
5. Calcular a porcentagem de pessoas com salário abaixo de R$1200: `poor = poor / 20`.
6. Apresentar uma linha separadora.
7. Apresentar a média salarial (`avgsal`).
8. Apresentar a média de filhos (`avgchild`).
9. Apresentar o maior salário (`rich`).
10. Apresentar a porcentagem de pessoas com salário abaixo de R$1200 (`poor`).

---

# 2. Contagem de Números por Intervalos

**Entrada:** valores inteiros (`num`)

**Processamento:**

- contagem de números entre `0` e `25` (`range1`)
- contagem de números entre `26` e `50` (`range2`)
- contagem de números entre `51` e `75` (`range3`)
- contagem de números entre `76` e `100` (`range4`)

**Saída:** apresentar a quantidade de números em cada intervalo

## Algoritmo

1. Declarar e inicializar as variáveis `range1 = 0`, `range2 = 0`, `range3 = 0`, `range4 = 0`, `count = 0` e `num = 0` do tipo inteiro.
2. Para `count` no intervalo de `1` até `20`, executar:
   1. Tentar ler um valor inteiro e armazenar em `num`.
   2. Se `num` estiver entre `0` e `25`, incrementar `range1` em `1`.
   3. Senão, se `num` estiver entre `26` e `50`, incrementar `range2` em `1`.
   4. Senão, se `num` estiver entre `51` e `75`, incrementar `range3` em `1`.
   5. Senão, se `num` estiver entre `76` e `100`, incrementar `range4` em `1`.
   6. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Apresentar uma linha separadora.
4. Apresentar a quantidade de números entre `0` e `25` (`range1`).
5. Apresentar a quantidade de números entre `26` e `50` (`range2`).
6. Apresentar a quantidade de números entre `51` e `75` (`range3`).
7. Apresentar a quantidade de números entre `76` e `100` (`range4`).

---

# 3. Pesquisa de Altura e Sexo

**Entrada:** altura (`height`) e sexo (`sex`)

**Processamento:**

- identificação da maior altura (`tall`)
- identificação da menor altura (`short`)
- soma das alturas das mulheres (`wsum`)
- soma das alturas da turma (`hsum`)
- contagem de mulheres (`women`)
- cálculo das médias

**Saída:** apresentar maior altura, menor altura, média de altura das mulheres e média da turma

## Algoritmo

1. Declarar e inicializar as variáveis `count = 0`, `sex = 0`, `women = 0`, `tall = 0`, `short = 0` do tipo inteiro e `height = 0.0`, `wsum = 0.0`, `hsum = 0.0` do tipo real.
2. Para `count` no intervalo de `1` até `50`, executar:
   1. Tentar ler um valor real e armazenar em `height`.
   2. Tentar ler um valor inteiro e armazenar em `sex`.
   3. Se `tall` for igual a `0` ou `height` for maior que `tall`, armazenar `height` em `tall`.
   4. Senão, se `short` for igual a `0` ou `height` for menor que `short`, armazenar `height` em `short`.
   5. Se `sex` for igual a `2`, incrementar `women` em `1`.
   6. Somar `height` em `wsum`.
   7. Somar `height` em `hsum`.
   8. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Calcular a média de altura das mulheres: `wsum = wsum / women`.
4. Calcular a média de altura da turma: `hsum = hsum / 50`.
5. Apresentar uma linha separadora.
6. Apresentar a maior altura (`tall`).
7. Apresentar a menor altura (`short`).
8. Apresentar a média de altura das mulheres (`wsum`).
9. Apresentar a média de altura da turma (`hsum`).

---

# 4. Contagem de Pessoas por Faixa Etária

**Entrada:** idade (`age`)

**Processamento:**

- contagem de pessoas até `15` anos (`pegi1`)
- contagem de pessoas entre `16` e `30` anos (`pegi2`)
- contagem de pessoas entre `31` e `45` anos (`pegi3`)
- contagem de pessoas entre `46` e `60` anos (`pegi4`)
- contagem de pessoas acima de `60` anos (`pegi5`)
- cálculo das porcentagens

**Saída:** apresentar a quantidade de pessoas em cada faixa etária e as porcentagens

## Algoritmo

1. Declarar e inicializar as variáveis `pegi1 = 0.0`, `pegi2 = 0.0`, `pegi3 = 0.0`, `pegi4 = 0.0`, `pegi5 = 0.0` do tipo real e `count = 0`, `age = 0` do tipo inteiro.
2. Para `count` no intervalo de `1` até `15`, executar:
   1. Tentar ler um valor inteiro e armazenar em `age`.
   2. Se `age` estiver entre `0` e `15`, incrementar `pegi1` em `1`.
   3. Senão, se `age` estiver entre `16` e `30`, incrementar `pegi2` em `1`.
   4. Senão, se `age` estiver entre `31` e `45`, incrementar `pegi3` em `1`.
   5. Senão, se `age` estiver entre `46` e `60`, incrementar `pegi4` em `1`.
   6. Caso contrário, incrementar `pegi5` em `1`.
   7. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Apresentar uma linha separadora.
4. Apresentar a quantidade de pessoas até `15` anos (`pegi1`).
5. Apresentar a quantidade de pessoas entre `16` e `30` anos (`pegi2`).
6. Apresentar a quantidade de pessoas entre `31` e `45` anos (`pegi3`).
7. Apresentar a quantidade de pessoas entre `46` e `60` anos (`pegi4`).
8. Apresentar a quantidade de pessoas acima de `60` anos (`pegi5`).
9. Calcular a porcentagem de pessoas até `15` anos: `pegi1 = pegi1 / 15`.
10. Calcular a porcentagem de pessoas acima de `60` anos: `pegi5 = pegi5 / 15`.
11. Apresentar a porcentagem de pessoas até `15` anos (`pegi1`).
12. Apresentar a porcentagem de pessoas acima de `60` anos (`pegi5`).

---

# 5. Pesquisa de Avaliações e Média de Idade

**Entrada:** idade (`age`) e avaliação (`review`)

**Processamento:**

- contagem de avaliações regulares (`regularsum`)
- contagem de avaliações boas (`goodpercent`)
- soma das idades das pessoas que avaliaram como ótimo (`greatage`)
- contagem de avaliações ótimas (`greatavg`)
- cálculo da média de idade
- cálculo do percentual de avaliações boas

**Saída:** apresentar quantidade de avaliações regulares, percentual de avaliações boas e média de idade das avaliações ótimas

## Algoritmo

1. Declarar e inicializar as variáveis `count = 0`, `age = 0`, `review = 0`, `regularsum = 0` do tipo inteiro e `greatavg = 0.0`, `greatage = 0.0`, `goodpercent = 0.0` do tipo real.
2. Para `count` no intervalo de `1` até `15`, executar:
   1. Apresentar as opções de avaliação:
      - `1` para Regular
      - `2` para Bom
      - `3` para Ótimo
   2. Tentar ler um valor inteiro e armazenar em `age`.
   3. Tentar ler um valor inteiro e armazenar em `review`.
   4. Se `review` for igual a `1`, incrementar `regularsum` em `1`.
   5. Senão, se `review` for igual a `2`, incrementar `goodpercent` em `1`.
   6. Senão, se `review` for igual a `3`:
      1. Somar `age` em `greatage`.
      2. Incrementar `greatavg` em `1`.
   7. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Calcular a média de idade das pessoas que avaliaram como ótimo: `greatavg = greatage / greatavg`.
4. Calcular o percentual de avaliações boas: `goodpercent = goodpercent / 15`.
5. Apresentar uma linha separadora.
6. Apresentar a quantidade de avaliações regulares (`regularsum`).
7. Apresentar o percentual de avaliações boas (`goodpercent`).
8. Apresentar a média de idade das pessoas que avaliaram como ótimo (`greatavg`).

---

# 6. Média de Idade de 20 Pessoas

**Entrada:** idade (`age`)

**Processamento:**

- soma das idades (`avgage`)
- cálculo da média das idades

**Saída:** apresentar a média das idades

## Algoritmo

1. Declarar e inicializar as variáveis `count = 0` e `age = 0` do tipo inteiro e `avgage = 0.0` do tipo real.
2. Para `count` no intervalo de `1` até `20`, executar:
   1. Tentar ler um valor inteiro e armazenar em `age`.
   2. Somar `age` em `avgage`.
   3. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Calcular a média das idades: `avgage = avgage / 20`.
4. Apresentar uma linha separadora.
5. Apresentar a média das idades (`avgage`).

---

# 7. Contagem de Pessoas Maiores de Idade

**Entrada:** idade (`age`)

**Processamento:**

- contagem de pessoas maiores de idade (`adult`)

**Saída:** apresentar a quantidade de pessoas maiores de idade

## Algoritmo

1. Declarar e inicializar as variáveis `count = 0`, `age = 0` e `adult = 0` do tipo inteiro.
2. Para `count` no intervalo de `1` até `20`, executar:
   1. Tentar ler um valor inteiro e armazenar em `age`.
   2. Se `age` for maior ou igual a `18`, incrementar `adult` em `1`.
   3. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Apresentar uma linha separadora.
4. Apresentar a quantidade de pessoas maiores de idade (`adult`).

---

# 8. Mulher Mais Alta e Homem Mais Baixo

**Entrada:** altura (`height`) e sexo (`sex`)

**Processamento:**

- identificação da mulher mais alta (`tallfemale`)
- identificação do homem mais baixo (`shortmale`)

**Saída:** apresentar a altura da mulher mais alta e do homem mais baixo

## Algoritmo

1. Declarar e inicializar as variáveis `height = 0.0`, `shortmale = 0.0`, `tallfemale = 0.0` do tipo real e `count = 0`, `sex = 0` do tipo inteiro.
2. Para `count` no intervalo de `1` até `20`, executar:
   1. Tentar ler um valor real e armazenar em `height`.
   2. Tentar ler um valor inteiro e armazenar em `sex` (`1` para feminino e `2` para masculino).
   3. Se `sex` for igual a `1` e `height` for maior que `tallfemale`, armazenar `height` em `tallfemale`.
   4. Senão, se `sex` for igual a `2` e `shortmale` for igual a `0.0`, armazenar `height` em `shortmale`.
   5. Senão, se `sex` for igual a `2` e `height` for menor que `shortmale`, armazenar `height` em `shortmale`.
   6. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Apresentar uma linha separadora.
4. Apresentar a altura da mulher mais alta (`tallfemale`).
5. Apresentar a altura do homem mais baixo (`shortmale`).

---

# 9. Maior, Menor e Média de 20 Números

**Entrada:** valores inteiros (`num`)

**Processamento:**

- soma dos números (`sum`)
- identificação do maior número (`biggest`)
- identificação do menor número (`smallest`)
- cálculo da média (`avg`)

**Saída:** apresentar maior número, menor número e média dos números

## Algoritmo

1. Declarar e inicializar as variáveis `count = 0`, `num = 0`, `sum = 0`, `biggest = 0`, `smallest = 0` do tipo inteiro e `avg = 0.0` do tipo real.
2. Para `count` no intervalo de `1` até `20`, executar:
   1. Tentar ler um valor inteiro e armazenar em `num`.
   2. Somar `num` em `sum`.
   3. Se `smallest` for igual a `0`, armazenar `num` em `smallest`.
   4. Senão, se `num` for menor que `smallest`, armazenar `num` em `smallest`.
   5. Senão, se `num` for maior que `biggest`, armazenar `num` em `biggest`.
   6. Em caso de erro na leitura (valor inválido), apresentar mensagem de entrada inválida.
3. Calcular a média dos números: `avg = sum / 20`.
4. Apresentar uma linha separadora.
5. Apresentar o maior número (`biggest`).
6. Apresentar o menor número (`smallest`).
7. Apresentar a média dos números (`avg`).
