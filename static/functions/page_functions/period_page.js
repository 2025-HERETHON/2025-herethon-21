document.addEventListener("DOMContentLoaded", function () {
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
      // 숨기기
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
      // 숨기기
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

  function setupDeleteButtons() {
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
  }
  setupDeleteButtons();

  addButton.addEventListener("click", function () {
    const startValRaw = startDateInput.value;
    const endValRaw = endDateInput.value;

    if (!startValRaw || !endValRaw) return;

    const startVal = cleanDateString(startValRaw);
    const endVal = cleanDateString(endValRaw);

    const startDate = new Date(startVal);
    const endDate = new Date(endVal);

    if (endDate < startDate) {
      alert("종료일이 시작일보다 빠를 수 없습니다.");
      return;
    }

    const duration = Math.floor((endDate - startDate) / (1000 * 60 * 60 * 24)) + 1;

    let cycle = "-";
    const lastRow = periodTable.querySelector(".period_row:last-child");
    if (lastRow) {
      const lastPeriodText = lastRow.querySelector("span")?.textContent || "";
      const [lastStart, lastEnd] = lastPeriodText.split(" - ").map(s => cleanDateString(s));
      if (lastEnd) {
        const lastEndDate = new Date(lastEnd);
        cycle = Math.floor((startDate - lastEndDate) / (1000 * 60 * 60 * 24));
      }
    }

    const newRow = document.createElement("div");
    newRow.className = "period_row";

    newRow.innerHTML = `
      <span>${startValRaw} - ${endValRaw}</span>
      <span>${duration}</span>
      <span>${cycle === "-" ? "-" : cycle}</span>
      <span class="icon_cell">
        <button class="icon_btn edit_btn">
          <img src="/static/assets/img/rewrite.png" alt="수정" />
        </button>
        <button class="icon_btn delete_btn">
          <img src="/static/assets/img/trashcan.png" alt="삭제" />
        </button>
      </span>
    `;

    periodTable.appendChild(newRow);

    startDateInput.value = "";
    endDateInput.value = "";
    updateDisplay();

    setupDeleteButtons();
  });
});
