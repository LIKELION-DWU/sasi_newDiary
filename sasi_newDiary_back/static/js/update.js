// 작성 당시 날짜가 보이게
let date = document.getElementById("date");


// 이전에 작성 글이 뜨게..

// 수정 버튼 누르면?
let updateBtn = document.getElementById("updateBtn");
var saveContent = function () {
  // 내용이 바뀌어서 저장되어야..
  // 일단 메인페이지로 이동하게 해놓음ㅠㅠ
  window.location.href = "../main.html";
};
updateBtn.addEventListener("click", saveContent);

// 삭제 버튼 누르면
let deleteBtn = document.getElementById("trashCan");
var deleteContent = function () {
  // 해당 박스 삭제..
  // 일단 메인페이지로 이동하게 해놓음ㅠㅠ
  window.location.href = "../main.html";
};
deleteBtn.addEventListener("click", deleteContent);
