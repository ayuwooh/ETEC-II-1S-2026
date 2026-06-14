#!/bin/bash

# Função que adiciona o prefixo 'processado_' ao nome do arquivo
renomear_arquivo() { # Nome da função
    local arquivo_atual=$1 # Variavel que faz com que o próximo arquivo selecionado no terminal seja o alvo
    local novo_nome="processado_${arquivo_atual}" # Variavel que define o novo nome
    mv "$arquivo_atual" "$novo_nome" # Renomeia o arquivo pelo novo nome
    echo " -> Arquivo renomeado para: $novo_nome" # Apresenta o novo nome
}

# === Script Principal ===
diretorio_alvo="./dados_teste" # Define o diretório alvo

# Criando ambiente de teste
mkdir -p "$diretorio_alvo" # Cria um diretório, "-p" faz com que seja feito dentro de outro diretório caso contenha no código
touch "$diretorio_alvo/relatorio1.txt" "$diretorio_alvo/relatorio2.txt" # Cria um arquivo txt no diretório

echo "=== Iniciando Processamento ===" # Apresenta a mensagem

if [[ -d $diretorio_alvo ]]; then # Checa se a variavel é um diretório
    cd "$diretorio_alvo" || exit 1 # Se sim, entra nele, caso contrário, sai
    
    # Loop em todos os .txt
    for arquivo in *.txt; do # Pega cada arquivo de qualquer nome e de extensão .txt;
        if [[ -f $arquivo ]]; then # Checa se é um arquivo comum;
            echo "Encontrado: $arquivo" # Apresenta que encontrou o arquivo;
            renomear_arquivo "$arquivo" # E renomeia o arquivo usando a função renomear_arquivo
        fi # Termina o código if/else
    done # Termina o código inteiro
    
    cd .. # Volta um diretório
else # Caso contrário;
    echo "Erro: O diretório $diretorio_alvo não existe." # Apresenta a mensagem
fi # Termina o código if/else

echo "=== Fim do Processamento ===" # Apresenta a mensagem

# Limpando ambiente (opcional para testes)
rm -r "$diretorio_alvo" # Apaga o diretório criado para esse experimento