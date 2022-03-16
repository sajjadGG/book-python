document.addEventListener("DOMContentLoaded", () => {
    let listings = document.querySelectorAll("pre");

    listings.forEach((listing, i) => {
        listing.contentEditable = true;
        listing.spellcheck = false;
    });
});
