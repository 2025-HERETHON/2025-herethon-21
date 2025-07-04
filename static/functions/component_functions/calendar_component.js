document.addEventListener("DOMContentLoaded", function () {
  const calendarTitle = document.getElementById("calendar_title");
  const calendarDays = document.getElementById("calendar_days");
  const prevMonthBtn = document.getElementById("prev_month");
  const nextMonthBtn = document.getElementById("next_month");

  const monthNames = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

// 🚫달력 표시 필요 없을 때는 지워도 되는 부분 
const aiPredictedSchedules = [
    { start: "2025-07-05", end: "2025-07-10", type: "trip" },
    { start: "2025-07-12", end: "2025-07-14", type: "birthday" },
    { start: "2025-07-16", end: "2025-07-20", type: "exam" },
    { start: "2025-07-22", end: "2025-07-24", type: "date" }
  ];

  function isDateInRange(dateStr, startStr, endStr) {
  const date = new Date(dateStr);
  const start = new Date(startStr);
  const end = new Date(endStr);
  return date >= start && date <= end;
}

  const highlightedDates = {};
  aiPredictedSchedules.forEach(schedule => {
    highlightedDates[schedule.date] = schedule.type;
  });
  
// 여기까지 지워도 됨


  let today = new Date();
  let currentYear = today.getFullYear();
  let currentMonth = today.getMonth(); 

  function renderCalendar(year, month) {
    calendarTitle.textContent = `${monthNames[month]} ${year}`;

    const firstDayOfMonth = new Date(year, month, 1).getDay(); // 요일: 0 (Sun) ~ 6 (Sat)
    const lastDateOfMonth = new Date(year, month + 1, 0).getDate(); // 말일
    const prevLastDate = new Date(year, month, 0).getDate(); // 이전 달 말일

    calendarDays.innerHTML = "";

    const fragment = document.createDocumentFragment();

    // 앞쪽: 이전 달 날짜로 채우기
    for (let i = firstDayOfMonth - 1; i >= 0; i--) {
      const prevDay = document.createElement("div");
      prevDay.classList.add("calendar_day", "prev_month");
      prevDay.textContent = prevLastDate - i;
      fragment.appendChild(prevDay);
    }

    // 이번 달 날짜 채우기
    for (let day = 1; day <= lastDateOfMonth; day++) {
      const dayCell = document.createElement("div");
      dayCell.classList.add("calendar_day");
      dayCell.textContent = day;

      // 오늘 날짜 표시
      if (
        year === today.getFullYear() &&
        month === today.getMonth() &&
        day === today.getDate()
      ) {
        dayCell.classList.add("today");
      }

      // 🚫달력 표시를 위해 추가한 부분 2 필요 없을 때는 지워도 됨
      const dateStr = `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
      
      aiPredictedSchedules.forEach(schedule => {
        if (isDateInRange(dateStr, schedule.start, schedule.end)) {
            dayCell.classList.add(`highlight_${schedule.type}`);
        }
    });
      // 여기까지 지워도 됨

      fragment.appendChild(dayCell);
    }

    // 뒤쪽: 다음 달 날짜로 필요한 만큼만 채우기 (7의 배수로 맞추기 위해)
    const totalCells = fragment.childNodes.length;
    const remaining = (7 - (totalCells % 7)) % 7;

    for (let i = 1; i <= remaining; i++) {
      const nextDay = document.createElement("div");
      nextDay.classList.add("calendar_day", "next_month");
      nextDay.textContent = i;
      fragment.appendChild(nextDay);
    }
    calendarDays.appendChild(fragment);
  }

  renderCalendar(currentYear, currentMonth);

  prevMonthBtn.addEventListener("click", function () {
    currentMonth--;
    if (currentMonth < 0) {
      currentMonth = 11;
      currentYear--;
    }
    renderCalendar(currentYear, currentMonth);
  });

  nextMonthBtn.addEventListener("click", function () {
    currentMonth++;
    if (currentMonth > 11) {
      currentMonth = 0;
      currentYear++;
    }
    renderCalendar(currentYear, currentMonth);
  });
});
