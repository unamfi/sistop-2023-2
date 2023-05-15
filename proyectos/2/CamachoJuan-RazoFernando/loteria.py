import random

class Proceso:
    def __init__(self, nombre, tiempo_llegada, duracion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.duracion = duracion
        self.tiempo_restante = duracion
        self.prioridad = 0
        self.completado = False

class planificadorLoteria:
    def __init__(self, procesos):
        self.procesos = procesos
        self.tickets = sum([p.duracion for p in procesos])

    def imprimeTabla(self,procesos):
        print('\n\n🔴🔴🔴 Metodo de planificacion por loteria 🔴🔴🔴\n\n')
        print('Lista de procesos:')
        print("Nombre Duracion llegada")
        for i in range(len(procesos)):
            print(f"{procesos[i].nombre}      {str((procesos[i].duracion))+' '}      {procesos[i].tiempo_llegada}")
        print("*Inicia la ejecucion")

    
    def horario(self):
        tiempo = 0
        orden_ejecucion = ""
        tabla_ejecucion = []
        while not all(p.completado for p in self.procesos):
            print("t=%d" % tiempo)
            procesos_listos = [p for p in self.procesos if p.tiempo_llegada <= tiempo and not p.completado]
            if not procesos_listos:
                tiempo += 1
                continue
            
            # Calcular lotería
            loteria = []
            for proceso in procesos_listos:
                for i in range(proceso.duracion):
                    loteria.append(proceso)
            
            #Obtener al ganador
            ganador = random.choice(loteria)
            # Verificar si el proceso está completado
            if ganador.tiempo_restante == ganador.duracion:
                print("   Nuevo proceso!!!")
            ganador.tiempo_restante -= 1
            
            # Imprimir tick para el ganador
            print("   ⌚: {}: 1 tick".format(ganador.nombre))
            
            #Actualizar el orden de ejecución y la tabla
            orden_ejecucion += ganador.nombre
            if not tabla_ejecucion or tabla_ejecucion[-1][0] != ganador:
                tabla_ejecucion.append([ganador, tiempo, tiempo+1])
            else:
                tabla_ejecucion[-1][2] += 1
            
            # Verificar si el proceso está completado
            if ganador.tiempo_restante == 0:
                ganador.completado = True
                print("   Proceso terminado!!!")
            
            tiempo += 1
        
        # Calcular las métricas de ejecución
        tiempo_total = max([p.tiempo_llegada + p.duracion for p in self.procesos])
        metricas_ejecucion = {}
        for proceso in self.procesos:
            tiempo_inicio = [p[1] for p in tabla_ejecucion if p[0] == proceso][0]
            tiempo_final = [p[2] for p in tabla_ejecucion if p[0] == proceso][-1]
            tiempo_ejecucion = tiempo_final - tiempo_inicio
            tiempo_espera = tiempo_inicio - proceso.tiempo_llegada
            indice_penalizacion = tiempo_ejecucion / proceso.duracion
            metricas_ejecucion[proceso.nombre] = [tiempo_inicio, tiempo_final, tiempo_ejecucion, tiempo_espera, indice_penalizacion]
        
        # Imprimir la ejecución y la tabla
        print("\n\nPlanificación realizada: " + orden_ejecucion)
        print("\n\nTabla de ejecución:")
        print('{:<7}  {:<7} {:<7} {:<7} {:<7} {:<7}'.format('Proceso','Inicio','Fin','T','E','P'))
        for proceso in self.procesos:
            metricas = metricas_ejecucion[proceso.nombre]
            print('{:<7}  {:<7} {:<7} {:<7} {:<7} {:<7}'.format(proceso.nombre,metricas[0],metricas[1], metricas[2], metricas[3], metricas[4]))
        
# Generar procesos aleatorios
procesos = []
for i in range(random.randint(5, 8)):
    nombre = chr(i+65)
    if i==0:
        tiempo_llegada=0
    else:
        tiempo_llegada = random.randint(0, 20)
    duracion = random.randint(80, 120)
    procesos.append(Proceso(nombre, tiempo_llegada, duracion))

#Instanciar el planificador y ejecutar la planificación
planificador = planificadorLoteria(procesos)
planificador.imprimeTabla(procesos)
planificador.horario()
