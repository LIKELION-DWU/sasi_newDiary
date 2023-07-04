let elbox = document.getElementById("box");

// 쓰기 버튼
let writeBtn = document.getElementById("writeBtn");

// 탭버튼
let listBtn = document.getElementById("listText");
let tileBtn = document.getElementById("tileText");

// 로그아웃 버튼
let logoutBtn = document.getElementById("logoutBtn");

var goUpdate = function () {
  window.location.href = "./pages/update.html";
};
var goWrite = function () {
  window.location.href = "./pages/write.html";
};

var goList = function () {
  window.location.href = "./list.html";
};

var goTile = function () {
  window.location.href = "./main.html";
};

var goLogin = function () {
  window.location.href = "./pages/login.html";
};

elbox.addEventListener("click", goUpdate);

writeBtn.addEventListener("click", goWrite);

listBtn.addEventListener("click", goList);
tileBtn.addEventListener("click", goTile);

// 로그인 창으로 이동
logoutBtn.addEventListener("click", goLogin);
