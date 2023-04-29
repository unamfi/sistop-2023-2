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

  constructor({ name, duration, start }, priority) {
    super({ name, duration, start });
    this.#priority = priority;
  }

  execute(n) {
    super.execute(n);
    this.#priority++;
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
  const queues = processes.reduce((a, b) => {
    a[b.priority] = a[b.priority] ? [...a[b.priority], b] : [b]
    return a;
  }, {});
  const executionOrder = [];
  let n = 0;
  let avaibleProcesses = queues;

  while (processes.some(p => p.end === null)) {
    avaibleProcesses = Object.keys(queues).reduce((a, b) => {
      const items = queues[b]
        .filter(p => p.start <= n)
        .filter(p => p.end === null);
      if (items.length > 0) a[b] = items;
      return a;
    }, {});

    const minKey = Object.keys(avaibleProcesses).sort()[0];

    if (minKey !== undefined) {
      const p = avaibleProcesses[minKey][0];
      const prevPriority = p.priority;
      p.execute(n);
      const newPriority = p.priority;
      executionOrder.push(p.name);

      queues[prevPriority] = queues[prevPriority].splice(1);

      if (!queues[newPriority])
        queues[newPriority] = []

      queues[newPriority].push(p);
    } else {
      executionOrder.push(null);
    }
    n++;
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

const init = async () => {
  const processes = [];
  const processesData = [
    { name: "a", duration: 2, start: 0, priority: 2 },
    { name: "b", duration: 8, start: 3, priority: 4 },
    { name: "c", duration: 3, start: 7, priority: 5 },
    { name: "d", duration: 5, start: 11, priority: 6 },
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
    { name: "a", duration: 4, start: 0, priority: 2 },
    { name: "b", duration: 8, start: 3, priority: 4 },
    { name: "c", duration: 3, start: 7, priority: 5 },
    { name: "d", duration: 5, start: 11, priority: 6 },
  ];

  for (var process of processesData) {
    const { name, duration, start, priority } = process;
    const newProcess = new MultilevelProcess({ name, duration, start }, 0);
    processes.push(newProcess);
  }

  const result = multilevel(processes);
  generateView(result.processes, result.executionOrder);
};

addEventListener("DOMContentLoaded", (e) => {
  init2();
})