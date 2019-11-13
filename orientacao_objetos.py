class Mamiferos():                                             ####Classes####
    olhos = 2
    patas = 4

    def __init__(self, pelo, especie, rabo, cor):               ####Construtor####
        self.especie = especie
        self.pelo = pelo
        self.rabo = rabo
        self.cor = cor

    def comer(self):
        print("Comi")
    def fazer_som(self):
        print("SOM")

mamifero = Mamiferos("curto", "doguinhos caninos", True, "caramelo")        ####Instancias####
mamifero2 = Mamiferos("longo", "agrarios monata", False, "purple")

mamifero.comer()
mamifero2.fazer_som()
print(mamifero.especie)
print(mamifero2.especie)