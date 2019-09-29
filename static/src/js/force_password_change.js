odoo.define('website_force_password_change.force_password_change', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var session = require('web.session');
    var rpc = require('web.rpc');

    require('web.dom_ready');

    function forcePasswordChange () {
        var diffPage = window.location.pathname.indexOf("/change/password") < 0;
        var userId = session.user_id;

        if (!session.is_website_user && diffPage) {
            rpc.query({
                'model': "res.users",
                'method': "search_read",
                'args': [[["id", "=", userId]], ["force_password_change"]],
            }).then(function (user) {
                var forcePassword = user[0].force_password_change;
                if (forcePassword) {
                    window.location.href = "/change/password";
                }
            });
        }
    }

    forcePasswordChange();
});
