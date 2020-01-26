
# Copyright 2018 Rémy Taymans <remytaymans@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo.http import request

from odoo.addons.website_portal_v10.controllers.main import WebsiteAccount


class EaterWebsiteAccount(WebsiteAccount):

    def _prepare_portal_layout_values(self):
        values = super(EaterWebsiteAccount,
                       self)._prepare_portal_layout_values()
        partner = request.env.user.partner_id.commercial_partner_id
        values.update({
            'eaters': partner.child_eater_ids,
        })
        return values
