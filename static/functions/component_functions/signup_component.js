document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("email");
    const pwInput = document.getElementById("password");
    const pwCheckInput = document.getElementById("repassword");
    const submitBtn = document.getElementById("signup_submitbtn");

    function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
    }

    function isValidPassword(pw) {
    const pwRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+\[\]{};':"\\|,.<>\/?]).{8,16}$/;
    return pwRegex.test(pw);
    }

    function checkInputs() {
    const email = emailInput.value.trim();
    const pw = pwInput.value;
    const pwConfirm = pwCheckInput.value;

    if (email.length === 0) {
        emailInput.style.border = "2px solid white";
    } else if (!isValidEmail(email)) {
        emailInput.style.border = "2px solid rgb(240, 102, 125)";
    } else {
        emailInput.style.border = "2px solid rgb(131, 218, 129)";
    }

    if (pw.length === 0) {
        pwInput.style.border = "2px solid white";
    } else if (!isValidPassword(pw)) {
        pwInput.style.border = "2px solid rgb(240, 102, 125)";
    } else {
        pwInput.style.border = "2px solid rgb(131, 218, 129)";
    }

    if (pwConfirm.length === 0) {
        pwCheckInput.style.border = "2px solid white";
    } else if (pwConfirm !== pw) {
        pwCheckInput.style.border = "2px solid rgb(240, 102, 125)";
    } else {
        pwCheckInput.style.border = "2px solid rgb(131, 218, 129)";
    }

    if (isValidEmail(email) && isValidPassword(pw) && pw === pwConfirm) {
        submitBtn.style.backgroundColor = "rgb(174, 129, 218)";
        submitBtn.style.color="white";
        submitBtn.disabled = false;
    } else {
        submitBtn.style.backgroundColor = "white";
        submitBtn.disabled = true;
    }
    }

    emailInput.addEventListener("input", checkInputs);
    pwInput.addEventListener("input", checkInputs);
    pwCheckInput.addEventListener("input", checkInputs);

    submitBtn.addEventListener("click", function (e) {
    e.preventDefault();

    const email = emailInput.value.trim();
    const pw = pwInput.value;
    const pwConfirm = pwCheckInput.value;

    if (isValidEmail(email) && isValidPassword(pw) && pw === pwConfirm) {
        window.location.href = "/onboarding_2";
    } else {
        alert("입력값을 다시 확인해주세요.");
    }
    });

})