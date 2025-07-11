const calendarTitle = document.getElementById("calendar_title");
const calendarDays = document.getElementById("calendar_days");
const prevMonthBtn = document.getElementById("prev_month");
const nextMonthBtn = document.getElementById("next_month");

const monthNames = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

let today = new Date();
let currentYear = today.getFullYear();
let currentMonth = today.getMonth();

function renderCalendar(year, month, exerciseReviewList) {
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
    if (year === today.getFullYear() && month === today.getMonth() && day === today.getDate()) {
      dayCell.classList.add("today");
    }

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

  // ⭐ 운동 리뷰가 있는 날짜에 별 아이콘 추가
  if (exerciseReviewList.length > 0) {
    const calendarCells = document.querySelectorAll(".calendar_day_positioned");

    const exerciseDates = new Set(exerciseReviewList.map((dateStr) => Number(dateStr.split("-")[2])));

    calendarCells.forEach((cell) => {
      const targetDate = Number(cell.textContent);

      if (exerciseDates.has(targetDate)) {
        const iconWrapper = cell.querySelector(".calendar_icon_wrapper");
        if (!iconWrapper) {
          iconWrapper = document.createElement("div");
          iconWrapper.className = "calendar_icon_wrapper";
          cell.appendChild(iconWrapper);
        }

        const existingStar = iconWrapper.querySelector(".review_star_icon");
        if (!existingStar) {
          const img = document.createElement("img");
          img.src = "/static/assets/img/star_calendar_icon.png";
          img.alt = "review star";
          img.className = "review_star_icon";
          iconWrapper.appendChild(img);
        }
      }
    });
  }
}

function callExerciseReviewCalendar(exerciseReviewList) {
  const today = new Date();
  const currentYear = today.getFullYear();
  const currentMonth = today.getMonth();

  renderCalendar(currentYear, currentMonth, exerciseReviewList);

  prevMonthBtn.addEventListener("click", function () {
    currentMonth--;
    if (currentMonth < 0) {
      currentMonth = 11;
      currentYear--;
    }
    renderCalendar(currentYear, currentMonth, exerciseReviewList);
  });

  nextMonthBtn.addEventListener("click", function () {
    currentMonth++;
    if (currentMonth > 11) {
      currentMonth = 0;
      currentYear++;
    }
    renderCalendar(currentYear, currentMonth, exerciseReviewList);
  });
}
