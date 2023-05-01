const init = async () => {
  const processes = [];
  const processesData = [
    { name: "a", duration: 4, start: 0, priority: 2 },
    { name: "b", duration: 5, start: 3, priority: 4 },
    { name: "c", duration: 8, start: 7, priority: 5 },
    { name: "d", duration: 9, start: 11, priority: 6 },
  ];

  const numTickets = processesData.map(pd => pd.priority).reduce((a, b) => a + b, 0);
  const tickets = Array(numTickets).fill(0).map((_, i) => i);

  for (var process of processesData) {
    const { name, duration, start, priority } = process;

    const newProcess = new LotteryProcess({ name, duration, start }, tickets.splice(0, priority));
    processes.push(newProcess);
  }

  const algorithm = new LotteryAlgorithm(processes);
  algorithm.init();

  let timeoutId = null;

  function animate(algorithm) {
    const currentStatus = algorithm.run();
    showTickets(algorithm);
    if (currentStatus.value !== null) {
      showMessage(currentStatus.value, algorithm)
    }
    if (!currentStatus.done && (currentStatus.value.type === "execution" || currentStatus.value.type === "idle")) {
      addProcessCell(currentStatus.value.payload);
    } else if (currentStatus.done) {
      clearInterval(timeoutId);
      document.getElementById("run-button").textContent = ">>"
    }
  }

  document.getElementById("next-button")
    .addEventListener("click", () => animate(algorithm));

  document.getElementById("run-button")
    .addEventListener("click", () => {
      if (timeoutId === null) {
        timeoutId = setInterval(() => animate(algorithm), 100);
        document.getElementById("run-button").textContent = "||"
      } else {
        clearInterval(timeoutId);
        timeoutId = null;
        document.getElementById("run-button").textContent = ">>"
      }
    });
};


addEventListener("DOMContentLoaded", init)