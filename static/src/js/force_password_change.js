odoo.define('website_force_password_change.force_password_change', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var session = require('web.session');
    require('web.dom_ready');

    function forcePasswordChange () {
        var diffPage = window.location.pathname.indexOf('/change/password') < 0;
        if (!session.is_website_user && diffPage) {
            var action = "/force-password-change";
            ajax.jsonRpc(action, "call").then(function (res) {
                var response = JSON.parse(res);
                // Show in modal or update current dom to contain page?
                if (response["redirect"]) {
                    window.location.href = response["redirect"];
                }
            });
        }
    }
    forcePasswordChange();
});
