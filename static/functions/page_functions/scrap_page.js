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

  // 삭제 버튼 이벤트
  const deleteButtons = document.querySelectorAll(".delete_btn");
  deleteButtons.forEach(button => {
    button.addEventListener("click", function (event) {
      event.stopPropagation(); // 클릭 이벤트 전파 방지
      const scrapItem = button.closest(".perroutine");

      openModal({
        title: "스크랩을 삭제하시겠습니까?",
        subtext: "*삭제한 정보는 복구할 수 없습니다",
        imageUrl: "/static/assets/img/modal_star.png",
        onConfirm: function () {
          scrapItem.remove();
        }
      });
    });
  });

  // 검색 버튼 클릭 이벤트
  searchBtn.addEventListener("click", function () {
    const startVal = parseDotDate(startDateInput.value);
    const endVal = parseDotDate(endDateInput.value);

    if (!startVal || !endVal) return;

    const startDate = new Date(startVal);
    const endDate = new Date(endVal);

    const items = document.querySelectorAll(".perroutine");

    items.forEach(item => {
      const dateText = item.querySelector(".date_")?.textContent.trim();
      if (!dateText) return;

      const cleanDateText = dateText.replace(/\./g, "-").replace(/-$/, "").trim();
      const itemDate = new Date(cleanDateText);

      if (itemDate >= startDate && itemDate <= endDate) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
    });

    startLine.classList.add("hidden");
    endLine.classList.add("hidden");
  });

  // ✅ 루틴 클릭 시 모달 열고 페이지 이동 - 항상 바인딩됨
  const routineWrapper = document.querySelector(".routines");
  routineWrapper.addEventListener("click", function (e) {
    const target = e.target;
    const routineItem = target.closest(".perroutine");

    if (routineItem && !target.closest(".delete_btn")) {
      openModal({
        title: "이 운동을 다시 진행하시겠습니까?",
        subtext: "*루틴을 불러와 운동을 시작합니다",
        imageUrl: "/static/assets/img/modal_star.png",
        onConfirm: function () {
          window.location.href = "/routineingpage";
        }
      });
    }
  });
});
