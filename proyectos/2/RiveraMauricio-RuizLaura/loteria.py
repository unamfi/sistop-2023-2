from random import randint

procesos = []
boletos = []
ejecucion = []
primer_proc = 'A'
num_boletos = 1
lim_sup = 0
lim_inf = 0
quantum = 1
resultado = 0
indicador = 0

# Se generan los 5 a 8 procesos aleatorios
var = randint(5,8)
dur1 = round(80/var)
dur2 = round(120/var)
print("Var: %d" %var)
print("Dur1: %d" %dur1)
print("Dur2: %d" %dur2)
for i in range(var):
  procesos.append({'nombre': chr(ord(primer_proc)+i),
                   'duración': randint(dur1,dur2)
                   })
for e in procesos:
  ejecucion.append({'nomproceso' : e['nombre'],
                    'inicio' : 0,
                    'fin' : 0,
                    'tiempototal' : e['duración'],
                    'tiempoespera' : 0,
                    'penalizacion' : 0
                   })

print('Lista de procesos:')
print("Proceso\tDuración")
for proc in procesos:
    print("%2s\t\t%3d" % (proc['nombre'], proc['duración']))
t = 0
res = ''
for b in procesos:
  lim_inf = num_boletos
  lim_sup = lim_inf + (b['duración']-1)
  boletos.append({'proceso': b['nombre'],'min_boleto': lim_inf, 'max_boleto': lim_sup, 'long': b['duración']})
  num_boletos = lim_sup+1
  
print("Proceso   Primer boleto     Último boleto")  
for info in boletos:
  print("%2s\t\t\t\t%d\t\t\t\t%d" % ((info['proceso']),info['min_boleto'],info['max_boleto']))
print("Límite superior: %d" %lim_sup)

print('\nInicia ejecución')

while indicador!=1:
  resultado = 0
  for suma in boletos:
      resultado = resultado + int(suma['long'])
  #verifica que haya procesos sin terminar
  if resultado != 0:
    for p in boletos:
        #Selecciona un boleto al azar
        ganador = randint(1,num_boletos)
        print("\nBoleto ganador ---> %d"%ganador)
        print("Proceso ganador ---> %s"%p['proceso'])
        print("t=%d" % t)
      
        #Cuando un boleto ganador es de un proceso ya terminado    
        if p['long'] <= 0:
          print("El proceso %s ha terminado" % p['proceso'])
        
        else:
          for g in boletos:
            if (ganador == int(g['min_boleto']) or ganador == int(g['max_boleto']) or (ganador > int(g['min_boleto']) and ganador < int(g['max_boleto']))) and int(g['long'])>0:
              res += g['proceso']
              g['long'] = int(g['long'])-quantum
              t += quantum
              print("    ⌚ %s %d tick" % (g['proceso'], t))
              print("Duración actual: %d" % int(g['long']))
              for au in ejecucion:
                if au['nomproceso'] == g['proceso'] and au['inicio'] == 0 and g['long'] > 0:
                  au['inicio'] = t
              for au2 in ejecucion:
                if au2['nomproceso'] == g['proceso'] and int(au2['fin']) == 0 and g['long'] == 0:
                  au2['fin'] = t
  else:
    indicador = 1

#Se coloca el orden en que se ejecutaron los procesos
print("\nPlanificación realizada: \n" + res)
#Duración total de la ejecución
print("\nDuración total: %d\n" % lim_sup)

#Se asigna el Tiempo de espera
for espera in ejecucion:
  espera['tiempoespera'] = int(espera['fin'] - espera['tiempototal'])

#Se asigna la Penalización
for penalizacion in ejecucion:
  penalizacion['penalizacion'] = round((penalizacion['fin'])/(penalizacion['tiempototal']),2)

print("\tTabla de ejecución")
print("Proceso\tInicio\tFin\tT\tE\tP")
for info in ejecucion:
  print("%2s\t\t%d\t\t%d\t%d\t%d\t%2d" % ((info['nomproceso']),info['inicio'],info['fin'],info['tiempototal'],info['tiempoespera'],info['penalizacion']))