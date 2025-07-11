document.addEventListener("DOMContentLoaded", function () {
  const dateInputs = document.querySelectorAll(".datepicker input[type='date']");
  const startDateInput = document.getElementById("period_start_date");
  const endDateInput = document.getElementById("period_end_date");
  const startLine = document.getElementById("period_start_line");
  const endLine = document.getElementById("period_end_line");
  const startText = document.getElementById("period_start_text");
  const endText = document.getElementById("period_end_text");
  const box = document.getElementsByClassName("selected_showingbox")[0];
  const addButton = document.getElementById("add_button");
  const periodTable = document.querySelector(".period_table");

  function cleanDateString(dateStr) {
    return dateStr.replace(/\./g, "-").replace(/-$/, "").trim();
  }

  function formatDate(isoDate) {
    const [year, month, day] = isoDate.split("-");
    return `${year}년 ${parseInt(month)}월 ${parseInt(day)}일`;
  }

  function updateDisplay() {
    const startVal = startDateInput.value;
    const endVal = endDateInput.value;

    if (startVal) {
      startLine.classList.remove("hidden");
      startText.textContent = formatDate(cleanDateString(startVal));
      startLine.style.display = "none";
      box.style.display = "none";
      startDateInput.classList.add("has-value");
    } else {
      startLine.classList.add("hidden");
      startDateInput.classList.remove("has-value");
    }

    if (endVal) {
      endLine.classList.remove("hidden");
      endText.textContent = formatDate(cleanDateString(endVal));
      endLine.style.display = "none";
      box.style.display = "none";
      endDateInput.classList.add("has-value");
    } else {
      endLine.classList.add("hidden");
      endDateInput.classList.remove("has-value");
    }

    if (startVal && endVal) {
      addButton.classList.add("active");
    } else {
      addButton.classList.remove("active");
    }
  }

  startDateInput.addEventListener("change", updateDisplay);
  endDateInput.addEventListener("change", updateDisplay);
  updateDisplay();

  dateInputs.forEach((input) => {
    if (input.value) input.classList.add("has-value");
  });
});
