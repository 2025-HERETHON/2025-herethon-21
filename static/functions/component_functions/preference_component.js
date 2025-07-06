document.addEventListener("DOMContentLoaded", function () {
    const circles = document.querySelectorAll(".circle");
    const selectedText = document.getElementById("selected-text"); 
    const msg = document.getElementById("default_msg");
    const selectedBox = document.querySelector(".selected_showingbox");
    let selected = [];

    for (let i = 0; i < circles.length; i++) {
        circles[i].addEventListener("click", function () {
        msg.style.display = "none";
        });
    }

    circles.forEach(circle => {
    circle.addEventListener("click", () => {
        const isSelected = circle.classList.contains("selected");

        if (isSelected) {
        circle.classList.remove("selected");
        selected = selected.filter(c => c !== circle);
        } else {
        if (selected.length < 3) {
            circle.classList.add("selected");
            selected.push(circle);
        } else {
            alert("최대 3개까지만 선택할 수 있습니다.");
            return;
        }
        }
        if (selected.length > 0) {
        selectedBox.style.display = "block";
        const names = selected.map(c => c.textContent.trim()).join(", ");
        selectedText.textContent = `${names}`;
        } else {
        selectedBox.style.display = "none";
        selectedText.textContent = "";
        }
    });
    });
})