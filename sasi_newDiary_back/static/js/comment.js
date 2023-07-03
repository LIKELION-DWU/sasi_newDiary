const form = document.querySelector("#form");
const commentsContainer = document.querySelector("#comments");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const usernameInput = form.elements.username;
  const commentInput = form.elements.comment;
  addComment(usernameInput.value, commentInput.value);
  usernameInput.value = "";
  commentInput.value = "";
});

const addComment = (username, comment) => {
  const newComment = document.createElement("li");
  const bTag = document.createElement("b");
  bTag.append(username);
  newComment.append(bTag);
  newComment.append(`- ${comment}`);
  commentsContainer.append(newComment);
};

// 댓글 수 반영
document.getElementById("chat_num").innerText = 2;
