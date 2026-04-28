# 1. Soma de Valores Pares e Ímpares

**Entrada:** valores inteiros (`num`)

**Processamento:** soma dos valores pares (`sumeven`) e soma dos valores ímpares (`sumuneven`)

**Saída:** apresentar (`sumeven`) e (`sumuneven`)

## Algoritmo

1. Declarar e inicializar as variáveis `num = 0`, `sumeven = 0`, `sumuneven = 0`, `count = 0`, `evenoruneven = 0` do tipo inteiro.
2. Enquanto `count` for menor que `10`, executar:
   1. Incrementar `count` em `1`.
   2. Ler um valor inteiro e armazenar em `num`.
   3. Calcular o resto da divisão de `num` por `2` e armazenar em `evenoruneven`.
   4. Se `evenoruneven` for igual a `0`, somar `num` em `sumeven`.
   5. Caso contrário, somar `num` em `sumuneven`.
3. Apresentar o valor da soma dos números pares (`sumeven`).
4. Apresentar o valor da soma dos números ímpares (`sumuneven`).

---

# 2. Soma de Valores até Número Negativo

**Entrada:** valores inteiros (`num`)

**Processamento:** soma de todos os valores digitados (`sum`)

**Saída:** apresentar (`sum`)

## Algoritmo

1. Declarar e inicializar as variáveis `num = 0`, `sum = 0` do tipo inteiro.
2. Enquanto verdadeiro, executar:
   1. Ler um valor inteiro e armazenar em `num`.
   2. Somar `num` em `sum`.
   3. Se `num` for menor que `0`, interromper o laço.
3. Apresentar o valor da soma de todos os números (`sum`).

---

# 3. Determinação do Menor e Maior Valor

**Entrada:** valores inteiros (`num`)

**Processamento:** determinação do menor (`lowest`) e do maior valor (`highest`)

**Saída:** apresentar (`lowest`) e (`highest`)

## Algoritmo

1. Declarar e inicializar as variáveis `num = 0`, `count = 0`, `lowest = 0`, `highest = 0` do tipo inteiro.
2. Enquanto `count` for menor que `15`, executar:
   1. Incrementar `count` em `1`.
   2. Ler um valor inteiro e armazenar em `num`.
   3. Se `count` for igual a `1`, atribuir `num` a `lowest` e `highest`.
   4. Senão, se `num` for maior que `highest`, atribuir `num` a `highest`.
   5. Senão, se `num` for menor que `lowest`, atribuir `num` a `lowest`.
3. Apresentar o menor valor (`lowest`).
4. Apresentar o maior valor (`highest`).

---

# 4. Média de Valores Acima e Abaixo de 10

**Entrada:** valores inteiros (`num`)

**Processamento:**  

- soma e contagem dos valores maiores ou iguais a 10 (`sumhigh`, `counthigh`)  
- soma e contagem dos valores menores que 10 (`sumlow`, `countlow`)  
- cálculo das médias (`highavg`, `lowavg`)  

**Saída:** apresentar (`highavg`) e (`lowavg`)

## Algoritmo

1. Declarar e inicializar as variáveis `num = 0`, `count = 0`, `counthigh = 0`, `countlow = 0`, `sumhigh = 0`, `sumlow = 0`, `highavg = 0`, `lowavg = 0` do tipo inteiro (exceto médias que podem ser reais).
2. Enquanto `count` for menor que `10`, executar:
   1. Incrementar `count` em `1`.
   2. Ler um valor inteiro e armazenar em `num`.
   3. Se `num` for maior ou igual a `10`:
      1. Incrementar `counthigh` em `1`.
      2. Somar `num` em `sumhigh`.
   4. Caso contrário:
      1. Incrementar `countlow` em `1`.
      2. Somar `num` em `sumlow`.
3. Calcular a média dos valores maiores ou iguais a `10`: `highavg = sumhigh / counthigh`.
4. Calcular a média dos valores menores que `10`: `lowavg = sumlow / countlow`.
5. Apresentar a média dos valores maiores ou iguais a `10` (`highavg`).
6. Apresentar a média dos valores menores que `10` (`lowavg`).

---

# 5. Jogo de Adivinhação com Tentativas Limitadas

