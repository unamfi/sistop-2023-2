const colors = {
  a: "#2370ee",
  b: "#3b23ee",
  c: "#a123ee",
  d: "#ee23d6",
  e: "#ee2370",
  f: "#ee3c23"
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

class LotteryProcess extends Process {
  #tickets;

  get tickets() { return [...this.#tickets] };

  constructor({ name, duration, start }, tickets) {
    super({ name, duration, start });
    this.#tickets = tickets;
  }

  containsTicket(number) {
    return this.#tickets.some(t => t == number);
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

function lotteryAlgorithm(processes) {
  const executionOrder = [];
  let n = 0;

  while (processes.some(p => p.end == null)) {
    const avaibleProcesses = processes
      .filter(p => p.start <= n)
      .filter(p => p.end == null);

    const avaibleTickets = avaibleProcesses
      .reduce((a, b) => [...a, ...b.tickets], []);

    const randIndex = Math.round((avaibleTickets.length - 1) * Math.random());
    const selectedTicket = avaibleTickets[randIndex];

    const p = avaibleProcesses.filter(p => p.containsTicket(selectedTicket))[0];

    if (p) {
      p.execute(n);
      executionOrder.push(p.name);
    } else {
      executionOrder.push(null);
    }
    n++;
  }

  return { processes, executionOrder };
}

function multilevelAlgorithm(processes) {
  // Se generan todas las colas
  const queues = {};
  const executionOrder = [];
  let n = 0;

  while (processes.some(p => p.end === null)) {
    if (!queues[0]) queues[0] = []

    processes
      .filter(p => p.priority === -1)
      .filter(p => p.start <= n)
      .forEach(p => {
        p.updatePriority();
        queues[0].push(p);
      });

    const minKey = Object.keys(queues)
      .filter(k => {
        return queues[k].length > 0;
      })
      .sort()[0];

    if (minKey !== undefined) {
      const p = queues[minKey][0];

      const prevPriority = p.priority;
      p.updatePriority();
      const newPriority = p.priority;

      let i = 2**minKey;
      do {
        p.execute(n);
        executionOrder.push({
          name: p.name, newPriority, prevPriority
        });
        i--;
        n++;
      } while(p.end === null && i > 0);

      console.log(prevPriority, newPriority);

      queues[prevPriority] = queues[prevPriority].splice(1);

      if (p.end === null) {
        if (!queues[newPriority])
          queues[newPriority] = [];

        queues[newPriority].push(p);
      }
    } else {
      executionOrder.push(null);
      n++;
    }
    // n++;
  }

  return { processes, executionOrder };
}

function generateView(processes, executionOrder) {
  const panel = document.getElementById("process-panel");
  const baseNode = document.createElement("span");

  executionOrder.forEach(p => {
    const node = baseNode.cloneNode()
    node.textContent = p || "_";
    if (p) node.style.backgroundColor = colors[p];
    else node.style.backgroundColor = "white";
    panel.appendChild(node);
  });
}

function generateView2(processes, executionOrder) {
  const panel = document.getElementById("process-panel");
  const baseNode = document.createElement("span");

  executionOrder.forEach((p, i) => {
    const node = baseNode.cloneNode()
    node.innerHTML = `<div><div class="cell">${p?.name || ''}</div><div>${p?.prevPriority.toString() || ''}${p !== null ? '->' : ''}${p?.newPriority.toString() || ''}</div><div>${i}</div></div>`;
    if (p) node.style.backgroundColor = colors[p.name];
    else node.style.backgroundColor = "white";
    panel.appendChild(node);
  });
}

const init = async () => {
  const processes = [];
  const processesData = [
    { name: "a", duration: 4, start: 0, priority: 2 },
    { name: "b", duration: 5, start: 3, priority: 4 },
    { name: "c", duration: 8, start: 7, priority: 5 },
    { name: "d", duration: 9, start: 11, priority: 6 },
  ];

  const numTickets = processesData.map(pd => pd.priority).reduce((a, b) => a + b, 1);
  const tickets = Array(numTickets).fill(0).map((_, i) => i);

  for (var process of processesData) {
    const { name, duration, start, priority } = process;

    const newProcess = new LotteryProcess({ name, duration, start }, tickets.splice(0, priority));
    processes.push(newProcess);
  }

  const result = lotteryAlgorithm(processes);
  generateView(result.processes, result.executionOrder);
};

const init2 = async () => {
  const processes = [];
  const processesData = [
    { name: "a", duration: 3, start: 0 },
    { name: "b", duration: 5, start: 1 },
    { name: "c", duration: 2, start: 3 },
    { name: "d", duration: 5, start: 9 },
    { name: "e", duration: 5, start: 12 },
  ];

  for (var process of processesData) {
    const { name, duration, start } = process;
    const newProcess = new MultilevelProcess({ name, duration, start });
    processes.push(newProcess);
  }

  const result = multilevelAlgorithm(processes);
  generateView2(result.processes, result.executionOrder);
};

addEventListener("DOMContentLoaded", (e) => {
  init2();
})