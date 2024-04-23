let checkbox = document.querySelector('.checkbox');
let input_pass = document.querySelector("#password-input");


checkbox.onclick = function(){
    if(checkbox.checked) input_pass.setAttribute("type", "text");
    else input_pass.setAttribute("type", "password");
}