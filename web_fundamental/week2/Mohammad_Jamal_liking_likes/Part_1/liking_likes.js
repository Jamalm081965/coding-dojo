var count = 0
var likebutton = document.querySelector(".like-nav");
console.log(likebutton);

function increaselikes() {
    count++;
    likebutton.innerText = count +  " Like(s)";
    console.log(count);
}