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

{
    'name': 'Website Force Password Change',
    'summary': 'Force password change for portal users',
    'version': '12.0.1.1.0',
    'category': 'Website',
    'website': 'https://github.com/savijoki/website_force_password_change',
    'author': 'Aleksi Savijoki',
    'license': 'AGPL-3',
    'depends': [
        'website_change_password',
    ],
    'data': [
        'views/res_users_views.xml',
        'views/assets.xml',
        'views/website_change_password.xml',
    ],
    'demo': [
    ],
    'application': False,
    'installable': True,
}
