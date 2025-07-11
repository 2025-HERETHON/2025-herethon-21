 document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
      const welcomeText = document.getElementById("welcome_text");
      const loginText = document.getElementById("login_text");

      welcomeText.style.transition = "opacity 1s";
      welcomeText.style.opacity = "0";

      setTimeout(() => {
        welcomeText.style.display = "none";
        loginText.style.opacity = "1";
      }, 1000);
    }, 1000);
  });