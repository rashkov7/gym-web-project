const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
})

let navButtonContainer = document.getElementById('navigation')
let btns = navButtonContainer.getElementsByClassName('navbar-btn')

for (let i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function () {
            let current = document.getElementsByClassName("active");

            if (current.length > 0) {
                current[0].className = current[0].className.replace("active", '')
            }

            this.className += " active"
        }
    )
}
