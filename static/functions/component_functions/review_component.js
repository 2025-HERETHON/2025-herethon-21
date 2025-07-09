document.addEventListener("DOMContentLoaded", function () {
  const editBtn = document.getElementById("edit_btn");
  const resetBtn = document.getElementById("review_resetbtn"); // ✅ id 수정
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
  openAlertModal({
    title: '리뷰가 저장되었습니다.',
    imageUrl: '/static/assets/img/modal_star.png',
      });
    });


  resetBtn.addEventListener("click", function () {
    openModal({
      title: '운동 리뷰를 리셋하시겠습니까?',    
      subtext: '작성된 리뷰내용이 모두 초기화됩니다.',
      imageUrl: '/static/assets/img/modal_star.png',
      onConfirm: function () {
        textarea.value = "";
        for (let j = 0; j < stars.length; j++) {
          stars[j].querySelector("img").src = emptySrc;
        }
      }
    });
  });
});
