document.addEventListener('DOMContentLoaded', function () {
  const headerIcon = document.getElementById('headerIconImage');
  const headerImageOptionBox = document.getElementById('headerImageOptionBox');
  const editButton = document.getElementById('editProfile');
  const logoutButton = document.getElementById('logout');
  const withdrawButton = document.getElementById('withdraw');
  
  const modal = document.getElementById('commonModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalText = document.getElementById('modalText');
  const modalSubText = document.getElementById('modalSubText');
  const rightBtn = document.querySelector('.modal_button.right_btn');

  // 프로필 아이콘 클릭 시 옵션 토글
  if (headerIcon && headerImageOptionBox) {
    headerIcon.addEventListener('click', (event) => {
      headerImageOptionBox.classList.toggle('hidden');
      event.stopPropagation();
    });
    document.addEventListener('click', (event) => {
      if (!headerImageOptionBox.contains(event.target) && event.target !== headerIcon) {
        headerImageOptionBox.classList.add('hidden');
      }
    });
  }

  // 프로필 수정
  if (editButton) {
    editButton.addEventListener('click', () => {
      window.location.href = '/edit';
    });
  }

  // 로그아웃
  if (logoutButton) {
    logoutButton.addEventListener('click', () => {
      modalTitle.textContent = "로그아웃 하시겠습니까?";
      modalSubText.style.display = "none";
      modal.style.display = 'flex';

      rightBtn.onclick = () => {
        const logoutUrl = logoutButton.dataset.logoutUrl;  // <- 여기서 HTML data 속성 가져옴
        if (logoutUrl) {
          window.location.href = logoutUrl;
        }
      };
    });
  }

  // 회원 탈퇴
  if (withdrawButton) {
    withdrawButton.addEventListener('click', () => {
      modalTitle.textContent = "정말로 회원 탈퇴를 하시겠습니까?";
      modalSubText.textContent = "*돌이킬 수 없습니다";
      modalSubText.style.display = "block";
      modal.style.display = 'flex';

      rightBtn.onclick = () => {
        const deleteUrl = withdrawButton.dataset.deleteUrl;
        const csrfTokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');

        if (deleteUrl && csrfTokenInput) {
          const form = document.createElement('form');
          form.method = 'POST';
          form.action = deleteUrl;

          const csrfInput = document.createElement('input');
          csrfInput.type = 'hidden';
          csrfInput.name = 'csrfmiddlewaretoken';
          csrfInput.value = csrfTokenInput.value;

          form.appendChild(csrfInput);
          document.body.appendChild(form);
          form.submit();
        }
      };
    });
  }
});

// 모달 닫기 함수
function closeModal() {
  const modal = document.getElementById('commonModal');
  if (modal) {
    modal.style.display = 'none';
  }
}
