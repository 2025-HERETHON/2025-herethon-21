document.addEventListener("DOMContentLoaded", function () {
  const startDateInput = document.getElementById("scrap_start_date");
  const endDateInput = document.getElementById("scrap_end_date");
  const startLine = document.getElementById("scrap_start_line");
  const endLine = document.getElementById("scrap_end_line");
  const startText = document.getElementById("scrap_start_text");
  const endText = document.getElementById("scrap_end_text");
  const box = document.getElementsByClassName("selected_showingbox")[0];
  const searchBtn = document.getElementById("search_button");
  
  function isValidDate(dateStr) {
    // YYYY-MM-DD 형식 검사
    const regex = /^\d{4}-\d{2}-\d{2}$/;
    if (!regex.test(dateStr)) return false;

    const date = new Date(dateStr);
    return !isNaN(date.getTime());  // 날짜 객체로 변환 가능하면 유효
  function formatDate(isoDate) {
    const [year, month, day] = isoDate.split("-");
    return `${year}년 ${parseInt(month)}월 ${parseInt(day)}일`;
  }

  function updateDisplay() {
    const startVal = startDateInput.value;
    const endVal = endDateInput.value;

    // 시작일 텍스트 표시 & 클래스 토글
    if (startVal) {
      // startText.textContent = formatDate(startVal);
      startLine.classList.remove("hidden");
      box.style.display = "block";
      startDateInput.classList.add("has-value");  
    } else {
      startLine.classList.add("hidden");
      startDateInput.classList.remove("has-value");  
    }

    if (endVal) {
      // endText.textContent = formatDate(endVal);
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
        title: "스크랩을 삭제하시겠습니까?",
        subtext: "*삭제한 정보는 복구할 수 없습니다",
        imageUrl: "/static/assets/img/modal_star.png"
      });
    });
  });
  startDateInput.addEventListener("change", updateDisplay);
  endDateInput.addEventListener("change", updateDisplay);

  updateDisplay();
});