**Entrada:** valor inteiro (`guess`)

**Processamento:**  

- geração de um número aleatório entre 1 e 10 (`num`)  
- controle de tentativas (`count`)  
- verificação do palpite em relação ao número gerado  

**Saída:** mensagens informando acerto, erro ou derrota

## Algoritmo

1. Declarar e inicializar as variáveis `num` (número aleatório entre `1` e `10`), `guess = 0`, `count = 0`.
2. Enquanto `count` for menor que `3`, executar:
   1. Incrementar `count` em `1`.
   2. Ler um valor inteiro e armazenar em `guess`.
   3. Se `guess` for igual a `num`, apresentar mensagem de acerto e encerrar o laço.
   4. Senão, se `count` for igual a `3`, apresentar mensagem de derrota.
   5. Senão, se `guess` for maior que `num`, apresentar mensagem informando que o número é menor.
   6. Senão, se `guess` for menor que `num`, apresentar mensagem informando que o número é maior.
   7. Em caso de erro na leitura (valor não inteiro), apresentar mensagem de valor inválido.

---

# 6. Média Sem o Maior e o Menor Valor

**Entrada:** valores inteiros (`num`)

**Processamento:**  

- soma dos valores (`sum`)  
- identificação do maior (`high`) e menor valor (`low`)  
- remoção do maior e menor da soma  
- cálculo da média (`avg`)  

**Saída:** apresentar (`avg`)

## Algoritmo

1. Declarar e inicializar as variáveis `num = 0`, `sum = 0`, `high = 0`, `low = 0`, `count = 0`, `avg = 0`.
2. Enquanto `count` for menor que `5`, executar:
   1. Ler um valor inteiro e armazenar em `num`.
   2. Incrementar `count` em `1`.
   3. Somar `num` em `sum`.
   4. Se `count` for igual a `1`, atribuir `num` a `high` e `low`.
   5. Senão, se `num` for maior que `high`, atribuir `num` a `high`.
   6. Senão, se `num` for menor que `low`, atribuir `num` a `low`.
   7. Em caso de erro na leitura (valor não inteiro), apresentar mensagem de valor inválido.
3. Subtrair o maior e o menor valor da soma: `sum = (sum - high) - low`.
4. Calcular a média dividindo a soma restante por `3`: `avg = sum / 3`.
5. Apresentar a média dos valores sem o maior e o menor (`avg`).

---

# 7. Contagem de Alunos Aprovados e Reprovados

**Entrada:** notas reais (`grade`)

**Processamento:**  

- cálculo da média de cada aluno (`avg`)  
- contagem de alunos aprovados (`spass`) e reprovados (`notpass`)  

**Saída:** apresentar (`spass`) e (`notpass`)

## Algoritmo

1. Declarar e inicializar as variáveis `avg = 0`, `student = 0`, `grade = 0.0`, `grades = 0`, `spass = 0`, `notpass = 0`.
2. Enquanto `student` for menor que `10`, executar:
   1. Enquanto `grades` for menor que `4`, executar:
      1. Ler um valor real e armazenar em `grade`.
      2. Somar `grade` em `avg`.
      3. Incrementar `grades` em `1`.
      4. Em caso de erro na leitura (valor inválido), apresentar mensagem de erro.
   2. Calcular a média do aluno: `avg = avg / 4`.
   3. Se `avg` for maior ou igual a `7`, incrementar `spass` em `1`.
   4. Caso contrário, incrementar `notpass` em `1`.
   5. Reinicializar `avg = 0` e `grades = 0`.
   6. Incrementar `student` em `1`.
3. Apresentar a quantidade de alunos aprovados (`spass`).
4. Apresentar a quantidade de alunos reprovados (`notpass`).

---

# 8. Soma de Números Entre Dois Valores

**Entrada:** valores inteiros (`num1`, `num2`)

**Processamento:**  

- soma dos valores entre `num1` e `num2` (`sum`)  

**Saída:** apresentar (`sum`)

## Algoritmo

1. Declarar e inicializar as variáveis `num1 = 0`, `num2 = 0`, `sum = 0`, `mid = 0`.
2. Ler dois valores inteiros e armazenar em `num1` e `num2`.
   1. Em caso de erro na leitura (valor inválido), apresentar mensagem de erro.
