document.addEventListener("DOMContentLoaded", function () {
  const editBtn = document.getElementById("editbtn");
  const resetBtn = document.getElementById("resetbtn");
  const textarea = document.getElementById("text_input");

  const stars = document.getElementsByClassName("star_per");
  const filledSrc = "/static/assets/img/star_purple.png";
  const emptySrc = "/static/assets/img/star_gray.png";

  for (let i = 0; i < stars.length; i++) {
    stars[i].addEventListener("click", function () {
      for (let j = 0; j < stars.length; j++) {
        stars[j].querySelector("img").src = emptySrc;
      }
      for (let j = 0; j <= i; j++) {
        stars[j].querySelector("img").src = filledSrc;
      }
    });
  }

  editBtn.addEventListener("click", function () {
    alert("저장되었습니다.");
  });

  resetBtn.addEventListener("click", function () {
    let ans = confirm("작성한 내용을 초기화하시겠습니까?")
    if (ans) {
        textarea.value = "";
        for (let j = 0; j < stars.length; j++) {
        stars[j].querySelector("img").src = emptySrc;
        }
    }
  });
});
