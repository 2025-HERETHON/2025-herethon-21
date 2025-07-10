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
      openAlertModal({
        title: "날짜를 다시 확인해주세요!",
        content: "종료일은 시작일보다 빠를 수 없습니다.",
        imageUrl: "/static/assets/img/modal_star.png",
        onConfirm: function () {
        }
      });
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

  const editButtons = document.querySelectorAll(".edit_btn");
  let currentlyEditingRow = null;

  editButtons.forEach(button => {
    button.addEventListener("click", function () {
      const row = button.closest(".period_row");
      const dateSpan = row.querySelector("span:nth-child(1)");
      const durationSpan = row.querySelector("span:nth-child(2)");
      const cycleSpan = row.querySelector("span:nth-child(3)");

      if (row.classList.contains("editing")) {
        openModal({
          title: "수정 내용을 저장하시겠습니까?",
          subtext: "*수정한 정보는 즉시 반영됩니다.",
          imageUrl: "/static/assets/img/modal_star.png",
          onConfirm: function () {
            const startInput = row.querySelector(".period_start_input");
            const endInput = row.querySelector(".period_end_input");

            const newStart = startInput.value;
            const newEnd = endInput.value;

            const newStartDate = new Date(newStart);
            const newEndDate = new Date(newEnd);

            if (newEndDate < newStartDate) {
              openAlertModal({
                title: "날짜를 다시 확인해주세요!",
                content: "종료일은 시작일보다 빠를 수 없습니다.",
                imageUrl: "/static/assets/img/modal_star.png"
              });
              return;
            }
            const duration = Math.floor((newEndDate - newStartDate) / (1000 * 60 * 60 * 24)) + 1;

            const prevRow = row.previousElementSibling?.classList.contains("period_row") ? row.previousElementSibling : null;
            let cycle = "-";
            if (prevRow) {
              const prevDateText = prevRow.querySelector("span:nth-child(1)").textContent;
              const prevEndStr = prevDateText.split(" - ")[1].replaceAll(".", "-").trim();
              const prevEndDate = new Date(prevEndStr);
              cycle = Math.floor((newStartDate - prevEndDate) / (1000 * 60 * 60 * 24));
            }

            function formatDot(dateStr) {
              const [y, m, d] = dateStr.split("-");
              return `${y}.${m}.${d}`;
            }

            dateSpan.textContent = `${formatDot(newStart)} - ${formatDot(newEnd)}`;
            durationSpan.textContent = `${duration}일`;
            cycleSpan.textContent = cycle !== "-" ? `${cycle}일` : "-";

            row.classList.remove("editing");
            currentlyEditingRow = null;
          }
        });
        return;
      }

      if (currentlyEditingRow && currentlyEditingRow !== row) return;

      const [startRaw, endRaw] = dateSpan.textContent.trim().split(" - ");
      const start = startRaw.replaceAll(".", "-").trim();
      const end = endRaw.replaceAll(".", "-").trim();

      dateSpan.innerHTML = `
        <input type="date" value="${start}" class="date_input period_date_input period_start_input" data-type="start">
        <span>-</span>
        <input type="date" value="${end}" class="date_input period_date_input period_end_input" data-type="end">
      `;

      const startInput = row.querySelector(".period_start_input");
      const endInput = row.querySelector(".period_end_input");

      function updateDuration() {
        if (!startInput.value || !endInput.value) {
          durationSpan.textContent = "-";
          return;
        }
        const startDate = new Date(startInput.value);
        const endDate = new Date(endInput.value);
        const diffDays = Math.floor((endDate - startDate) / (1000 * 60 * 60 * 24)) + 1;
        durationSpan.textContent = diffDays > 0 ? `${diffDays}` : "-";
      }

      startInput.addEventListener("change", updateDuration);
      endInput.addEventListener("change", updateDuration);

      row.classList.add("editing");
      currentlyEditingRow = row;
    });
  });

  dateInputs.forEach(input => {
    if (input.value) input.classList.add("has-value");
  });
});