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

class Process {
  #name;
  #duration;
  #start;
  #end;
  #missingTime;

  get name() { return this.#name }
  get duration() { return this.#duration }
  get start() { return this.#start }
  get end() { return this.#end }
  get missing() { return this.#missingTime }

  constructor({ name, duration, start }) {
    this.#name = name;
    this.#duration = duration;
    this.#start = start;
    this.#end = null;
    this.#missingTime = duration;
  }

  execute(num) {
    if (this.#missingTime > 0)
      this.#missingTime--;
    else {
      throw Error(`This process cannot be executed (${this.#name}).`);
    }

    if (this.#missingTime == 0)
      this.#end = num;
  }
}

class MultilevelProcess extends Process {
  #priority;

  get priority() { return this.#priority };

  constructor({ name, duration, start }) {
    super({ name, duration, start });
    this.#priority = -1;
  }

  updatePriority() {
    if (this.end === null)
      this.#priority++;
    else
      this.#priority = null;
  }
}

class LotteryProcess extends Process {
  #tickets;

  get tickets() { return [...this.#tickets] };

  constructor({ name, duration, start }, tickets) {
    super({ name, duration, start });
    this.#tickets = tickets;
  }

  containsTicket(number) {
    return this.#tickets.includes(number);
  }
}

class AbstractProcessPlanningAlgorithm {
  #processes
  #currenTick
  #generator

  get processes() {return this.#processes}
  get currentTick() {return this.#currenTick}
  get generator() {return this.#generator}

  constructor(processes) {
    this.#processes = processes;
  }

  init() {
    this.#currenTick = 0;
    this.#generator = this._exec();
  }

  setNextTick() {
    this.#currenTick++;
  }

  run() {
    return this.generator.next()
  }

  *_exec() {
    throw new Error("Unimplemented method.")
  }
}

class MultilevelAlgorithm extends AbstractProcessPlanningAlgorithm {
  #queues

  get queues() {return this.#queues}

  constructor(processes) {
    super(processes);
  }

  init() {
    super.init();
    this.#queues = {};
  }

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
      if (!this.#queues[0])
        this.#queues[0] = []

      let arrivalProcesses = this.getArrivalProcesses();

      console.log(this.currenTick);
      if (arrivalProcesses.length > 0)
        yield {
          type: "arrival",
          payload: arrivalProcesses
        };

      const q = Object.keys(this.#queues)
        .filter(k => {
          return this.#queues[k].length > 0;
        })
        .sort()[0];

      if (q !== undefined) {
        const p = this.#queues[q][0];

        const prevPriority = p.priority;

        let i = 2 ** q;
        do {
          if (i < 2 ** q) {
            arrivalProcesses = this.getArrivalProcesses();
            if (arrivalProcesses.length > 0)
              yield {
                type: "arrival-but",
                payload: arrivalProcesses
              };
          }

          p.execute(this.currenTick);
          this.setNextTick();
          yield {
            type: "execution",
            payload: p
          };

          i--;

        } while (p.end === null && i > 0);

        p.updatePriority();
        const newPriority = p.priority;

        this.#queues[prevPriority] = this.#queues[prevPriority].splice(1);

        if (p.end === null) {
          if (!this.#queues[newPriority])
            this.#queues[newPriority] = [];

          this.#queues[newPriority].push(p);

          yield {
            type: "priority",
            payload: p
          }
        } else {
          yield {
            type: "remove",
            payload: p
          }
        }

      } else {
        this.setNextTick();
        yield {
          type: "idle",
          payload: null
        };
      }
    }
    return null;
  }
}

class LotteryAlgorithm extends AbstractProcessPlanningAlgorithm {
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

      const newProcesses = this.processes.filter(p => p.start === this.currentTick);
      if (newProcesses.length > 0) {
        newProcesses.forEach(p => this.#avaibleProcesses.push(p));
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
        yield {
          type: "execution",
          payload: p,
          ticket: selectedTicket
        };

        if (p.end !== null) {
          this.#avaibleProcesses = this.#avaibleProcesses.filter(p => p.end === null);
          yield {
            type: "remove",
            payload: p
          }
        }
      } else {
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
    case "":
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