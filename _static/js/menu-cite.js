let today = new Date()
let year = today.getFullYear()
let date = today.toISOString().split('T')[0]
let url = window.location.href
let revision = $('footer span.commit code').text()

const CITE = `<div id="cite">
    Cite this page:
    <div>
        Harasymczuk, Matt.
        Python: from None to Machine Learning.
        ORCID: https://orcid.org/0000-0002-2961-0617
        ISBN: 978-83-957186-2-5.
        Year: ${year}.
        Retrived: ${date}.
        Revision: ${revision}.
        URL: ${url}
    </div>
    </div>`;


document.addEventListener("DOMContentLoaded", () => {
    // let left_menu = document.querySelectorAll('nav[class="wy-nav-side"]')[0];
    var left_menu = $('nav[class="wy-nav-side"]');
    left_menu.append(CITE);
});