3. Calcular a soma inicial: `sum = num1 + num2`.
4. Atribuir `num1` à variável `mid`.
5. Enquanto verdadeiro, executar:
   1. Incrementar `mid` em `1`.
   2. Se `mid` for igual a `num2`, interromper o laço.
   3. Caso contrário, somar `mid` em `sum`.
6. Apresentar a soma dos números entre `num1` e `num2` (`sum`).

---

# 9. Tabuada de um Número

**Entrada:** valor inteiro (`val`)

**Processamento:**  

- cálculo da tabuada de 1 a 10 (`result`)  

**Saída:** apresentar os resultados da multiplicação

---

## Algoritmo

1. Declarar e inicializar as variáveis `val = 0`, `number = 0`, `result = 0`.
2. Ler um valor inteiro e armazenar em `val`.
3. Enquanto `number` for menor que `10`, executar:
   1. Incrementar `number` em `1`.
   2. Calcular `result = val * number`.
   3. Apresentar o resultado da multiplicação no formato `val x number = result`.
4. Apresentar o fim da tabuada.

---

# 10. Média de Idade e Pessoa Mais Velha por Estado

**Entrada:** estado (`state`) e idade (`age`)

**Processamento:**  

- soma das idades por estado (`agesp`, `agemg`, `agerj`)  
- contagem de pessoas por estado (`spcount`, `mgcount`, `rjcount`)  
- identificação da maior idade por estado (`oldestsp`, `oldestmg`, `oldestrj`)  
- cálculo das médias por estado  

**Saída:** apresentar médias de idade e maior idade para cada estado

## Algoritmo

1. Declarar e inicializar as variáveis:  
   `state = 0`, `SP = 1`, `MG = 2`, `RJ = 3`  
   `age = 0`, `agesp = 0`, `agemg = 0`, `agerj = 0`  
   `spcount = 0`, `mgcount = 0`, `rjcount = 0`  
   `oldestsp = 0`, `oldestmg = 0`, `oldestrj = 0`.

2. Enquanto verdadeiro, executar:
   1. Apresentar as opções de estados: `1 - SP`, `2 - MG`, `3 - RJ`.
   2. Ler um valor inteiro para `state`.
      1. Se `state` for menor que `0`, encerrar o laço.
      2. Se `state` não estiver entre `SP`, `MG` ou `RJ`, apresentar mensagem de erro e continuar o laço.
      3. Em caso de erro na leitura, apresentar mensagem de erro e continuar o laço.
   3. Ler um valor inteiro para `age`.
      1. Se `age` for menor ou igual a `0`, apresentar mensagem de erro e continuar o laço.
      2. Em caso de erro na leitura, apresentar mensagem de erro e continuar o laço.
   4. Se `state` for igual a `SP`:
      1. Somar `age` em `agesp`.
      2. Incrementar `spcount` em `1`.
      3. Se `age` for maior que `oldestsp`, atualizar `oldestsp`.
   5. Senão, se `state` for igual a `MG`:
      1. Somar `age` em `agemg`.
      2. Incrementar `mgcount` em `1`.
      3. Se `age` for maior que `oldestmg`, atualizar `oldestmg`.
   6. Senão, se `state` for igual a `RJ`:
      1. Somar `age` em `agerj`.
      2. Incrementar `rjcount` em `1`.
      3. Se `age` for maior que `oldestrj`, atualizar `oldestrj`.

3. Se `spcount` for maior que `0`:
   1. Calcular a média: `agesp = agesp / spcount`.
   2. Apresentar a média de idade em SP (`agesp`).
   3. Apresentar a maior idade em SP (`oldestsp`).

4. Se `mgcount` for maior que `0`:
   1. Calcular a média: `agemg = agemg / mgcount`.
   2. Apresentar a média de idade em MG (`agemg`).
   3. Apresentar a maior idade em MG (`oldestmg`).

5. Se `rjcount` for maior que `0`:
   1. Calcular a média: `agerj = agerj / rjcount`.
   2. Apresentar a média de idade em RJ (`agerj`).
   3. Apresentar a maior idade em RJ (`oldestrj`).
