#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class warranty(models.Model):

    _name = "asset_management.warranty"
    _description = "asset_management.warranty"
    name = fields.Char( required=True, string="Name", )
    contract_ref = fields.Text( string="Contract Ref", )
    support_exp_date = fields.Date( string="Support Exp Date", )
    note = fields.Text( string="Note", ) 

    suplier_id = fields.Many2one(comodel_name="res.partner",  string="Suplier", )
