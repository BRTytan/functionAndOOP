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
    def __init__(self, pernas, olhos, pele, cabelo, mãos):
        self.pernas = pernas
        self.olhos = olhos
        self.pele = pele
        self.cabelo = cabelo
        self.mãos = mãos
######################################## Metodos ########################################    
    def falar_nome(self):
        nome = input("Digite seu nome: ")
        print(f"{nome}")

######################################## Instancias da classe Pessoas ########################################
pessoaA = Pessoas(2, 2, True, "curto", 2)                               
pessoaA.falar_nome()
print()





# class Pet():
#     def __init__(self, patas, pelos, olhos, rabo):
#         self.patas = patas
#         self.pelos = pelos
#         self.olhos = olhos
#         self.rabo = rabo
#     def 