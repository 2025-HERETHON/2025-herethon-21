document.addEventListener("DOMContentLoaded", function () {
  const conditions = document.getElementsByClassName("condition_per");
  const content = document.getElementById("text_input");
  const todaysCondition = document.getElementById("todays_condition");
  const editBtn = document.getElementById("condition_editbtn");
  const resetBtn = document.getElementById("condition_resetbtn");
  const selectedRatingInput = document.getElementById("selected_rating");
  const form = document.getElementById("condition_form");

  let selectedIndex = -1;
  let isEditing = false;

  if (selectedRatingInput?.value) {
    selectedIndex = [...conditions].findIndex(
      (span) => span.dataset.rating === selectedRatingInput.value
    );
  }

  if (content) {
    content.disabled = true;
    content.placeholder = "연필 버튼을 눌러 글을 작성하세요!";
  }

  Array.from(conditions).forEach((el) => el.classList.add("disabled"));

  function handleConditionClick(i) {
    if (!isEditing) return;

    Array.from(conditions).forEach((el) => el.classList.remove("selected"));

    conditions[i].classList.add("selected");
    selectedRatingInput.value = conditions[i].dataset.rating;
    selectedIndex = i;

    if (todaysCondition) {
      const selectedImg = conditions[i].querySelector("img");
      const newImg = document.createElement("img");
      newImg.src = selectedImg.src;
      newImg.alt = selectedImg.alt;
      newImg.style.animation = "popEffect 0.3s ease";
      newImg.style.width = "30px";
      todaysCondition.innerHTML = "";
      todaysCondition.appendChild(newImg);
    }
  }

  Array.from(conditions).forEach((el, i) => {
    el.addEventListener("click", () => handleConditionClick(i));
  });

  editBtn?.addEventListener("click", function () {
    if (!isEditing) {
      content.disabled = false;
      content.placeholder = "오늘의 일기를 남겨주세요!";
      isEditing = true;
      Array.from(conditions).forEach((el) => el.classList.remove("disabled"));
    } else {
      if (!selectedRatingInput.value || content.value.trim() === "") {
        openAlertModal({
          title: "감정과 내용을 모두 입력해주세요!",
          imageUrl: "/static/assets/img/modal_star.png",
          onConfirm: () => {},
        });
        return;
      }

      openAlertModal({
        title: "리뷰가 저장되었습니다.",
        imageUrl: "/static/assets/img/modal_star.png",
        onConfirm: function () {
          content.disabled = false;
          removeEmotionFromCalendar();
          if (selectedIndex !== -1) addEmotionToCalendar();
          form.submit();
        },
      });
    }
  });

  resetBtn?.addEventListener("click", function () {
    openModal({
      title: "컨디션 리뷰를 삭제하시겠습니까?",
      subtext: "*텍스트와 감정이 모두 사라집니다.",
      imageUrl: "/static/assets/img/modal_star.png",
      onConfirm: function () {
        const dateText = document
          .querySelector("#current_time_display")
          .textContent.trim();
        const formattedDate = formatDateToYMD(dateText);
        if (formattedDate) {
          window.location.href = `/conditionreviews/delete/${formattedDate}/`;
        } else {
          openAlertModal({
            title: "날짜 형식을 인식할 수 없습니다!",
            imageUrl: "/static/assets/img/modal_star.png",
          });
        }
      },
    });
  });

  function formatDateToYMD(koreanDate) {
    const match = koreanDate.match(/(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일/);
    if (!match) return "";
    const [, year, month, day] = match;
    return `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
  }

  function addEmotionToCalendar() {
    const calendarCells = document.querySelectorAll(".calendar_day_positioned");
    const today = new Date();
    const todayDate = today.getDate();

    calendarCells.forEach((cell) => {
      const cellDay = parseInt(cell.textContent.trim(), 10);
      if (
        cellDay === todayDate &&
        !cell.classList.contains("prev_month") &&
        !cell.classList.contains("next_month")
      ) {
        let iconWrapper = cell.querySelector(".calendar_icon_wrapper");
        if (!iconWrapper) {
          iconWrapper = document.createElement("div");
          iconWrapper.className = "calendar_icon_wrapper";
          cell.appendChild(iconWrapper);
        }

        const existingEmotion = iconWrapper.querySelector(".emotion_icon");
        if (existingEmotion) existingEmotion.remove();

        const img = document.createElement("img");
        img.src = "/static/assets/img/smile_calendar_emozi.png";
        img.alt = "emotion";
        img.className = "emotion_icon";

        iconWrapper.prepend(img);
      }
    });
  }

  function removeEmotionFromCalendar() {
    const calendarCells = document.querySelectorAll(".calendar_day_positioned");
    const today = new Date();
    const todayDate = today.getDate();
    calendarCells.forEach((cell) => {
      const cellDay = parseInt(cell.textContent.trim(), 10);
      if (
        cellDay === todayDate &&
        !cell.classList.contains("prev_month") &&
        !cell.classList.contains("next_month")
      ) {
        const icon = cell.querySelector(".emotion_icon");
        if (icon) icon.remove();
      }
    });
  }
});
