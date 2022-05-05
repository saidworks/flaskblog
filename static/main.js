const card = document.querySelector('.card');

card.addEventListener('mouseenter',()=>{
    card.classList.add("appear")
})

card.addEventListener('mouseleave',()=>{
    card.classList.remove("appear")
})