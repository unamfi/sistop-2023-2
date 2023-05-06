function init() {
  // Lista de objetos LotteryProcess
  const processes = [];
  
  // Lista de datos recolectados de los inputs
  const processesData = [];

  processesName.forEach(name => {
      const start = parseInt(document.querySelector(`#${name}_start`).value);
      const duration = parseInt(document.querySelector(`#${name}_duration`).value);

      processesData.push({name, duration, start})
  });

  for (var process of processesData) {
    const { name, duration, start } = process;
    const newProcess = new MultilevelProcess({ name, duration, start });
    processes.push(newProcess);
  }

  const algorithm = new MultilevelAlgorithm(processes);
  algorithm.init();

  let timeoutId = null;

  function showStatistics() {
    const {processes} = algorithm;
    processes.forEach(p => {
      const cells = document.querySelectorAll(`#metrics-${p.name} td`);
      const {T, E, P} = p.metrics;
      cells[0].textContent = p.duration;
      cells[1].textContent = p.start;
      cells[2].textContent = p.end;
      cells[3].textContent = T;
      cells[4].textContent = E;
      cells[5].textContent = Number.parseFloat(P).toFixed(2);
    });
    
    // Se suman las métricas
    const sum = processes
      .reduce((prev, p) => {
        const { T, E, P } = p.metrics;
        return {
          T: T + prev.T,
          E: E + prev.E,
          P: P + prev.P,
        }
      }, { T: 0, E: 0, P: 0 });
      
    const cells = document.querySelectorAll(`#metrics-avg td`);
    cells[3].textContent = Number.parseFloat(sum.T / processes.length).toFixed(2);
    cells[4].textContent = Number.parseFloat(sum.E / processes.length).toFixed(2);
    cells[5].textContent = Number.parseFloat(sum.P / processes.length).toFixed(2);
  }

  function animate(algorithm) {
    const currentStatus = algorithm.run();
    showQueues(algorithm);
    if (currentStatus.value !== null)
      showMessage(currentStatus.value);
    if (!currentStatus.done && (currentStatus.value.type === "execution" || currentStatus.value.type === "idle")) {
      addProcessCell(currentStatus.value.payload);
    } else if (currentStatus.done) {
      if (timeoutId !== null)
        clearInterval(timeoutId);
      showStatistics();
      document.getElementById("run-button").textContent = "►"
    }
  }

  document.getElementById("next-button")
  .addEventListener("click", () => {
    animate(algorithm);
  });

  document.getElementById("reload-button")
    .addEventListener('click', () => {
      location.reload();
  });

  document.getElementById("run-button")
  .addEventListener("click", () => {
    if (timeoutId === null) {
      timeoutId = setInterval(() => animate(algorithm), 10);
      document.getElementById("run-button").textContent = "||"
    } else {
      clearInterval(timeoutId);
      timeoutId = null;
      document.getElementById("run-button").textContent = "►"
    }
  });
   
};

addEventListener("DOMContentLoaded", init)
