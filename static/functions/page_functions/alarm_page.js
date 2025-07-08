document.addEventListener("DOMContentLoaded", function () {
    window.respond = function(user, accepted) {
        const bubble = document.getElementById(`bubble${user}`);
        bubble.innerHTML = `
            <div class="timestamp">방금</div>
            <div class="message_text">
            ${user}의 친구 요청을 ${accepted ? '수락' : '거절'}했습니다
            </div>
        `;
    }
});
