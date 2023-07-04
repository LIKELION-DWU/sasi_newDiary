let signupBtn = document.getElementById("signup");
let seaechBtn = document.getElementById("search");

// 로그인하기 버튼
let loginBtn = document.getElementById("loginBtn");

var goSignUp = function () {
  window.location.href = "./signup.html";
};

var goMain = function () {
  window.location.href = "../main.html";
};

// 회원가입 창으로 이동
signupBtn.addEventListener("click", goSignUp);

// 로그인 했으니까 메인페이지로 이동 (기능 구현 해야 함)
loginBtn.addEventListener("click", goMain);
