document.addEventListener('DOMContentLoaded', function () {
  const editableName = document.querySelector('.editable_text'); 
  const nicknameInput = document.getElementById('nickname_input');
  const penIcon2 = document.getElementById('penIcon_2');
  const trashcanIcon2 = document.getElementById('trashcanIcon_2');

  const textarea = document.getElementById('introTextarea');
  const bioInput = document.getElementById('bio_input');
  const penIcon = document.getElementById('penIcon');
  const trashcanIcon = document.getElementById('trashcanIcon');

  const tags = document.querySelectorAll('.preference_box .preference_tag');
  const saveButton = document.getElementById('saveButton');

  const imageInput = document.getElementById('profileImageInput');
  const currentImage = document.querySelector('#profileImage');
  const defaultImage = "/static/assets/img/icon.png";

  let currentImageSrc = currentImage ? currentImage.src : defaultImage;

  function checkModified() {
    const nameChanged = editableName && editableName.textContent.trim() !== nicknameInput.value.trim();
    const bioChanged = textarea && textarea.value.trim() !== bioInput.value.trim();
    const goalChanged = Array.from(document.querySelectorAll('.goal_checkbox')).some(cb => cb.checked);
    const imageChanged = currentImage && currentImage.src !== defaultImage;

    if (nameChanged || bioChanged || goalChanged || imageChanged) {
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
    penIcon2.addEventListener('click', () => editableName.focus());
  }

  if (trashcanIcon2) {
    trashcanIcon2.addEventListener('click', () => {
      editableName.textContent = '나';
      checkModified();
    });
  }

  if (textarea) {
    textarea.addEventListener('input', () => {
      if (textarea.value.length > 30) {
        textarea.value = textarea.value.slice(0, 30);
      }
      checkModified();
    });
  }

  if (trashcanIcon) {
    trashcanIcon.addEventListener('click', () => {
      textarea.value = "";
      checkModified();
    });
  }

  tags.forEach(tag => {
    tag.addEventListener('click', () => {
      tag.classList.toggle('active');
      const checkbox = tag.querySelector('input[type="checkbox"]');
      if (checkbox) {
        checkbox.checked = tag.classList.contains('active');
      }
      checkModified();
    });
  });

  const galleryOption = document.getElementById('galleryOption');
  const defaultImageOption = document.getElementById('defaultImageOption');
  const imageOptionBox = document.getElementById('imageOptionBox');
  const editableIcon = document.querySelector('.icon_image2');

  if (editableIcon && imageOptionBox) {
    editableIcon.addEventListener('click', e => {
      imageOptionBox.classList.toggle('hidden');
      e.stopPropagation();
    });

    document.addEventListener('click', e => {
      if (!imageOptionBox.contains(e.target) && e.target !== editableIcon) {
        imageOptionBox.classList.add('hidden');
      }
    });
  }

  if (galleryOption && imageInput) {
    galleryOption.addEventListener('click', () => {
      imageInput.click();
    });

    imageInput.addEventListener('change', e => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (event) {
          currentImageSrc = event.target.result;
          if (editableIcon) editableIcon.src = currentImageSrc;
          checkModified();
        };
        reader.readAsDataURL(file);
      }
    });
  }

  if (defaultImageOption) {
    defaultImageOption.addEventListener('click', () => {
      currentImageSrc = defaultImage;
      if (editableIcon) editableIcon.src = defaultImage;
      checkModified();
    });
  }

  const form = document.getElementById('editProfileForm');
  if (form) {
    form.addEventListener('submit', function () {
      if (editableName) nicknameInput.value = editableName.textContent.trim();
      if (textarea) bioInput.value = textarea.value.trim();

      console.log("\ud83d\ude80 \uc81c출\ub428");
      console.log("\ub2c9\ub124임:", nicknameInput.value);
      console.log("\uc18c개:", bioInput.value);

      document.querySelectorAll('.goal_checkbox').forEach(cb => {
        console.log("\uc6b4동 \ubaa9적 checkbox:", cb.name, cb.value, "=>", cb.checked);
      });
    });
  }

  checkModified();
});