const DONATE = `<div id="donate">
    <form action="https://www.paypal.com/donate" method="post" target="_top">
    <input type="hidden" name="hosted_button_id" value="XPRR34ATBTYPG" />
    <input type="image" src="https://www.paypalobjects.com/en_US/PL/i/btn/btn_donateCC_LG.gif" name="submit" title="Donate with PayPal button" alt="Donate with PayPal button" />
    </form>
    </div>`;


document.addEventListener("DOMContentLoaded", () => {
    // let left_menu = document.querySelectorAll('nav[class="wy-nav-side"]')[0];
    let left_menu = $('nav[class="wy-nav-side"]');
    left_menu.append(DONATE);
});
