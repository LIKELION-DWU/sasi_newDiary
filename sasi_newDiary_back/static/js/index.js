// JavaScript를 이용하여 현재 날짜를 받아오기
var today = new Date();

// 날짜 정보 추출
var year = today.getFullYear();
var month = today.getMonth() + 1; // 월은 0부터 시작하므로 1을 더해줌
var day = today.getDate();

document.getElementById("year").innerText = year;
document.getElementById("month").innerText = month;
document.getElementById("day").innerText = day;

// 책 버튼 클릭하면 다이어리 작성 페이지로 넘어가기
let button = document.getElementById("btn");

function btnClick() {
  window.location.href = "./diary_write.html";
}

button.addEventListener("click", btnClick);

// 일기 작성한 박스를 클릭하면 다이어리 작성한 것을 확인할 수 있는 페이지로 넘어가기
let box = document.getElementById("box");

function boxClick() {
  window.location.href = "./diary_check.html";
}

box.addEventListener("click", boxClick);
