let writeBtn = document.getElementById("writeBtn");

// 글 작성 페이지로 이동!!
var goWrite = function () {
  window.location.href = "../pages/write.html";
};

writeBtn.addEventListener("click", goWrite);
