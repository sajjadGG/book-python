document.addEventListener("DOMContentLoaded", () => {
    let chapters = document.querySelectorAll("nav.wy-nav-side p.caption")

    chapters.forEach((menuEntry, i) => {
        let number = i + 1
        menuEntry.innerHTML = `${number}. ${menuEntry.innerHTML}`
    });
});
