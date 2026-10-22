

class Personaje:  

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida): 
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

mi_personaje = Personaje("lupe", 10, 1, 5, 100)
mi_enemigo = Personaje("doña", 10, 4, 1, 100)
#mi_personaje.atributos()
mi_personaje.subir_nivel(1, 4, 1)

#mi_personaje.atributos()
#mi_enemigo.atributos()
#print(mi_personaje.esta_vivo())#con return
#como append, remove, insert, clear, primero poner lo que cambiaremos o añadiremos y luego el print , pero esta vez con la varibale mi_personae jutno con los atributops
#mi_personaje.morir()#verdadero o falso
#print(mi_personaje.morir())
#mi_personaje.atributos()

#print(mi_personaje.daño(mi_enemigo)) #muesrea el daño 10
#mi_personaje.atacar(mi_enemigo)#lupe ha realizado 10 puntos de daño a doña Vida de doña es 90




    
