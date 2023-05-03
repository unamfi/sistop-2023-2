function init() {
  const processes = [];
  const processesData = [
    { name: "a", duration: 3, start: 0 },
    { name: "b", duration: 5, start: 1 },
    { name: "c", duration: 2, start: 3 },
    { name: "d", duration: 5, start: 9 },
    { name: "e", duration: 5, start: 12 },
    { name: "f", duration: 15, start: 17 },
    { name: "g", duration: 25, start: 18 },
    { name: "h", duration: 5, start: 25 },
  ];

  for (var process of processesData) {
    const { name, duration, start } = process;
    const newProcess = new MultilevelProcess({ name, duration, start });
    processes.push(newProcess);
  }

  const algorithm = new MultilevelAlgorithm(processes);
  algorithm.init();

  let timeoutId = null;

  function animate(algorithm) {
    const currentStatus = algorithm.run();
    showQueues(algorithm);
    if (currentStatus.value !== null)
      showMessage(currentStatus.value);
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