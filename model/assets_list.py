#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class assets_list(models.Model):

    _name = "account.asset.asset"
    _description = "account.asset.asset"

    _inherit = "account.asset.asset"

    serial_number = fields.Text( string="Serial Number", )
    spesification = fields.Html( string="Spesification", )
    barcode = fields.Text( string="Barcode", )
    qrcode = fields.Text( string="Qrcode", )

    image_small = fields.Binary( string="Photo", )

    asset_location_id = fields.Many2one(comodel_name="stock.location",  string="Asset Location", )
    asset_status_id = fields.Many2one(comodel_name="asset_management.asset_status",  string="Asset Status", )
    warranty_id = fields.Many2one(comodel_name="asset_management.warranty",  string="Warranty", )
    employee_id = fields.Many2one(comodel_name="hr.employee",  string="Employee", )
    asset_moves_ids = fields.One2many(comodel_name="asset_management.asset_moves",  inverse_name="assets_list_id",  string="Asset Moves", )
    suplier_info_ids = fields.One2many(comodel_name="res.partner",  inverse_name="asset_list_id",  string="Suplier Info", )




