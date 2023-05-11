/**
 * Colores para cada uno de los procesos
 */
const colors = {
  a: "#2370ee",
  b: "#3b23ee",
  c: "#a123ee",
  d: "#ee23d6",
  e: "#ee2370",
  f: "#ee3c23",
  g: "#1abc9c",
  h: "#f4d03f",
}

/**
 * Nombres de los procesos utilizados
 */
const processesName = [
  "a", "b", "c", "d", "e", "f", "g", "h"
]

/**
 * Clase que representa un proceso que se ejecutará a través
 * de un planificador de procesos.
 */
class Process {
  /**
   * El nombre del proceso
   */
  #name;

  /**
   * Duración del proceso en Ticks
   */
  #duration;

  /**
   * Tick en el que iniciará en la simulación
   */
  #start;

  /**
   * Tick en el que termina. Inicialmente tiene el valor de `null`
   */
  #end;

  /**
   * El tiempo restante de procesamiento.
   */
  #missingTime;

  get name() { return this.#name }
  get duration() { return this.#duration }
  get start() { return this.#start }
  get end() { return this.#end }
  get missing() { return this.#missingTime }
  get metrics() {
    if (this.#end === null)
      throw new Error("This process hasn't ended yet.")
    
    // Tiempo de respuesta
    const T = this.#end - this.#start + 1;

    // Tiempo de espera
    const E = T - this.#duration;

    // Proporción de penalización
    const P = T / this.#duration;

    return {
      T, E, P
    };
  }

  constructor({ name, duration, start }) {
    this.#name = name;
    this.#duration = duration;
    this.#start = start;
    this.#end = null;
    this.#missingTime = duration;
  }

  /**
   * Disminuye uno al tiempo de procesamiento restante. En caso de que se 
   * termine de ejecutar, se asigna el tickNumber al valor de #end.
   * @param {Number} tickNumber el tick que se está ejecutando actualmente.
   */
  execute(tickNumber) {
    if (this.#missingTime > 0)
      this.#missingTime--;
    else {
      throw Error(`This process cannot be executed (${this.#name}).`);
    }

    if (this.#missingTime == 0)
      this.#end = tickNumber;
  }
}

/**
 * Clase que describe un proceso para el algoritmo
 * de Retroalimentación Multinivel
 */
class MultilevelProcess extends Process {
  /**
   * La prioridad del proceso especificada con un número entero.
   * Entre más grande el número, menor prioridad.
   */
  #priority;

  get priority() { return this.#priority };

  constructor({ name, duration, start }) {
    super({ name, duration, start });
    this.#priority = -1;
  }

  /**
   * Degrada la prioridad en una unidad.
   */
  updatePriority() {
    if (this.end === null)
      this.#priority++;
    else
      this.#priority = null;
  }
}

/**
 * Clase que describe un proceso para el algoritmo
 * de Lotería
 */
class LotteryProcess extends Process {

  /**
   * Los tickets asociados al proceso
   */
  #tickets;

  get tickets() { return [...this.#tickets] };

  constructor({ name, duration, start }, tickets) {
    super({ name, duration, start });
    this.#tickets = tickets;
  }

  /**
   * Indica si el proceso tiene asignado o no un ticket.
   * @param {Number} number el número de ticket.
   * @returns valor lógico del resultado.
   */
  containsTicket(number) {
    return this.#tickets.includes(number);
  }
}

/**
 * Clase abstracta que representa un
 * algoritmo de planificación
 */
class AbstractProcessPlanningAlgorithm {
  /**
   * Los procesos asociados al algoritmo
   */
  #processes

  /**
   * El tick actual del algoritmo
   */
  #currentTick

  /**
   * Objeto generador para iterar en el algoritmo
   */
  #generator

  get processes() {return this.#processes}
  get currentTick() {return this.#currentTick}
  get generator() {return this.#generator}

  constructor(processes) {
    this.#processes = processes;
  }

  /**
   * Inicializa el algorimo
   */
  init() {
    this.#currentTick = 0;
    this.#generator = this._exec();
  }

  /**
   * Incrementa el ticket
   */
  setNextTick() {
    this.#currentTick++;
  }

  /**
   * Ejecuta el siguiente movimiento del algoritmo.
   * @returns un objeto con el movimiento realizado en el algoritmo
   */
  run() {
    return this.generator.next()
  }

  /**
   * Función generadora para el funcionamiento del algoritmo.
   */
  *_exec() {
    throw new Error("Unimplemented method.")
  }
}

/**
 * Clase que representa el algoritmo de planificación por Retroalimentación
 * Multinivel.
 */
class MultilevelAlgorithm extends AbstractProcessPlanningAlgorithm {
  /**
   * Las colas con los procesos de prioridad
   */
  #queues

  get queues() {return this.#queues}

  constructor(processes) {
    super(processes);
  }

  init() {
    super.init();
    this.#queues = {};
  }

  /**
   * Identifica los procesos que acaban de llegar a la ejecución en
   * el tick actual.
   * @returns una lista con los procesos que acaban de llegar.
   */
  getArrivalProcesses() {
    const newProcesses = this.processes
      .filter(p => p.priority === -1)
      .filter(p => p.start === this.currentTick)

    newProcesses
      .forEach(p => {
        p.updatePriority();
        this.#queues[0].push(p);
      });

    return newProcesses;
  }

  *_exec() {
    while (this.processes.some(p => p.end === null)) {
      // Se crea la cola [0]
      if (!this.#queues[0])
        this.#queues[0] = []

      // Nuevos procesos
      let arrivalProcesses = this.getArrivalProcesses();

      // Llegan nuevos procesos
      if (arrivalProcesses.length > 0)
        yield {
          type: "arrival",
          payload: arrivalProcesses
        };

      // Se obtiee la cola de mayor prioridad
      const q = Object.keys(this.#queues)
        .filter(k => {
          return this.#queues[k].length > 0;
        })
        .sort()[0];

      if (q !== undefined) {
        // Primer proceso
        const p = this.#queues[q][0];

        const prevPriority = p.priority;

        // Se dan 2^n ticks de ejecución
        let i = 2 ** q;
        do {
          if (i < 2 ** q) {
            arrivalProcesses = this.getArrivalProcesses();
            
            // Llega un nuevo proceso durante la ejecución
            if (arrivalProcesses.length > 0)
              yield {
                type: "arrival-but",
                payload: arrivalProcesses
              };
          }

          p.execute(this.currentTick);
          this.setNextTick();
          
          // Se notifica ejecución
          yield {
            type: "execution",
            payload: p
          };

          i--;

        } while (p.end === null && i > 0);

        p.updatePriority();
        const newPriority = p.priority;

        this.#queues[prevPriority] = this.#queues[prevPriority].splice(1);

        // Si no ha termina su ejecución, se agrega a nueva cola de prioridad
        if (p.end === null) {
          if (!this.#queues[newPriority])
            this.#queues[newPriority] = [];

          this.#queues[newPriority].push(p);

          // Se notifica cambio de prioridad
          yield {
            type: "priority",
            payload: p
          }
        } else {
          // Se notifica término de proceso
          yield {
            type: "remove",
            payload: p
          }
        }

      } else {
        this.setNextTick();
        // Se notifica "no hay nada que hacer"
        yield {
          type: "idle",
          payload: null
        };
      }
    }
    return null;
  }
}

/**
 * Clase que representa el algoritmo de planificación por
 * Lotería.
 */
class LotteryAlgorithm extends AbstractProcessPlanningAlgorithm {
  /**
   * Procesos que se encuentran en ejcución actualmente
   */
  #avaibleProcesses

  get avaibleProcesses() {return this.#avaibleProcesses}

  constructor(processes) {
    super(processes);
  }

  init() {
    super.init();
    this.#avaibleProcesses = [];
  }

  *_exec() {
    while (this.processes.some(p => p.end == null)) {
      // Se identifican nuevos proceso que acaba de llegar
      const newProcesses = this.processes
        .filter(p => p.start === this.currentTick);
      if (newProcesses.length > 0) {
        newProcesses.forEach(p => this.#avaibleProcesses.push(p));
        // Se notifica nuevo proceso
        yield {
          type: "arrival",
          payload: newProcesses
        }
      }

      // Tickets de los procesos que aún no han terminado
      const avaibleTickets = this.#avaibleProcesses.flatMap(t => t.tickets);

      // Selección del ticket
      const randIndex = Math.round((avaibleTickets.length - 1) * Math.random());
      const selectedTicket = avaibleTickets[randIndex];

      // Selección del proceso asociado a dicho ticket
      const p = this.#avaibleProcesses.filter(p => p.containsTicket(selectedTicket))[0];

      if (p) {
        p.execute(this.currentTick);
        // Se notifica ejecución
        yield {
          type: "execution",
          payload: p,
          ticket: selectedTicket
        };

        if (p.end !== null) {
          this.#avaibleProcesses = this.#avaibleProcesses
            .filter(p => p.end === null);
          // Se notifica finalización de proceso
          yield {
            type: "remove",
            payload: p
          }
        }
      } else {
        // Se notifica "no hay nada que hacer"
        yield {
          type: "idle",
          payload: null
        };
      }
      this.setNextTick();
    }
    return null;
  }
}

function showTickets(algorithm) {
  const panel = document.getElementById("tickets-panel");
  const baseNode = document.createElement("div")

  panel.innerHTML = "";

  algorithm.avaibleProcesses
    .forEach(p => {
      const node = baseNode.cloneNode();
      const content = p.tickets
        .map(p => `<span>${p}</span>`)
        .join(', ');
      node.innerHTML = `<span>${p.name} (${p.missing})</span> <span>[</span> ${content} <span> ]</span>`
      panel.appendChild(node);
    })
}

function showMessage(response) {
  let message = '';
  let ticketString = isNaN(response.ticket) ? '' : `(${response.ticket})`;
  switch (response.type) {
    case "execution":
      message = `Se ejecuta el proceso [${response.payload.name}] ${ticketString}`
      break;
    case "remove":
      message = `Termina el proceso [${response.payload.name}]`
      break;
    case "priority":
      message = `Cambia la prioridad de [${response.payload.name}]`
      break;
    case "idle":
      message = `Nada que hacer`;
      break;
    case "arrival":
      message = `Llegada de: [${response.payload.map(p => p.name).join(', ')}]`
      break;
    case "arrival-but":
      message = `Llegada de: [${response.payload.map(p => p.name).join(', ')}], pero se está ejecutando otro proceso`
  }
  console.log(message);
  document.getElementById("message-container").textContent = message;
}

function showQueues(algorithm) {
  const panel = document.getElementById("queues-panel");
  const baseNode = document.createElement("div")
  const queues = algorithm.queues;

  panel.innerHTML = "";

  Object.keys(queues)
    .sort()
    .forEach(k => {
      const node = baseNode.cloneNode();
      const content = queues[k]
        .filter(p => p.end === null)
        .map(p => `<span>${p.name} (${p.missing})</span>`)
        .join(', ');
      node.innerHTML = `<span>${k}</span> <span>[</span> ${content} <span> ]</span>`
      panel.appendChild(node);
    })
}

function addProcessCell(process) {
  const panel = document.getElementById("process-panel");
  const node = document.createElement("span");

  node.innerHTML = `<div class="cell">${process?.name || ''}</div>`;
  if (process) node.style.backgroundColor = colors[process.name];
  else node.style.backgroundColor = "white";
  panel.appendChild(node);
}