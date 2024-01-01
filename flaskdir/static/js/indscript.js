let btn=document.getElementById("login")

let btn1=document.getElementById("Register")
let loginform=document.querySelector(".login-form-container")
let registerform=document.querySelector(".register-form-container")
console.log(btn,loginform,registerform)
btn.addEventListener("click",()=>{
  loginform.style.zIndex="2";
  registerform.style.zIndex="1";
  loginform.style.opacity="1";
  registerform.style.opacity="0";
})
btn1.addEventListener("click",()=>{
  loginform.style.zIndex="1";
  registerform.style.zIndex="2";
  loginform.style.opacity="0";
  registerform.style.opacity="1";
})