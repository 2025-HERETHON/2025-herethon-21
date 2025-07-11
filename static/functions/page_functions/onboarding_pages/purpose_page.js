document.addEventListener("DOMContentLoaded", function () {
    const purposes = document.querySelectorAll(".purpose");
    const selectedPurposeBox = document.getElementById("selected_purposes"); 
    const msg = document.getElementById("default_msg");
    const selectedBox = document.querySelector(".selected_showingbox");
    let selected = [];

    purposes.forEach(purpose => {
        purpose.addEventListener("click", (event) => {
            event.preventDefault(); // ✅ 체크박스 기본 동작 막기 (원할 경우)
            const targetLabel = event.currentTarget;

            // 선택 메시지 제거
            msg.style.display = "none";

            const isSelected = targetLabel.classList.contains("selected");

            if (isSelected) {
                targetLabel.classList.remove("selected");
                targetLabel.querySelector("input[type=checkbox]").checked = false;
                selected = selected.filter(p => p !== targetLabel);
            } else {
                if (selected.length < 2) {
                    targetLabel.classList.add("selected");
                    targetLabel.querySelector("input[type=checkbox]").checked = true;
                    selected.push(targetLabel);
                } else {
                    selectedBox.classList.add("shake");
                    setTimeout(() => {
                        selectedBox.classList.remove("shake");
                    }, 400);
                    return;
                }
            }

            // 왼쪽에 선택된 목적 보여주기
            if (selected.length > 0) {
                selectedBox.style.display = "block";
                selectedPurposeBox.innerHTML = "";

                selected.forEach(p => {
                    const item = document.createElement("span");
                    item.className = "selected-item";
                    item.textContent = p.textContent.trim();
                    selectedPurposeBox.appendChild(item);
                });
            } else {
                selectedBox.style.display = "none";
                selectedPurposeBox.textContent = "";
            }
        });
    });
});
