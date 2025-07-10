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

  const deleteButtons = document.querySelectorAll(".delete_btn");
deleteButtons.forEach(button => {
  button.addEventListener("click", function () {
    const scrapItem = button.closest(".perroutine"); // 삭제할 루틴 요소 저장

    openModal({
      title: "스크랩을 삭제하시겠습니까?",
      subtext: "*삭제한 정보는 복구할 수 없습니다",
      imageUrl: "/static/assets/img/modal_star.png",
      onConfirm: function () {
        scrapItem.remove(); // 예 누르면 삭제되도록
      }
    });
  });
});


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

    // 검색 후 날짜 박스 텍스트 숨기기
    startLine.classList.add("hidden");
    endLine.classList.add("hidden");
  });
});
