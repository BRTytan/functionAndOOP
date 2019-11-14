# Criar as respectivas Classes:

# - Pessoa
# - Pet

# - Modelar atributos no __init__
# - criar métodos na classe Pessoa:
# - Retornar Nome da Pessoa
# - Retornar idade da Pessoa

# - criar métodos na classe Pet:
# - Retornar nome de pet e nome do seu dono
# - retornar todas as infos do pet

# Testar todos os métodos criados printando em tela os resultados solicitados acima.
######################################## Classe Pessoas ########################################
class Pessoas():
############################## Metodo Construtor __Init__ ##############################    
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome
######################################## Metodos ########################################    
    def falar_nome(self):
        nome = str(input("Digite seu nome: "))
        print(f"{nome}")
    def falar_idade(self):
        idade = int(input("Digite seu idade: "))
        print(f"{idade}")
    
######################################## Instancias da classe Pessoas ########################################
pessoa1 = Pessoas()     #Duvida: como faço para chamar o input do metodo#
pessoa2 = Pessoas()
pessoa1.falar_nome()
pessoa1.falar_idade()
pessoa2.falar_nome()
pessoa2.falar_idade()
print(pessoa1.nome)
print(f"O nome é: {pessoa1.nome} e a idade é: {pessoa1.idade}")
print(f"O nome é: {pessoa2.nome} e a idade é: {pessoa2.idade}")




# class Pet():
#     def __init__(self, patas, pelos, olhos, rabo):
#         self.patas = patas
#         self.pelos = pelos
#         self.olhos = olhos
#         self.rabo = rabo
#     def 