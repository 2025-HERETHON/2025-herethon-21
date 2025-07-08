document.addEventListener('DOMContentLoaded', function () {
  const editableName = document.querySelector('.editable_text'); 
  const penIcon2 = document.getElementById('penIcon_2');
  const trashcanIcon2 = document.getElementById('trashcanIcon_2');
  const leftInfoTitle = document.querySelector('.content_left .info_title');

  const textarea = document.getElementById('introTextarea');
  const penIcon = document.getElementById('penIcon');
  const trashcanIcon = document.getElementById('trashcanIcon');

  const tags = document.querySelectorAll('.preference_box .preference_tag');
  const maxSelected = 2;

  const saveButton = document.getElementById('saveButton');

  const editableIcon = document.querySelector(".content_right .icon_image2");
  const imageOptionBox = document.getElementById("imageOptionBox");
  const galleryOption = document.getElementById("galleryOption");
  const imageInput = document.getElementById("profileImageInput");
  const defaultImageOption = document.getElementById("defaultImageOption");

  let currentImageSrc = "/static/assets/img/icon.png";

  function checkModified() {
    const nameModified = editableName && editableName.textContent.trim() !== '나';
    const textModified = textarea && textarea.value.trim() !== '';
    const selectedTags = document.querySelectorAll('.preference_box .preference_tag.active').length > 0;
    const imageModified = currentImageSrc !== "/static/assets/img/icon.png";

    if (nameModified || textModified || selectedTags || imageModified) {
      saveButton.classList.add('active');
      saveButton.disabled = false;
    } else {
      saveButton.classList.remove('active');
      saveButton.disabled = true;
    }
  }

  if (editableName) {
    editableName.addEventListener('input', checkModified);
    editableName.addEventListener('keyup', checkModified);
  }

  if (penIcon2) {
    penIcon2.addEventListener('click', () => {
      editableName.focus();
    });
  }
  if (trashcanIcon2) {
    trashcanIcon2.addEventListener('click', () => {
      editableName.textContent = '나';
      checkModified();
    });
  }

  if (textarea) {
    textarea.addEventListener('input', () => {
      penIcon.src = textarea.value.trim() !== "" 
        ? "/static/assets/img/pen_after.png"
        : "/static/assets/img/pen_before.png";

      const infoText = document.querySelector('.content_right .info_text');
      if (infoText) {
        infoText.textContent = textarea.value || "안녕? 나는 너만의 운동 루틴 추천 AI 피피야";
      }
      checkModified();
    });
  }

  if (trashcanIcon) {
    trashcanIcon.addEventListener('click', () => {
      if (textarea) {
        textarea.value = "";
      }
      penIcon.src = "/static/assets/img/pen_before.png";
      const infoText = document.querySelector('.content_right .info_text');
      if (infoText) {
        infoText.textContent = "안녕? 나는 너만의 운동 루틴 추천 AI 피피야";
      }
      checkModified();
    });
  }

  tags.forEach(tag => {
    tag.addEventListener('click', () => {
      const activeTags = document.querySelectorAll('.preference_box .preference_tag.active');

      if (tag.classList.contains('active')) {
        tag.classList.remove('active');
      } else {
        if (activeTags.length < maxSelected) {
          tag.classList.add('active');
        } else {
          alert(`최대 ${maxSelected}개까지만 선택할 수 있습니다.`);
          return;
        }
      }

      checkModified();
    });
  });

  saveButton.addEventListener('click', () => {

    if (editableName && leftInfoTitle) {
      leftInfoTitle.textContent = editableName.textContent.trim() || '나';
    }

    const leftText = document.querySelector('.content_left .info_text');
    if (leftText && textarea) {
      leftText.textContent = textarea.value.trim() || "안녕? 나는 너만의 운동 루틴 추천 AI 피피야";
    }

    const leftTags = document.querySelector('.content_left .info_box .tags');
    if (leftTags) {
      leftTags.innerHTML = '';
      document.querySelectorAll('.preference_box .preference_tag.active').forEach(t => {
        const span = document.createElement('span');
        span.className = 'preference_tag';
        span.textContent = t.textContent.trim();
        leftTags.appendChild(span);
      });
    }

    if (editableIcon) {
      const leftImage = document.querySelector('.content_left .icon_image2');
      if (leftImage) {
        leftImage.src = currentImageSrc;
      }
    }

    saveButton.classList.remove('active');
    saveButton.disabled = true;

    penIcon.src = "/static/assets/img/pen_before.png";
  });

  if (editableIcon && imageOptionBox) {
    editableIcon.addEventListener("click", (event) => {
      const isHidden = imageOptionBox.classList.contains("hidden");

      if (isHidden) {
        editableIcon.src = "/static/assets/img/edit_image.png"; 
        imageOptionBox.classList.remove("hidden");
      } else {
        editableIcon.src = currentImageSrc;
        imageOptionBox.classList.add("hidden");
      }
      event.stopPropagation();
    });

    document.addEventListener("click", (event) => {
      if (!imageOptionBox.contains(event.target) && event.target !== editableIcon) {
        imageOptionBox.classList.add("hidden");
        editableIcon.src = currentImageSrc;
      }
    });
  }

  if (galleryOption && imageInput && editableIcon) {
    galleryOption.addEventListener("click", () => {
      imageInput.click();
    });

    imageInput.addEventListener("change", (e) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (event) {
          currentImageSrc = event.target.result;
          editableIcon.src = currentImageSrc;
          imageOptionBox.classList.add("hidden");
          checkModified();
        };
        reader.readAsDataURL(file);
      }
    });
  }

  if (defaultImageOption && editableIcon && imageOptionBox) {
    defaultImageOption.addEventListener("click", () => {
      currentImageSrc = "/static/assets/img/icon.png";
      editableIcon.src = currentImageSrc;
      imageOptionBox.classList.add("hidden");
      checkModified();
    });
  }

  checkModified();
});
