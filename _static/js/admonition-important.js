document.addEventListener("DOMContentLoaded", () => {

    let label = document.createElement('label')
    label.classList.add('admonition-title')
    label.textContent = 'Important'

    let list = document.querySelector('h1 + ul')
    list.classList.add('important')
    list.classList.add('admonition')
    list.prepend(label)

});
