document.addEventListener("DOMContentLoaded", function () {
  const toggleBox = document.getElementById("reviewToggleBox");
  const detailBox = document.getElementById("reviewDetail");
  const editBtn = document.getElementById("reviewed_review_editbtn");
  const textInput = document.getElementById("text_input");
  const starRating = document.getElementById("starRating");
  const emotionBtns = document.querySelectorAll(".emotion_btn");

  let isOpen = false;
  let isEditing = false;

  // 클릭으로 열고 닫기
  toggleBox.addEventListener("click", function (e) {
    if (
      e.target.closest('.icon_btn') || 
      e.target.tagName === 'TEXTAREA' || 
      e.target.closest('.emotion_btn')
    ) return;

    isOpen = !isOpen;
    detailBox.classList.toggle("collapsed", !isOpen);

    if (!isOpen) {
      // 닫을 때 수정모드 종료
      isEditing = false;
      textInput.setAttribute("disabled", true);
      starRating.classList.add("disabled");
    }
  });

  // 연필 아이콘 클릭 시 수정 or 저장
  editBtn.addEventListener("click", function (e) {
    e.stopPropagation();

    if (!isEditing) {
      // 수정 시작
      isEditing = true;
      textInput.removeAttribute("disabled");
      starRating.classList.remove("disabled");
      textInput.focus();
    } else {
      // 저장
      isEditing = false;
      textInput.setAttribute("disabled", true);
      starRating.classList.add("disabled");

      const updatedText = textInput.value;
      console.log("저장된 텍스트:", updatedText); // 필요시 서버에 보낼 수 있음

      alert("저장되었습니다.");
    }
  });

  // 감정 버튼
  emotionBtns.forEach(function (btn) {
    const countSpan = btn.querySelector(".count");
    let currentCount = parseInt(countSpan.textContent) || 0;
    if (currentCount === 0) countSpan.style.display = "none";

    btn.addEventListener("click", function () {
      if (btn.classList.contains("selected")) {
        currentCount -= 1;
        btn.classList.remove("selected");
      } else {
        currentCount += 1;
        btn.classList.add("selected");
      }

      countSpan.textContent = currentCount;
      countSpan.style.display = currentCount === 0 ? "none" : "flex";
      countSpan.classList.remove("animate");
      void countSpan.offsetWidth;
      countSpan.classList.add("animate");
    });
  });
});
