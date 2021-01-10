/* Assignment - Change numbering to A, B, C, ... */

const ALPHABET = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    14: "P",
    15: "Q",
};

document.addEventListener("DOMContentLoaded", () => {
    let assignments = document.querySelectorAll('#assignments .caption-number')
    i = 0;
    for (let assignment of assignments)
        assignment.innerHTML = `Assignment ${ALPHABET[i++]}.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`;
});
