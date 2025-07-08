document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("email");
    const pwInput = document.getElementById("password");
    const pwCheckInput = document.getElementById("repassword");
    const submitBtn = document.getElementById("signup_submitbtn");

    const emailError = document.getElementById("email_error");
    const pwError = document.getElementById("password_error");
    const repwError = document.getElementById("repassword_error");

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function isValidPassword(pw) {
        const pwRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+\[\]{};':"\\|,.<>\/?]).{8,16}$/;
        return pwRegex.test(pw);
    }

    function resetValidation() {
        [emailInput, pwInput, pwCheckInput].forEach(input => input.classList.remove("input_error"));
        [emailError, pwError, repwError].forEach(span => span.textContent = "");
    }

    function showError(input, errorSpan, message) {
        input.classList.add("input_error");
        errorSpan.textContent = message;
    }

    function validateForm() {
        resetValidation();

        let valid = true;
        const email = emailInput.value.trim();
        const pw = pwInput.value;
        const pwConfirm = pwCheckInput.value;

        if (!isValidEmail(email)) {
            showError(emailInput, emailError, "이메일 형식이 잘못되었습니다.");
            valid = false;
        }

        if (!isValidPassword(pw)) {
            showError(pwInput, pwError, "비밀번호 형식을 확인해주세요.");
            valid = false;
        }

        if (pw !== pwConfirm || pwConfirm === "") {
            showError(pwCheckInput, repwError, "비밀번호가 일치하지 않습니다.");
            valid = false;
        }

        return valid;
    }

    submitBtn.addEventListener("click", function (e) {
        e.preventDefault();

        if (validateForm()) {
            window.location.href = "/onboarding_2";
        }
    });
});
