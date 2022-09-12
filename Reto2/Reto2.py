import numpy as np
from random import randint
import matplotlib.pyplot as plt

#Se realiza la logica donde se pedira el numero de intentos, muestra las simulacion de las demas opciones y la opcion sin cambiar de puerta 
class Simulation:
    def __init__(self):
        intentos =0
        while(intentos <1):
            intentos = IngresarInteger("Ingrese la cantidad de intentos... ")
        self.intentos = intentos
        self.puntucacionesMedia = []
        self.cont = []
    
    def Simulate(self):
        self.TakeDoor()
        
        print(self.puntucacionesMedia)
    
    # Se realiza el calculo para la opcion sin el cambio de puerta
    def TakeDoor(self, ):
        scores = []
        for i in range(0, self.intentos):
            premio = randint(0,2)
            eleccion = randint(0,2)
            # print("eleccion", eleccion)

            if premio == eleccion:
                scores.append( 1)
            else:
                scores.append(0)
        self.puntucacionesMedia.append(np.mean(scores)*100)
        print("")
        print("***************************************************")
        print("Probabilidad sin cambiar puerta en ",self.intentos)
    

#Se realiza el calculo para la opcion del cambio de puerta 
class SimulationConCambio(Simulation):
    def TakeDoor(self):
        for i in range(0, self.intentos):
            scores = []
            for i in range(0, i +1):
                premio = randint(0,2)
                eleccion = randint(0,2)


                newEleccion = [0,1,2]
                newEleccion.remove(eleccion)

                if newEleccion[0] == premio:
                    del newEleccion[1]
                elif newEleccion[1] == premio:
                    del newEleccion[0]
                else:
                    del newEleccion[randint(0, len(newEleccion)-1)]

                eleccion = newEleccion[0]

                if premio == eleccion:
                    scores.append( 1)
                else:
                    scores.append( 0)
            self.puntucacionesMedia.append(np.mean(scores)*100)
        print("")
        print("***************************************************")
        print("Probabilidad cambiando la puerta escogida al inicio, se muestra la probabilidad de cada intento hasta el ", self.intentos)

# Se realiza el calculo para la opcion de cambio de puerta en 4 puertas y sin que el presentador tenga conocimiento de donde se encuentra el premio
class SimulationNuevaPuerta(Simulation):
    def TakeDoor(self):
        
        for i in range(0, self.intentos):
            scores = []
            for i in range(0, i +1):
                premio = randint(0,3)
                eleccion = randint(0,3)

                newEleccion = [0,1,2, 3]
                newEleccion.remove(eleccion)
                
                numero = randint(0, len(newEleccion)-1)
                presentador = newEleccion[numero]
                if presentador == premio:
                    eleccion = presentador
                else:
                    del newEleccion [numero]

                if presentador != premio:
                    eleccion = newEleccion[randint(0, len(newEleccion)-1)]
                # print("nueva eleccion ",eleccion)

                if premio == eleccion:
                    scores.append( 1)
                else:
                    scores.append( 0)
            self.puntucacionesMedia.append(np.mean(scores)*100)
        print("")
        print("***************************************************")
        print("Probabilidad cambiando la puerta escogida al inicio, de las 4 puertas, se muestra la probabilidad de cada intento hasta el ", self.intentos)

#Pedira el ingreso de un numero de acuerdo a las opciones presentadas
def IngresarInteger(mensaje):
    while True:
        try:
            print("")
            choice = int(input(mensaje))
        except ValueError:
            print("Porfavor ingrese un valores numerico")
            continue
        else:
            return choice


# Menu donde se accedera a las opciones presentadas
def Menu():
    print("")
    print("***********************************")
    print("(1) Jugar sin cambiar la puerta")
    print("(2) Jugar cambiando la puerta")
    print("(3) Jugar cambiando la puerta con 4")
    print("(4) Exit")
    print("***********************************")
    print("")

    valores = [1,2,3,4]
    valor = 0
    while (valor not in valores):
        valor = IngresarInteger("Ingrese la eleccion... ")
    
    if valor ==1 :
        simulation = Simulation()
    elif valor == 2:
        simulation = SimulationConCambio()
    elif valor == 3:
        simulation = SimulationNuevaPuerta()
    elif valor == 4:
        exit()
    simulation.Simulate()

    Menu()

if __name__ == "__main__":
    Menu()