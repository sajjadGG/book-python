const PREFIX = {
    0: "1.",
    1: "2.",
    2: "3.",
    3: "4.",
    4: "5.",
    5: "6.",
    6: "7.",
    7: "8.",
    8: "9.",
    9: "10.",
    10: "11.",
    11: "12.",
    12: "13.",
    13: "14.",
    14: "15.",
    15: "",
};


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
        chapter.innerHTML = `${PREFIX[i]} ${chapter.innerHTML}`;
        chapter.onclick = () => {
            let ul = chapter.nextElementSibling;
            if (ul.style.display !== "block")
                ul.style.display = "block";
            else
                ul.style.display = "none";
        }
    });
});
