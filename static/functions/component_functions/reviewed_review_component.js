document.addEventListener("DOMContentLoaded", function () {
  const toggleBoxes = document.querySelectorAll(".review_container");
  let currentlyOpen = null;

  toggleBoxes.forEach((toggleBox, index) => {
    const detailBox = document.getElementById(`reviewDetail_${index}`);
    const editBtn = document.getElementById(`reviewed_review_editbtn_${index}`);
    const deleteBtn = document.getElementById(`delete_btn_${index}`);
    const textInput = document.getElementById(`text_input_${index}`);
    const starRating = document.getElementById(`starRating_${index}`);
    const emotionBtns = toggleBox.querySelectorAll(".emotion_btn");

    let isOpen = false;
    let isEditing = false;

    // 펼치기/접기
    toggleBox.addEventListener("click", function (e) {
      if (
        e.target.closest(".icon_btn") ||
        e.target.tagName === "TEXTAREA" ||
        e.target.closest(".emotion_btn")
      ) return;

      if (currentlyOpen && currentlyOpen !== detailBox) {
        currentlyOpen.classList.add("collapsed");
      }

      isOpen = !isOpen;
      detailBox.classList.toggle("collapsed", !isOpen);
      currentlyOpen = isOpen ? detailBox : null;

      if (!isOpen) {
        isEditing = false;
        textInput.setAttribute("disabled", true);
        starRating.classList.add("disabled");
      }
    });

    // 수정 버튼
    editBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      if (!isEditing) {
        isEditing = true;
        textInput.removeAttribute("disabled");
        starRating.classList.remove("disabled");
        textInput.focus();
      } else {
        isEditing = false;
        textInput.setAttribute("disabled", true);
        starRating.classList.add("disabled");

        const updatedText = textInput.value;
        openAlertModal({
        title: '리뷰가 저장되었습니다.',
        imageUrl: '/static/assets/img/modal_star.png',
          });
      }
    });

    deleteBtn.addEventListener("click", function (e) {
      e.stopPropagation();

      openModal({
        title: "운동 리뷰를 리셋하시겠습니까?",
        subtext: "*텍스트, 별점, 반응 개수가 모두 사라집니다",
        imageUrl: "/static/assets/img/modal_star.png",
        onConfirm: function () {
          // ⭐ 1. 텍스트 초기화
          textInput.value = "";

          // ⭐ 2. 별점 초기화
          const stars = starRating.querySelectorAll(".star_per img");
          stars.forEach(img => {
            img.src = "/static/assets/img/star_gray.png";
          });

          // ⭐ 3. 감정 버튼 초기화
          emotionBtns.forEach(btn => {
            btn.classList.remove("selected");

            const countSpan = btn.querySelector(".count");
            const originalCount = parseInt(countSpan.dataset.original) || 0;

            // 숫자 초기화
            countSpan.textContent = originalCount;
            countSpan.style.display = originalCount === 0 ? "none" : "flex";

            // 선택 여부 초기화용 데이터 속성까지 초기화
            btn.dataset.selected = "false";
          });
        }
      });
    });

    // 감정 버튼들
    emotionBtns.forEach(function (btn) {
      const countSpan = btn.querySelector(".count");
      const originalCount = parseInt(countSpan.dataset.original) || 0;
      let isSelected = false;

      if (originalCount === 0) countSpan.style.display = "none";

      btn.addEventListener("click", function () {
        isSelected = !isSelected;

        if (isSelected) {
          countSpan.textContent = originalCount + 1;
          btn.classList.add("selected");
          countSpan.style.display = "flex";
        } else {
          countSpan.textContent = originalCount;
          btn.classList.remove("selected");
          countSpan.style.display = originalCount === 0 ? "none" : "flex";
        }

        countSpan.classList.remove("animate");
        void countSpan.offsetWidth;
        countSpan.classList.add("animate");
      });
    });
  });
});
