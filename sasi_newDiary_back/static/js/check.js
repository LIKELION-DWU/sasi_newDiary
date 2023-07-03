// 수정 버튼 누르면 index페이지로 넘어가기
let button = document.getElementById("miniBox");

function btnClick() {
  window.location.href = "./index.html";
}

button.addEventListener("click", btnClick);

// 댓글 수 반영
document.getElementById("chat_num").innerText = 2;

// 책 버튼 클릭하면 다이어리 작성 페이지로 넘어가기
let write_button = document.getElementById("btn");

function write_btnClick() {
  window.location.href = "./diary_write.html";
}

write_button.addEventListener("click", write_btnClick);
