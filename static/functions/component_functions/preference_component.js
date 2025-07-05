document.addEventListener("DOMContentLoaded", function () {
    const circles = document.querySelectorAll(".circle");
    const selectedText = document.getElementById("selected-text"); 
    let selected = [];

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
        const names = selected.map(c => c.textContent.trim()).join(", ");
        selectedText.textContent = `${names}`;
        } else {
        selectedText.textContent = "";
        }
    });
    });
})