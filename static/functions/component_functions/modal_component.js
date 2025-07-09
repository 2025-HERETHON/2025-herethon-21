let modalConfirmCallback = null; // 콜백 저장 변수

function openModal({ title, subtext = "", imageUrl, onConfirm = null }) {
  document.getElementById('modalTitle').textContent = title;
  document.getElementById('modalImage').src = imageUrl;

  const subTextElement = document.getElementById('modalSubText');
  if (subtext && subtext.trim() !== "") {
    subTextElement.textContent = subtext;
    subTextElement.style.display = "block";
  } else {
    subTextElement.style.display = "none";
  }

  modalConfirmCallback = onConfirm;
  document.getElementById('commonModal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('commonModal').style.display = 'none';
  modalConfirmCallback = null;
}

document.addEventListener("DOMContentLoaded", function () {
  const yesBtn = document.querySelector("#commonModal .right_btn");
  const noBtn = document.querySelector("#commonModal .left_btn");

  yesBtn.addEventListener("click", function () {
    if (typeof modalConfirmCallback === "function") {
      modalConfirmCallback();
    }
    closeModal();
  });

  noBtn.addEventListener("click", closeModal);
});
