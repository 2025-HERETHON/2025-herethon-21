document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('toggleSwitch');

  toggle.addEventListener('change', function () {
    if (toggle.checked) {
    window.location.href = "/cyclepage";
  } else {
    window.location.href = "/restpage";
  }
  });
}); 