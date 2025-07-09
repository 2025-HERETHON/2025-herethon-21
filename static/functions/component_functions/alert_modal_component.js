if (typeof window.alertModalCallback === "undefined") {
  window.alertModalCallback = null;
}

function openAlertModal({ title, text, subtext = "", imageUrl, onConfirm = null }) {
  document.getElementById('alertModalTitle').textContent = title;
  document.getElementById('alertModalText').textContent = text;
  document.getElementById('alertModalImage').src = imageUrl;

  const subTextElement = document.getElementById('alertModalSubText');
  if (subtext && subtext.trim() !== "") {
    subTextElement.textContent = subtext;
    subTextElement.style.display = "block";
  } else {
    subTextElement.style.display = "none";
  }

  window.alertModalCallback = onConfirm;
  document.getElementById('alertModal').style.display = 'flex';
}

function closeAlertModal() {
  document.getElementById('alertModal').style.display = 'none';
  window.alertModalCallback = null;
}

document.addEventListener("DOMContentLoaded", function () {
  const confirmBtn = document.getElementById('alertConfirmBtn');
  if (confirmBtn) {
    confirmBtn.addEventListener("click", function () {
      if (typeof window.alertModalCallback === "function") {
        window.alertModalCallback();
      }
      closeAlertModal();
    });
  }
});
