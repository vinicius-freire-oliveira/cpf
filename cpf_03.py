# Define uma string contendo dados pessoais, incluindo um CPF
dados_pessoais = "Rafaela Brasil, CPF: 718.457.190-85"

# Importa o módulo de expressões regulares (RegEx)
import re

# Compila uma expressão regular que corresponde ao formato de um CPF
# [0-9]{3}      - corresponde a exatamente três dígitos (0 a 9)
# [.]           - corresponde a um ponto literal
# [0-9]{3}      - corresponde a exatamente três dígitos
# [.]           - corresponde a outro ponto literal
# [0-9]{3}      - corresponde a exatamente três dígitos
# [-]           - corresponde a um hífen literal
# [0-9]{2}      - corresponde a exatamente dois dígitos
padrao = re.compile("[0-9]{3}[.]{1}[0-9]{3}[.]{1}[0-9]{3}[-]{1}[0-9]{2}")

# Usa o padrão compilado para procurar o CPF na string 'dados_pessoais'
# A função search procura a primeira ocorrência que corresponda ao padrão
busca = padrao.search(dados_pessoais)

# Se a busca encontrar uma correspondência (ou seja, 'busca' não for None)
if busca:
    # Captura a correspondência encontrada (o CPF) usando o método 'group'
    cpf = busca.group()
    # Imprime o CPF encontrado
    print(cpf)  # Saída esperada: 718.457.190-85
