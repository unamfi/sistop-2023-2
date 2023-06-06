# Ejercicio de sincronización
	Rivera García Mauricio
	Ruiz Flores Laura Andrea

## Problema
	El cruce del rio
## Lenguaje 
	Python 
## Estrategia de solucion
Para este problema nos basamos en dos de los ejercicios de ejemplo que se desarrollaron en clase: el ejercicio de la barrera y el de lectores y escritores.

Lo primero que se realizó fue darles diferentes características a los hilos. En este caso, habrá hilos que representen a serfs (los cuales tienen un identificador y son del "tipo cero") y habrá hilos que serán los hackers (que también tienen un identificador y serán del "tipo uno"). El tipo de hilo se define como un argumento de la función `espera` la cual es donde se realiza todo el problema en cuestión.

    threading.Thread(target=espera, args=[numH,0]).start() #llamada a funcion del hacker
    threading.Thread(target=espera, args=[numS,1]).start() #llamada a función del serf

Una vez que se definiera que tipo de desarrollador será el hilo que recorrerá la función, todo lo demás se basará en condicionales que serán utilizadas para liberar las barreras.

Se planteó tener con tres barreras y que los desarrolladores entraran en parejas de un mismo tipo, cubriendo así todos los casos en la barca debería partir (dos serfs y dos hackers, cuatro serfs y cuatro hackers). De esta manera, se implementó una barrera para serfs y otra para hackers la cual sería liberada cuando lleguen dos de ellos. Al suceder esto, todos llegarán a una tercera barrera la cual representará a la balsa, la cual también zarpará en el momento en el que suban cuatro personas a ella (o bien, cuatro hilos).

Cabe mencionar que también fue utilizado un mutex para ir controlando operaciones más delicadas como el conteo de hilos para cumplir la condición de levantamiento de la barrera.

## Dudas y posibles mejoras

Sobre el final se realizó una segunda cuenta de hackers y serfs al llegar a la balsa utilizando otra variable. Se intentó utilizar una sola pero no era muy sencillo ya que esta se iba modificando con respecto a las primeras barreras que había (cuando salen, se reinicia la cuenta para ir controlando la barrera). Para fines de visualización permite ver bien que las balsas están balanceadas, sin embargo, para este punto tal vez ya usaría alrededor de cinco variables para contar. ¿Podría esto optimizarse, o sería mejor dejarlo así?

        cuentaB=cuentaB+1
        if tipo==0:
            cuentaH2=cuentaH2+1
            print("Hackers en la balsa: %d" %cuentaH2)
            print("Serfs en balsa: %d" %cuentaS2)
        if tipo==1:
            cuentaS2=cuentaS2+1
            print("Hackers en la balsa: %d" %cuentaH2)
            print("Serfs en balsa: %d" %cuentaS2)
        print("Total de desarrolladores en la balsa: %d" % cuentaB)
        if cuentaB==soporte_barca:
            barreraB.release()
            print("Arranca la balsa.")

Otra duda que surgió es si se puede adaptar para que sea una sola barrera la que controle el paso de los hackers y serfs, dándole ciertas condiciones. Lo más conveniente para llevar un control fue optar por las tres barreras, pero, ¿sería el mínimo para garantizar que siga habiendo ese control?