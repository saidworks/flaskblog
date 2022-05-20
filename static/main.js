const cards = document.querySelectorAll('.card');

cards.forEach( card =>{card.addEventListener('mouseenter',()=>{
    card.classList.add("appear")
})

card.addEventListener('mouseleave',()=>{
    card.classList.remove("appear")
})})


//for the navigation menu
const toggle = document.getElementById('toggle');
const nav = document.getElementById('nav');


toggle.addEventListener('click', ()=> nav.classList.toggle('active'));