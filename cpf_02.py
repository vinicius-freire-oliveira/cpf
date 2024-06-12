# Define a classe Pessoa
class Pessoa:
    # Atributo de classe que define o tamanho padrão do CPF
    tamanho_cpf = 11

    # Método construtor que inicializa os atributos 'cpf' e 'nome'
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    # Método para validar se o CPF tem o comprimento correto
    def valida_cpf(self):
        # Retorna True se o comprimento do CPF for igual ao tamanho_cpf, senão retorna False
        return True if len(self.cpf) == __class__.tamanho_cpf else False

# Cria uma instância da classe Pessoa com CPF de 11 dígitos
pe = Pessoa('00000000001', 'Ruby')
# Imprime o resultado da validação do CPF (True)
print(pe.valida_cpf())

# Cria uma instância da classe Pessoa com CPF de 10 dígitos
pe = Pessoa('0000000000', 'Cristal')
# Imprime o resultado da validação do CPF (False)
print(pe.valida_cpf())
