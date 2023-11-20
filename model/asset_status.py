#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class asset_status(models.Model):

    _name = "asset_management.asset_status"
    _description = "asset_management.asset_status"
    name = fields.Char( required=True, string="Name", )
    note = fields.Text( string="Note", )


