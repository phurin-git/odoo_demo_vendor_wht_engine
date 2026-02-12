from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    x_wht_rate = fields.Float(default=3.0)
    x_wht_amount = fields.Monetary(compute="_compute_wht", store=True)
    x_approval_state = fields.Selection([
        ("draft", "Draft"),
        ("waiting", "Waiting Approval"),
        ("approved", "Approved"),
    ], default="draft")
    x_is_approved = fields.Boolean(compute="_compute_is_approved", store=True)

    @api.depends("amount_total", "x_wht_rate")
    def _compute_wht(self):
        for rec in self:
            if rec.move_type == "in_invoice":
                rec.x_wht_amount = rec.amount_total * rec.x_wht_rate / 100
            else:
                rec.x_wht_amount = 0.0

    @api.depends("x_approval_state")
    def _compute_is_approved(self):
        for rec in self:
            rec.x_is_approved = rec.x_approval_state == "approved"

    def action_send_for_approval(self):
        for rec in self:
            if rec.amount_total >= 50000:
                rec.x_approval_state = "waiting"
            else:
                rec.x_approval_state = "approved"

    def action_approve(self):
        if not self.env.user.has_group('demo_vendor_wht_engine.group_vendor_wht_manager'):
            raise UserError(_("Only WHT Manager can approve."))
        self.x_approval_state = "approved"

    def action_post(self):
        for rec in self:
            if rec.move_type == "in_invoice":
                if rec.amount_total >= 50000 and not rec.x_is_approved:
                    raise UserError(_("Vendor Bill must be approved before posting."))
        return super().action_post()

    def button_draft(self):
        for rec in self:
            rec.x_approval_state = "draft"
        return super().button_draft()

    def button_cancel(self):
        for rec in self:
            rec.x_approval_state = "draft"
        return super().button_cancel()