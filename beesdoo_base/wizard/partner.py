# -*- coding: utf-8 -*-
from openerp import models, fields, api

class NewEaterWizard(models.TransientModel):
    """
        A transient model for the creation of a eater related to a worker.
    """
    _name = 'eater.new.wizard'

    def _get_default_partner(self):
        return self.env.context['active_id']

    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    email = fields.Char('Email')

    partner_id = fields.Many2one('res.partner', default=_get_default_partner)

    @api.one
    def create_new_eater(self):
        self.partner_id._new_eater(self.first_name, self.last_name, self.email)
