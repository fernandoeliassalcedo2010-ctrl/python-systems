class Personaje:  

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida): 
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    

    def atributos(self):
        print(self.__nombre, ":", sep="")
        print("·Fuerza:", self.__fuerza)
        print("·Inteligencia:", self.__inteligencia)
        print("·Defensa:", self.__defensa)
        print("·Vida:", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("no se puede poner fuerzas negativas , intentalo de nuevo")
        else:
            self.__fuerza = fuerza
class guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    

guts = guerrero("guts", 10, 23, 12, 100, 5)
guts.atributos()
print(guts.espada)
#mi_personaje = Personaje("lupe", 10, 1, 5, 100)
#mi_enemigo = Personaje("doña", 10, 4, 1, 100)

#hemos puesto en modo privado los codigos los atributos y de las funciones de lo quie creamos , el cual no se prodra acceder
#almenos con get y set para los datos OBSARVLO CON GET Y SET Y SIN GET SET

#print(mi_personaje.fuerza) #error no atribuido en la fuerza por el privado
#print(mi_personaje.atributos()) # se puede peo con un none nulo
#mi_personaje.atributos() # se puede normal para el jugador

#mi_personaje.fuerza = 0 # NO CAMBIA NADA
#mi_personaje.atributos()

#mi_personaje.morir() # ya no ocurre nmada por el privado 
    #def __morir(self):
        #self.__vida = 0
        #print(self.__nombre, "ha muerto")
#mi_personaje.atacar(mi_enemigo) Vida de doña es 91
 # [con set y get]
#mi_personaje.set_fuerza(5)
#mi_personaje.atributos() # lo cambia a 5
#print(mi_personaje._Personaje__fuerza) # se puede ingresar con _Personaje y eso siendo privado
