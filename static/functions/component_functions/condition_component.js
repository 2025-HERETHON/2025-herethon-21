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
      alert("저장되었습니다.");
      content.disabled = true;
      content.placeholder = "연필 버튼을 눌러 글을 작성하세요!";
      isEditing = false;
      for (let i = 0; i < conditions.length; i++) {
        conditions[i].classList.add("disabled");
      }
    }
  });

  resetBtn.addEventListener("click", function () {
  openModal({
    title: '컨디션 리뷰를 리셋하시겠습니까?',
    text: '작성한 일기와 감정 선택이 모두 사라집니다.',
    subtext: '*텍스트, 반응이 모두 초기화됩니다.',
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

});
