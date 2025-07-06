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
            alert("최대 2개까지만 선택할 수 있습니다.");
            return;
        }
        }
        if (selected.length > 0) {
        selectedBox.style.display = "block";
        const names = selected.map(p => p.textContent.trim()).join(", ");
        selecteddPurpose.textContent = `${names}`;
        } else {
        selectedBox.style.display = "none";
        selecteddPurpose.textContent = "";
        }
    });
    });
})