document.addEventListener("DOMContentLoaded", function () {
  const toggleBoxes = document.querySelectorAll(".review_container");
  let currentlyOpen = null;

  toggleBoxes.forEach((toggleBox, index) => {
    const detailBox = document.getElementById(`reviewDetail_${index}`);
    const editBtn = document.getElementById(`reviewed_review_editbtn_${index}`);
    const deleteBtn = document.getElementById(`delete_btn_${index}`);
    const textInput = document.getElementById(`text_input_${index}`);

    const starRating = document.getElementById(`starRating_${index}`);
    const starImgs = starRating.querySelectorAll(".star_per img");
    const emotionBtns = toggleBox.querySelectorAll(".emotion_btn");

    let isOpen = false;
    let isEditing = false;
    let currentRating = starRating.querySelectorAll("img[src*='star_purple']").length;

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

        openAlertModal({
          title: '리뷰가 저장되었습니다.',
          imageUrl: '/static/assets/img/modal_star.png',
        });
      }
    });

    // 별점 클릭 (이 컴포넌트 안에서만 동작)
   // reviewed_review_component.js 중 별점 부분만 따로 추출
  starImgs.forEach((img, i) => {
    img.addEventListener("click", function (e) {
      e.stopPropagation();  // 다른 toggle 이벤트 방지
      if (starRating.classList.contains("disabled")) return;

      starImgs.forEach((star, j) => {
        star.src = j <= i
          ? "/static/assets/img/star_purple.png"
          : "/static/assets/img/star_gray.png";
      });

      currentRating = i + 1;
    });
  });


    // 삭제 버튼
    deleteBtn.addEventListener("click", function (e) {
      e.stopPropagation();

      openModal({
        title: "운동 리뷰를 리셋하시겠습니까?",
        subtext: "*텍스트, 별점, 반응 개수가 모두 사라집니다",
        imageUrl: "/static/assets/img/modal_star.png",
        onConfirm: function () {
          // 텍스트 초기화
          textInput.value = "";

          // 별점 초기화 (이 컴포넌트에만 적용)
          currentRating = 0;
          starImgs.forEach(img => {
            img.src = "/static/assets/img/star_gray.png";
          });

          // 감정 초기화
          emotionBtns.forEach(btn => {
            btn.classList.remove("selected");

            const countSpan = btn.querySelector(".count");
            const originalCount = parseInt(countSpan.dataset.original) || 0;

            countSpan.textContent = originalCount;
            countSpan.style.display = originalCount === 0 ? "none" : "flex";
            btn.dataset.selected = "false";
          });
        }
      });
    });

    // 감정 버튼
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
