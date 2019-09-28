##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

# 1. Standard library imports:
import json

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import http
from odoo.http import request

# 4. Imports from Odoo modules (rarely, and only if necessary):
from odoo.addons.website_change_password.controllers.main import ChangePassword

# 5. Local imports in the relative form:

# 6. Unknown third party imports (One per line sorted and splitted in


class ForcePasswordChange(ChangePassword):

    @http.route(['/force-password-change'], type='json', auth="user", website=True, csrf=False)
    def force_password_change(self, **post):
        """ Check if user has to change password and redirect to change password page """
        current_user = request.env.user
        res = {}
        if current_user.force_password_change:
            res['redirect'] = '/change/password'
        return json.dumps(res)
