document.addEventListener("DOMContentLoaded", () => {
    /* Left menu - auto-expand current chapter  */
    let menuItems = document.querySelectorAll("nav.wy-nav-side p.caption + ul");
    menuItems.forEach((ul) => {
        if (ul.className === "current")
            ul.style.display = "block";
        else
            ul.style.display = "none";
    });

    /* Left menu - allow to expand other chapters */
    let chapters = document.querySelectorAll("nav.wy-nav-side p.caption");
    chapters.forEach((chapter, i) => {
        chapter.onclick = () => {
            let ul = chapter.nextElementSibling;
            if (ul.style.display !== "block")
                ul.style.display = "block";
            else
                ul.style.display = "none";
        }
    });
});
