// function myFunction() {
//     var x = document.getElementById("myLinks");
//     if (x.style.display === "block") {
//       x.style.display = "none";
//     } else {
//       x.style.display = "block";
//     }
//   }


const logo=document.querySelector(".humberger")
const close_btn=document.querySelector(".close_btn")
var  x = document.getElementById("mobile-menubar");

logo.addEventListener("click",()=>{
    x.style.display="block"
})

close_btn.addEventListener("click",()=>{
    x.style.display="none"
})