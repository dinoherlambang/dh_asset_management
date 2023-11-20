#!/usr/bin/python
#-*- coding: utf-8 -*-

STATES = [('draft','Draft'),('open','In-Progress'),('done','Done')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class asset_moves(models.Model):

    _name = "asset_management.asset_moves"
    _description = "asset_management.asset_moves"
    name = fields.Char( required=True, default="New", readonly=True,  string="Name", )
    state = fields.Selection(selection=STATES,  readonly=True, default=STATES[0][0],  string="State", )
    note = fields.Text( string="Note",  readonly=True, states={"draft" : [("readonly",False)]}, )
    photo = fields.Binary( string="Photo",  readonly=True, states={"draft" : [("readonly",False)]}, )


    @api.model
    def create(self, vals):
        if not vals.get("name", False) or vals["name"] == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("asset_management.asset_moves") or "Error Number!!!"
        return super(asset_moves, self).create(vals)

    def action_confirm(self):
        self.state = STATES[1][0]

    def action_done(self):
        self.state = STATES[2][0]

    def action_draft(self):
        self.state = STATES[0][0]

    def unlink(self):
        for me_id in self :
            if me_id.state != STATES[0][0]:
                raise UserError("Cannot delete non draft record!")
        return super(asset_moves, self).unlink()

    assets_list_id = fields.Many2one(comodel_name="account.asset.asset",  string="Assets List",  readonly=True, states={"draft" : [("readonly",False)]}, )
    move_from = fields.Many2one(comodel_name="stock.location",  string="Move From",  readonly=True, states={"draft" : [("readonly",False)]}, )
    move_to = fields.Many2one(comodel_name="stock.location",  string="Move To",  readonly=True, states={"draft" : [("readonly",False)]}, )
    responsible_person = fields.Many2one(comodel_name="hr.employee",  string="Responsible Person",  readonly=True, states={"draft" : [("readonly",False)]}, )
