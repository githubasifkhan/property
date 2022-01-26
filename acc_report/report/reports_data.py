from dateutil.relativedelta import relativedelta

from odoo import models, api
from datetime import date
from datetime import timedelta, datetime


class AccReport(models.AbstractModel):
    _name = 'report.acc_report.test_report_id_print'
    _description = 'Acc Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        result = self.env['acc.report'].browse(self.env.context.get('active_ids'))
        partners = self.env['account.move.line'].search([]).mapped('partner_id')
        return {
            'docs': result,
            'doc_model': 'acc.report',
            'partners': partners
        }








