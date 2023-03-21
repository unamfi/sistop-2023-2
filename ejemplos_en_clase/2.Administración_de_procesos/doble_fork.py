#!/usr/bin/python3
import os
import time

# ... ¿Y si me da flojera declarar handlers?
# ... ¿Y si no quiero preocuparme de dejar un reguero de procesos "zombie"?
# ... ¿Soy una mala persona?

pid1 = os.fork()
if pid1 == 0:
    # Proceso intermedio (hijo)
    pid2 = os.fork()
    if pid2 == 0:
        # Proceso hijo "efectivo"
        print("El proceso hijo efectivo tiene el PID %d" % os.getpid() )
        time.sleep(10)
        print("OK, ya me voy...")
    else:
        # Proceso intermedio (padre)
        print("El proceso intermedio (%d) lanzó al hijo (%d) y ya se va" %
              (os.getpid(), pid2))
        exit(0)
else:
    # Proceso padre
    print("El proceso padre (%d) lanzó al intermedio (%d), y sigue..." %
          (os.getpid(), pid1))

    time.sleep(5)
    print("El papá se va...")
    exit(1)
