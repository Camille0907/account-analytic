# Copyright 2022 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    department_id = fields.Many2one(
        "hr.department", related="analytic_account_id.department_id"
    )
