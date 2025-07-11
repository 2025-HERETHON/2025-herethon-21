document.addEventListener("DOMContentLoaded", function () {
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");
  const loginBtn = document.getElementById("login_submitbtn");
  const signupBtn = document.getElementById("to_signup");
  
  signupBtn.addEventListener("click", function () {
    const url = signupBtn.dataset.url;
    window.location.href = url;
    });


  function checkInputs() {
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();
    if (email && password) {
      loginBtn.style.backgroundColor = " #A48BE7";
      loginBtn.style.color = "white";
    } else {
      loginBtn.style.backgroundColor = "white";
      loginBtn.style.color = " #A48BE7";
    }
  }

  emailInput.addEventListener("input", checkInputs);
  passwordInput.addEventListener("input", checkInputs);

  loginBtn.addEventListener("click", function (e) {
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();

  });
});
