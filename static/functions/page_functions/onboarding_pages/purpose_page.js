document.addEventListener("DOMContentLoaded", function () {
  const purposes = document.querySelectorAll(".purpose");
  const selectedPurpose = document.getElementById("selected_purposes");
  const msg = document.getElementById("default_msg");
  const selectedBox = document.querySelector(".selected_showingbox");
  let selected = [];

  purposes.forEach((purpose) => {
    purpose.addEventListener("click", (e) => {
      e.preventDefault(); // 라벨 기본 클릭 막기

      const checkbox = purpose.querySelector("input[type='checkbox']");
      const isSelected = purpose.classList.contains("selected");

      msg.style.display = "none";

      if (isSelected) {
        purpose.classList.remove("selected");
        checkbox.checked = false;
        selected = selected.filter((c) => c !== purpose);
      } else {
        if (selected.length < 2) {
          purpose.classList.add("selected");
          checkbox.checked = true;
          selected.push(purpose);
        } else {
          selectedBox.classList.add("shake");
          setTimeout(() => {
            selectedBox.classList.remove("shake");
          }, 400);
          return;
        }
      }

      if (selected.length > 0) {
        selectedBox.style.display = "block";
        selectedPurpose.innerHTML = "";
        selected.forEach((p) => {
          const item = document.createElement("span");
          item.className = "selected-item";
          item.textContent = p.textContent.trim();
          selectedPurpose.appendChild(item);
        });
      } else {
        selectedBox.style.display = "none";
        selectedPurpose.textContent = "";
        msg.style.display = "block";
      }
    });
  });
});
