function show(event) {
  const target = event.target;
  target.classList.add("hidden");
  target.nextElementSibling.classList.remove("hidden");
}

function hide(event) {
  const target = event.target.closest("div");
  target.classList.add("hidden");
  target.previousElementSibling.classList.remove("hidden");
}
