let elSaveBtn = document.getElementById("saveBtn");
let gallBtn = document.getElementById("galleryBtn");

// 저장 버튼 누르면 메인 페이지로 이동.. 이동 시 글 추가 되어야 함
var goSave = function () {
  window.location.href = "../main.html";
};

var goAdd = function () {
  // 여기에 이미지 버튼 누르면 이미지 추가하게 기능 구현
};

elSaveBtn.addEventListener("click", goSave);

gallBtn.addEventListener("click", goAdd);
