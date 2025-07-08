document.addEventListener("DOMContentLoaded", function () {
    const purposes = document.querySelectorAll(".purpose");
    const selecteddPurpose = document.getElementById("selected_purposes"); 
    const msg = document.getElementById("default_msg");
    const selectedBox = document.querySelector(".selected_showingbox");
    let selected = [];

    for (let i = 0; i < purposes.length; i++) {
        purposes[i].addEventListener("click", function () {
        msg.style.display = "none";
        });
    }

    purposes.forEach(purpose => {
    purpose.addEventListener("click", () => {
        const isSelected = purpose.classList.contains("selected");

        if (isSelected) {
        purpose.classList.remove("selected");
        selected = selected.filter(c => c !== purpose);
        } else {
        if (selected.length < 2) {
        purpose.classList.add("selected");
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
            selecteddPurpose.innerHTML = ""; // 기존 내용 초기화

            selected.forEach(p => {
                const item = document.createElement("span");
                item.className = "selected-item";
                item.textContent = p.textContent.trim();
                selecteddPurpose.appendChild(item);
            });
            } else {
            selectedBox.style.display = "none";
            selecteddPurpose.textContent = "";
            }

    });
    });
})