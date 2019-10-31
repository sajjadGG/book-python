// const ROMAN_NUMERALS = {
//     1000: "M",
//     900: "CM",
//     500: "D",
//     400: "CD",
//     100: "C",
//     90: "XC",
//     50: "L",
//     40: "XL",
//     10: "X",
//     9: "IX",
//     4: "IV",
//     5: "V",
//     1: "I",
// };
//
// function toRoman(number) {
//     if (number === 0)
//         return "";
//
//     for (let index of Object.keys(ROMAN_NUMERALS).reverse())
//         if (number >= index)
//             return ROMAN_NUMERALS[index] + toRoman(number - index);
// }

const ALPHABET = {
    0: "0",
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z",
};

function toAlpha(number) {
    return ALPHABET[index];
}

document.addEventListener("DOMContentLoaded", () => {

    /* Replace solution links to chapter */
    document.querySelectorAll('a.download').forEach( (a) => {
        let chapter = window.location.pathname.split('/')[1];
        a.innerHTML = a.innerHTML.replace('solution',  chapter);
    });



    let chapters = document.querySelectorAll("nav.wy-nav-side p.caption");
    let menuItems = document.querySelectorAll("nav.wy-nav-side p.caption + ul");

    menuItems.forEach((ul) => {
        if (ul.className === "current")
            ul.style.display = "block";
        else
            ul.style.display = "none";
    });

    chapters.forEach((chapter, i) => {
        //chapter.innerHTML = `${i}. ${chapter.innerHTML}`;

        // let roman = toRoman(i+1);
        // chapter.innerHTML = `${roman}. ${chapter.innerHTML}`;

        let alpha = toAlpha(i);
        chapter.innerHTML = `${alpha}. ${chapter.innerHTML}`;

        chapter.onclick = () => {
            let ul = chapter.nextElementSibling;

            if (ul.style.display !== "block")
                ul.style.display = "block";
            else
                ul.style.display = "none";
        }
    });
});
