let regBtn = document.getElementById("registerBtn");

var goLogin = function () {
  window.location.href = "./login.html";
};

// 회원가입 했으니까 로그인 창으로 이동
// 회원가입 데이터 어케 넘김?
regBtn.addEventListener("click", goLogin);
