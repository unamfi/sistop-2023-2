const colors = {
  a:"#2370ee",
  b:"#3b23ee",
  c:"#a123ee",
  d:"#ee23d6",
  e:"#ee2370",
  f:"#ee3c23"
}

class Process {
  #name;
  #duration;
  #start;
  #end;
  #missingTime;

  get name() {return this.#name}
  get duration() {return this.#duration}
  get start() {return this.#start}
  get end() {return this.#end}

  constructor({name, duration, start}) {
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
      console.log(this);
      throw Error(`This process cannot be executed (${this.#name}).`);
    }
    
    if (this.#missingTime == 0)
      this.#end = num;
  }
}

class LotteryProcess extends Process {
  #tickets;

  get tickets() {return [...this.#tickets]};

  constructor({name, duration, start}, tickets) {
    super({name, duration, start});
    this.#tickets = tickets;
  }

  containsTicket(number) {
    return this.#tickets.some(t => t == number);
  }
}

function algorithm(processes) {
  const executionOrder = [];
  let n = 0;

  while(processes.some(p => p.end == null)) {
    const avaibleProcesses = processes
      .filter(p => p.start <= n)
      .filter(p => p.end == null);

    const avaibleTickets = avaibleProcesses
      .reduce((a,b) => [...a, ...b.tickets], []);

    const randIndex = Math.round((avaibleTickets.length - 1) * Math.random());
    const selectedTicket = avaibleTickets[randIndex];

    const p = avaibleProcesses.filter(p => p.containsTicket(selectedTicket))[0];

    if (p) {
      console.log(p.name);
      p.execute(n);
      executionOrder.push(p.name);
    }
    n++;
  }

  return {processes, executionOrder};
}

function generateHexString(str) {
  return str.codePointAt(str.length-1).toString(16).split("").reverse().join("");
}

function generateView(processes, executionOrder) {
  const panel = document.getElementById("process-panel");
  const baseNode = document.createElement("span");

  executionOrder.forEach(p => {
    const node = baseNode.cloneNode()
    node.textContent = p;
    node.style.backgroundColor=colors[p];
    console.log(generateHexString(p));
    panel.appendChild(node);
  });
}

const init = async () => {
  const processes = [];
  const processesData = [
    { name: "a", duration: 10, start: 0, priority: 2 },
    { name: "b", duration: 8, start: 3, priority: 4 },
    { name: "c", duration: 3, start: 7, priority: 5 },
    { name: "d", duration: 5, start: 11, priority: 6 },
  ];

  const numTickets = processesData.map(pd => pd.priority).reduce((a, b) => a + b, 0);
  const tickets = Array(numTickets).fill(0).map((_, i) => i);

  for (var process of processesData) {
    const { name, duration, start, priority } = process;

    const newProcess = new LotteryProcess({ name, duration, start }, tickets.splice(0, priority));
    processes.push(newProcess);
  }

  const result = algorithm(processes);
  generateView(result.processes, result.executionOrder);
};

addEventListener("DOMContentLoaded", (e) => {
  init();
})