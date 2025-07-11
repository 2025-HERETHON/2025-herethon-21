document.addEventListener("DOMContentLoaded", function () {
  const startDateInput = document.getElementById("scrap_start_date");
  const endDateInput = document.getElementById("scrap_end_date");
  const startLine = document.getElementById("scrap_start_line");
  const endLine = document.getElementById("scrap_end_line");
  const startText = document.getElementById("scrap_start_text");
  const endText = document.getElementById("scrap_end_text");
  const box = document.querySelector(".selected_showingbox");
  const searchBtn = document.getElementById("search_button");

  function parseDotDate(dateStr) {
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
      startText.textContent = formatDate(parseDotDate(startVal));
      box.style.display = "block";
      startDateInput.classList.add("has-value");
    } else {
      startLine.classList.add("hidden");
      startDateInput.classList.remove("has-value");
    }

    if (endVal) {
      endLine.classList.remove("hidden");
      endText.textContent = formatDate(parseDotDate(endVal));
      box.style.display = "block";
      endDateInput.classList.add("has-value");
    } else {
      endLine.classList.add("hidden");
      endDateInput.classList.remove("has-value");
    }

    if (startVal && endVal) {
      searchBtn.classList.add("active");
    } else {
      searchBtn.classList.remove("active");
    }
  }

  startDateInput.addEventListener("change", updateDisplay);
  endDateInput.addEventListener("change", updateDisplay);
  updateDisplay();
});
