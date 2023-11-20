#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class asset_location(models.Model):

    _name = "stock.location"
    _description = "stock.location"

    _inherit = "stock.location"
    note = fields.Text( string="Note", )
    address = fields.Text( string="Address", )
    geolocation = fields.Text( string="Geolocation", )


    assets_list_ids = fields.One2many(comodel_name="account.asset.asset",  inverse_name="asset_location_id",  string="Assets List", )
