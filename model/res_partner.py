#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class res_partner(models.Model):

    _name = "res.partner"
    _description = "res.partner"

    _inherit = "res.partner"
    note = fields.Text( string="Note", )


    warranty_ids = fields.One2many(comodel_name="asset_management.warranty",  inverse_name="suplier_id",  string="Warranty", )
    asset_list_id = fields.Many2one(comodel_name="account.asset.asset",  string="Asset List", )
