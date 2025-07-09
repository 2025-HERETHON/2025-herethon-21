document.addEventListener("DOMContentLoaded", function () {
  const startDateInput = document.getElementById("period_start_date");
  const endDateInput = document.getElementById("period_end_date");
  const startLine = document.getElementById("period_start_line");
  const endLine = document.getElementById("period_end_line");
  const startText = document.getElementById("period_start_text");
  const endText = document.getElementById("period_end_text");
  const box = document.getElementsByClassName("selected_showingbox")[0];
  const searchBtn = document.getElementById("add_button");

  function isValidDate(dateStr) {
    const regex = /^\d{4}-\d{2}-\d{2}$/;
    if (!regex.test(dateStr)) return false;

    const date = new Date(dateStr);
    return !isNaN(date.getTime());
  }

  function updateButtonState() {
    const start = startInput.value.trim();
    const end = endInput.value.trim();

    if (isValidDate(start) && isValidDate(end)) {
      searchBtn.classList.add('active');
  function formatDate(isoDate) {
    const [year, month, day] = isoDate.split("-");
    return `${year}년 ${parseInt(month)}월 ${parseInt(day)}일`;
  }

  function updateDisplay() {
    const startVal = startDateInput.value;
    const endVal = endDateInput.value;

    if (startVal) {
      //startText.textContent = formatDate(startVal);  
      startLine.classList.remove("hidden");
      box.style.display = "block";
      startDateInput.classList.add("has-value");  
    } else {
      startLine.classList.add("hidden");
      startDateInput.classList.remove("has-value");  
    }

    if (endVal) {
      //endText.textContent = formatDate(endVal);  
      endLine.classList.remove("hidden");
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

  startInput.addEventListener('input', updateButtonState);
  endInput.addEventListener('input', updateButtonState);

  // ✅ 삭제 버튼 이벤트 연결
  const deleteButtons = document.querySelectorAll(".delete_btn");
  deleteButtons.forEach(button => {
    button.addEventListener("click", function () {
      openModal({
        title: "월경 내역을 삭제하시겠습니까?",
        subtext: "*삭제한 정보는 복구할 수 없습니다",
        imageUrl: "/static/assets/img/modal_star.png"
      });
    });
  });
  startDateInput.addEventListener("change", updateDisplay);
  endDateInput.addEventListener("change", updateDisplay);
  updateDisplay();
});
