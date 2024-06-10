if (window.jQuery && window.jQuery.fn.sliderPro) {
    initSliderPro();
} else {
    const initSliderProTimer = setInterval(() => {
        if (window.jQuery && window.jQuery.fn.sliderPro) {
            initSliderPro();
            clearInterval(initSliderProTimer);
        }
    }, 100);
}

function initSliderPro() {
    jQuery(document).ready(function ($) {
        $("#slider-pro-24").sliderPro({
            width: 800,
            height: 533,
            imageScaleMode: "none",
            arrows: true,
            buttons: false,
            thumbnailImageSize: "medium",
            thumbnailWidth: 200,
            thumbnailHeight: 133
        });

    });
}

(function (grecaptcha, sitekey, actions) {

    var wpcf7recaptcha = {

        execute: function (action) {
            grecaptcha.execute(
                sitekey,
                { action: action }
            ).then(function (token) {
                var forms = document.getElementsByTagName('form');

                for (var i = 0; i < forms.length; i++) {
                    var fields = forms[i].getElementsByTagName('input');

                    for (var j = 0; j < fields.length; j++) {
                        var field = fields[j];

                        if ('g-recaptcha-response' === field.getAttribute('name')) {
                            field.setAttribute('value', token);
                            break;
                        }
                    }
                }
            });
        },

        executeOnHomepage: function () {
            wpcf7recaptcha.execute(actions['homepage']);
        },

        executeOnContactform: function () {
            wpcf7recaptcha.execute(actions['contactform']);
        },

    };

    grecaptcha.ready(
        wpcf7recaptcha.executeOnHomepage
    );

    document.addEventListener('change',
        wpcf7recaptcha.executeOnContactform, false
    );

    document.addEventListener('wpcf7submit',
        wpcf7recaptcha.executeOnHomepage, false
    );

})(
    grecaptcha,
    '6LfUe3wkAAAAAJwYdl-OKdjf5h0fdMsJlPpvwGX5',
    { "homepage": "homepage", "contactform": "contactform" }
);