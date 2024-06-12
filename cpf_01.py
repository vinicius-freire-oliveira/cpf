# Define a classe Pessoa
class Pessoa:
    # Atributo de classe que define o tamanho padrão do CPF
    tamanho_cpf = 11

# Cria uma instância da classe Pessoa
p = Pessoa()

# Imprime o valor do atributo de classe 'tamanho_cpf' acessado pela instância 'p'
print(p.tamanho_cpf)  # Saída: 11

# Atribui um novo valor ao atributo 'tamanho_cpf' na instância 'p'
p.tamanho_cpf = 12

# Imprime o valor do atributo 'tamanho_cpf' da instância 'p', que agora é 12
print(p.tamanho_cpf)  # Saída: 12

# Imprime o valor do atributo de classe 'tamanho_cpf' acessado diretamente pela classe 'Pessoa'
print(Pessoa.tamanho_cpf)  # Saída: 11
