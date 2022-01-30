const DONATE = `<div id="donate">
    <form action="https://www.paypal.com/donate" method="post" target="_top">
    <input type="hidden" name="hosted_button_id" value="XPRR34ATBTYPG" />
    <input type="image" src="https://pics.paypal.com/00/s/OTMyZjhiZGEtMTMxNi00ZDQxLWI5ZmUtYWFjY2M1MTdhM2Nm/file.PNG" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
    </form>
    </div>`;

document.addEventListener("DOMContentLoaded", () => {
    // let left_menu = document.querySelectorAll('nav[class="wy-nav-side"]')[0];
    var left_menu = $('nav[class="wy-nav-side"]');
    left_menu.append(DONATE);
});
