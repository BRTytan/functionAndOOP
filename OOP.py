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

class Pessoa():
    def __init__(self, pernas, olhos, pele, cabelo, mãos):              ######Modelar atributos no __init__######
        self.pernas = pernas
        self.olhos = olhos
        self.pele = pele
        self.cabelo = cabelo
        self.mãos = mãos
    def falar_nome(self):
        nome = input("Digite seu nome: ")
        print(f"{nome}")
falar = Pessoa.falar_nome(self)
print(falar)
# class Pet():
#     def __init__(self, patas, pelos, olhos, rabo):
#         self.patas = patas
#         self.pelos = pelos
#         self.olhos = olhos
#         self.rabo = rabo
#     def 