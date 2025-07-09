document.addEventListener("DOMContentLoaded", function () {
  const conditions = document.getElementsByClassName("condition_per");
  const content = document.getElementById("text_input");
  const todaysCondition = document.getElementById("todays_condition");
  const editBtn = document.getElementById("condition_editbtn");
  const resetBtn = document.getElementById("condition_resetbtn");

  let selectedIndex = -1;
  let isEditing = false;

  content.disabled = true;
  content.placeholder = "연필 버튼을 눌러 글을 작성하세요!";
  for (let i = 0; i < conditions.length; i++) {
    conditions[i].classList.add("disabled");
  }

  function handleConditionClick(i) {
    if (!isEditing) return;

    if (selectedIndex === i) {
      conditions[i].classList.remove("selected");
      todaysCondition.innerHTML = "";
      // 달력 반영은 저장 시 처리하므로 여기선 제거하지 않음
      selectedIndex = -1;
      return;
    }

    for (let j = 0; j < conditions.length; j++) {
      conditions[j].classList.remove("selected");
    }

    conditions[i].classList.add("selected");
    const selectedImg = conditions[i].querySelector("img");
    const newImg = document.createElement("img");
    newImg.src = selectedImg.src;
    newImg.alt = selectedImg.alt;
    newImg.style.animation = "popEffect 0.3s ease";
    newImg.style.width = "30px";

    todaysCondition.innerHTML = "";
    todaysCondition.appendChild(newImg);
    selectedIndex = i;

    // 달력에는 저장 후 반영하므로 여기서는 호출하지 않음
  }


  for (let i = 0; i < conditions.length; i++) {
    conditions[i].addEventListener("click", () => handleConditionClick(i));
  }

  editBtn.addEventListener("click", function () {
    if (!isEditing) {
      content.disabled = false;
      content.placeholder = "오늘의 일기를 남겨주세요!";
      isEditing = true;
      for (let i = 0; i < conditions.length; i++) {
        conditions[i].classList.remove("disabled");
      }
    } else {
      openAlertModal({
        title: '저장되었습니다.',
        text: '리뷰가 성공적으로 저장되었습니다.',
        imageUrl: '/static/assets/img/modal_star.png',
        onConfirm: function () {
          content.disabled = true;
          content.placeholder = "연필 버튼을 눌러 글을 작성하세요!";
          isEditing = false;
          for (let i = 0; i < conditions.length; i++) {
            conditions[i].classList.add("disabled");
          }

          // 저장 시 달력 이모지 반영
          removeEmotionFromCalendar(); // 기존 이모지 제거
          if (selectedIndex !== -1) {
            addEmotionToCalendar();
          }
        }
      });
    }
  });



  resetBtn.addEventListener("click", function () {
    openModal({
      title: '컨디션 리뷰를 리셋하시겠습니까?',
      subtext: '*텍스트, 감정이 모두 초기화됩니다.',
      imageUrl: '/static/assets/img/modal_star.png',
      onConfirm: function () {
        content.value = "";
        todaysCondition.innerHTML = "";
        for (let i = 0; i < conditions.length; i++) {
          conditions[i].classList.remove("selected");
        }
        selectedIndex = -1;
      }
    });
  });

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

      // ⭐ 항상 앞에 추가 (이모지가 왼쪽)
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
