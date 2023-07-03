var daysOfWeek = ["일", "월", "화", "수", "목", "금", "토"];
// JavaScript를 이용하여 현재 날짜를 받아오기
var today = new Date();

// 날짜 정보 추출
var year = today.getFullYear();
var month = today.getMonth() + 1; // 월은 0부터 시작하므로 1을 더해줌
var day = today.getDate();
var dayOfWeek = today.getDay();

document.getElementById("year").innerText = year;
document.getElementById("month").innerText = month;
document.getElementById("day").innerText = day;
document.getElementById("day_of_week").innerText = daysOfWeek[dayOfWeek];

let button = document.getElementById("save");

function btnClick() {
  window.location.href = "./index.html";
}

button.addEventListener("click", btnClick);
