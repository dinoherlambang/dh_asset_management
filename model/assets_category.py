#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class assets_category(models.Model):

    _name = "account.asset.category"
    _description = "account.asset.category"

    _inherit = "account.asset.category"


