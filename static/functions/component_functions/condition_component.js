document.addEventListener("DOMContentLoaded", function () {
  const conditions = document.getElementsByClassName("condition_per");
  const content = document.getElementById("text_input");
  const todaysCondition = document.getElementById("todays_condition");
  let cnt = 0;

  for (let i = 0; i < conditions.length; i++) {
    conditions[i].addEventListener("click", function () {
      for (let j = 0; j < conditions.length; j++) {
        conditions[j].classList.remove("selected");
      }

      this.classList.add("selected");

      const selectedImg = this.querySelector("img");
      const newImg = document.createElement("img");
      newImg.src = selectedImg.src;
      newImg.alt = selectedImg.alt;
      newImg.style.animation = "popEffect 0.3s ease";
      newImg.style.width = "30px";

      todaysCondition.innerHTML = "";
      todaysCondition.appendChild(newImg);

      cnt++;
    });
  }

  const savebtn = document.getElementById("savebtn");
  if (savebtn) {
    savebtn.addEventListener("click", function () {
      if (content.value.trim() === "") {
        alert("내용을 입력해주세요.");
      } else if (cnt === 0) {
        alert("오늘의 감정을 선택해주세요.");
      } else {
        alert("저장되었습니다.");
      }
    });
  }
});
