function openModal({ title, text, subtext = "", imageUrl }) {
  document.getElementById('modalTitle').textContent = title;
  document.getElementById('modalText').textContent = text;
  document.getElementById('modalImage').src = imageUrl;

  const subTextElement = document.getElementById('modalSubText');
  if (subtext && subtext.trim() !== "") {
    subTextElement.textContent = subtext;
    subTextElement.style.display = "block";
  } else {
    subTextElement.style.display = "none";
  }

  document.getElementById('commonModal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('commonModal').style.display = 'none';
}
