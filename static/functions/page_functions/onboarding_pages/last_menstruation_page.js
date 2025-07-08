document.addEventListener("DOMContentLoaded", function () {
    const startDateInput = document.getElementById("start_date");
    const endDateInput = document.getElementById("end_date");
    const startLine = document.getElementById("start-line");
    const endLine = document.getElementById("end-line");
    const startText = document.getElementById("start_text");
    const endText = document.getElementById("end_text");
    const box = document.getElementsByClassName("selected_showingbox")[0];

    function formatDate(isoDate) {
    const [year, month, day] = isoDate.split("-");
    return `${year}년 ${parseInt(month)}월 ${parseInt(day)}일`;
    }

    function updateDisplay() {
    const startVal = startDateInput.value;
    const endVal = endDateInput.value;

    // 시작일 처리
    if (startVal) {
        startText.textContent = formatDate(startVal);
        startLine.classList.remove("hidden");
        box.style.display = ("block");
    } else {
        startLine.classList.add("hidden");
    }

    // 종료일 처리
    if (endVal) {
        endText.textContent = formatDate(endVal);
        endLine.classList.remove("hidden");
    } else {
        endLine.classList.add("hidden");
    }
    }

    startDateInput.addEventListener("change", updateDisplay);
    endDateInput.addEventListener("change", updateDisplay);
})