document.addEventListener("DOMContentLoaded", function () {
  const emailInput = document.getElementById("email");
  const submitBtn = document.getElementById("friend_submitbtn");

  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  function checkInputs() {
    const email = emailInput.value.trim();

    if (email.length === 0) {
      emailInput.style.border = "2px solid white";
    } else if (!isValidEmail(email)) {
      emailInput.style.border = "2px solid rgb(240, 102, 125)";
    } else {
      emailInput.style.border = "2px solid rgb(131, 218, 129)";
    }

    if (isValidEmail(email)) {
      submitBtn.style.backgroundColor = "rgb(174, 129, 218)";
      submitBtn.style.color = "white";
      submitBtn.disabled = false;
    } else {
      submitBtn.style.backgroundColor = "white";
      submitBtn.style.color = "#A48BE7";
      submitBtn.disabled = true;
    }
  }

  emailInput.addEventListener("input", checkInputs);

  submitBtn.addEventListener("click", function () {
    const email = emailInput.value.trim();

    if (isValidEmail(email)) {
      window.location.href = "/friendsconfirm";
    }
  });

  // 초기 로드시 상태 반영
  checkInputs();
});
