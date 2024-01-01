// let btn=document.getElementById("btn")
// btn.addEventListener('click',()=>{
    function test(){
    let data=fetch("/login");
    if(data=="go further"){
        console.log("hello")
    }
    else{
        console.log("bye")
    }
    }
    
// })