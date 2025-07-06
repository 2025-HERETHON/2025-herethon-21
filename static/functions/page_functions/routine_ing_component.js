document.addEventListener("DOMContentLoaded", function () {
  const stepElements = document.querySelectorAll(".step");
  const radius = 30;
  const strokeWidth = 6;

  const stepContentEl = document.getElementById("step_content");
  const stepCategoryEl = document.getElementById("category");

  function injectProgressCircle(circleEl, durationMin) {
    const svgSize = 60;
    const center = svgSize / 2;
    const circumference = 2 * Math.PI * radius;

    circleEl.innerHTML = `
      <svg width="${svgSize}" height="${svgSize}" style="transform: rotate(-90deg); overflow:visible">
        <circle cx="${center}" cy="${center}" r="${radius}" stroke="#e0e0e0" stroke-width="${strokeWidth}" fill="none"/>
        <circle class="progress" cx="${center}" cy="${center}" r="${radius}"
          stroke-width="${strokeWidth}" fill="none"
          stroke-dasharray="${circumference}"
          stroke-dashoffset="${circumference}"
          stroke-linecap="round"
        />
      </svg>
      <div class="time-text">${durationMin}분</div>
    `;

    const timeText = circleEl.querySelector(".time-text");
    Object.assign(timeText.style, {
      position: "absolute",
      top: "50%",
      left: "50%",
      transform: "translate(-50%, -50%)",
      fontWeight: "bold",
      fontSize: "14px",
      lineHeight: "1",
      whiteSpace: "nowrap",
      textAlign: "center",
    });

    circleEl.style.position = "relative";
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

    const imageEL = document.getElementById("routine_image");
    imageEL.src = images[index];

    stepContentEl.textContent = routineData[index].content;
    stepCategoryEl.textContent = routineData[index].category;

    injectProgressCircle(circleEl, durationMin);

    const progressCircle = circleEl.querySelector(".progress");
    const timeText = circleEl.querySelector(".time-text");
    const circumference = 2 * Math.PI * radius;

    let elapsed = 0;
    const timer = setInterval(() => {
      elapsed++;
      const ratio = elapsed / durationSec;
      const offset = circumference * (1 - ratio);
      progressCircle.style.strokeDashoffset = offset;
      timeText.textContent = `${Math.ceil((durationSec - elapsed) / 60)}min`;

      if (elapsed >= durationSec) {
        clearInterval(timer);
        timeText.textContent = "완료!";
        timeText.style.fontSize = "14px";
        runTimer(index + 1);
      }
    }, 1000);
  }

  runTimer(0);
});
