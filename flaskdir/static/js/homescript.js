let sec = document.querySelector("section")

let elem = sec.firstElementChild.firstElementChild
setInterval(()=>{
  if(elem.style.transform=="translateX(0px)"){
    elem.style.transform = "translateX(80%)"
  }
  else{
    elem.style.transform = "translateX(0px)"
  }
},2000)
