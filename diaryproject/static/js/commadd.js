const instaForm = document.querySelector("#instaForm");
const commentsContainer = document.querySelector("#comments");
instaForm.addEventListener("submit", function (e) {
  e.preventDefault();
  const commentInput = instaForm.elements.comment;
  addComment(commentInput.value);
  commentInput.value = "";
});

const addComment = (comment) => {
  const newComment = document.createElement("div");
  //const bTag = document.createElement("b");
  //bTag.append(username);
  //newComment.append(bTag);
  newComment.append(`${comment}`);
  commentsContainer.append(newComment);
};
