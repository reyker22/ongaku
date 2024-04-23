let do_review = document.querySelector('.do-review');
let form = document.querySelector('.create-review');

do_review.onclick = function(){
    form.removeAttribute('hidden');
    do_review.setAttribute('hidden', 'hidden');
}