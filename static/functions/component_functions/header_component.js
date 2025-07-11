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

  if (editButton) {
    editButton.addEventListener('click', () => {
      window.location.href = '/editpage';
    });
  }

  if (logoutButton) {
    logoutButton.addEventListener('click', () => {
      modalTitle.textContent = "로그아웃 하시겠습니까?";
      modalSubText.style.display = "none";
      modal.style.display = 'flex';

      rightBtn.onclick = () => {
        window.location.href = '/logout/';
      };
    });
  }

  if (withdrawButton) {
    withdrawButton.addEventListener('click', () => {
      modalTitle.textContent = "정말로 회원 탈퇴를 하시겠습니까?";
      modalSubText.textContent = "*돌이킬 수 없습니다";
      modalSubText.style.display = "block";
      modal.style.display = 'flex';

      rightBtn.onclick = () => {
        window.location.href = '/delete_account/';
      };
    });
  }
});

function closeModal() {
  const modal = document.getElementById('commonModal');
  if (modal) {
    modal.style.display = 'none';
  }
}
