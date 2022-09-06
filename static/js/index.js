const shows = document.querySelector('ul')

shows.addEventListener('click', (event) => {
    // event.target.style.backgroundColor = 'green';    CSAK EGYIRANYU
    // event.currentTarget.classList.toggle('green-style')  MIND
    event.target.classList.toggle('green-style')
} )