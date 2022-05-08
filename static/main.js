const cards = document.querySelectorAll('.card');

cards.forEach( card =>{card.addEventListener('mouseenter',()=>{
    card.classList.add("appear")
})

card.addEventListener('mouseleave',()=>{
    card.classList.remove("appear")
})})
