document.addEventListener('DOMContentLoaded', function () {
  const startInput = document.getElementById('scrap_start_date');
  const endInput = document.getElementById('scrap_end_date');
  const searchBtn = document.getElementById('search_button');

  
  function isValidDate(dateStr) {
    // YYYY-MM-DD 형식 검사
    const regex = /^\d{4}-\d{2}-\d{2}$/;
    if (!regex.test(dateStr)) return false;

    const date = new Date(dateStr);
    return !isNaN(date.getTime());  // 날짜 객체로 변환 가능하면 유효
  }

  function updateButtonState() {
    const start = startInput.value.trim();
    const end = endInput.value.trim();

    if (isValidDate(start) && isValidDate(end)) {
      searchBtn.classList.add('active');
    } else {
      searchBtn.classList.remove('active');
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
});
