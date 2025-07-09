document.addEventListener("DOMContentLoaded", function () {
  const dateInputs = document.querySelectorAll(".datepicker input[type='date']");

  dateInputs.forEach(input => {
    input.addEventListener("change", () => {
      if (input.value) {
        input.classList.add("has-value");
      } else {
        input.classList.remove("has-value");
      }
    });

    if (input.value) {
      input.classList.add("has-value");
    }
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

            const duration = Math.floor((newEndDate - newStartDate) / (1000 * 60 * 60 * 24)) + 1;

            // 이전 행 종료일 가져와서 주기 계산
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

      // **여기서 input 이벤트 추가:**
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

      // 초기 기간 계산
      updateDuration();

      row.classList.add("editing");
      currentlyEditingRow = row;
    });
  });

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
