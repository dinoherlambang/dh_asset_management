#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class hr_employee(models.Model):

    _name = "hr.employee"
    _description = "hr.employee"

    _inherit = "hr.employee"


    asset_list_ids = fields.One2many(comodel_name="account.asset.asset",  inverse_name="employee_id",  string="Asset List", )
