document.addEventListener("DOMContentLoaded", function () {
const stepElements = document.querySelectorAll(".step");

const durations = [3, 5, 3, 5, 4]; 

function injectProgressCircle(circleEl, durationMin) {
  const svgSize = 60;
  const radius = 28;
  const circumference = 2 * Math.PI * radius;

  circleEl.innerHTML = `
    <svg width="${svgSize}" height="${svgSize}" style="transform: rotate(-90deg);">
      <circle cx="30" cy="30" r="${radius}" stroke="#e0e0e0" stroke-width="4" fill="none"/>
      <circle class="progress" cx="30" cy="30" r="${radius}" stroke="#4caf50"
        stroke-width="4" fill="none"
        stroke-dasharray="${circumference}"
        stroke-dashoffset="${circumference}"
        stroke-linecap="round"
      />
    </svg>
    <div class="time-text">${durationMin}분</div>
  `;

  circleEl.style.position = "relative";
  const timeText = circleEl.querySelector(".time-text");
  timeText.style.position = "absolute";
  timeText.style.top = "50%";
  timeText.style.left = "50%";
  timeText.style.transform = "translate(-50%, -50%)";
  timeText.style.fontWeight = "bold";
  timeText.style.fontSize = "14px";
}

function runTimer(index) {
  if (index >= stepElements.length) {
    alert("운동이 모두 완료되었습니다!");
    return;
  }

  const step = stepElements[index];
  const circleEl = step.querySelector(".circle");
  const durationMin = durations[index];
  const durationSec = durationMin * 60;

  injectProgressCircle(circleEl, durationMin);

  const progressCircle = circleEl.querySelector(".progress");
  const timeText = circleEl.querySelector(".time-text");
  const circumference = 2 * Math.PI * 28;

  let elapsed = 0;
  const timer = setInterval(() => {
    elapsed++;
    const ratio = elapsed / durationSec;
    const offset = circumference * (1 - ratio);
    progressCircle.style.strokeDashoffset = offset;
    timeText.textContent = `${Math.ceil((durationSec - elapsed) / 60)}분`;

    if (elapsed >= durationSec) {
      clearInterval(timer);
      runTimer(index + 1);
    }
  }, 1000);
}

runTimer(0);

})
