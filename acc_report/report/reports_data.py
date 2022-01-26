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
        if result['account_type'] == 'receive':
            account = 'receivable'
            journal = 'Customer Invoices'
        else:
            account = 'payable'
            journal = 'Vendor Bills'
        partner = result['partner_id']
        current_invoices = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.internal_type', '=', account),
             ('move_id.invoice_date_due', '=', datetime.today().date())])
        last = datetime.today().date() - relativedelta(months=1)
        oneto30 = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.internal_type', '=', account),
             ('move_id.invoice_date_due', '>=', last), ('move_id.invoice_date_due', '<', datetime.today().date())])
        tto60 = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.internal_type', '=', account),
             ('move_id.invoice_date_due', '>=', last - relativedelta(months=1)),
             ('move_id.invoice_date_due', '<', last)])
        last = last - relativedelta(months=1)
        tto90 = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.internal_type', '=', account),
             ('move_id.invoice_date_due', '>=', last - relativedelta(months=1)),
             ('move_id.invoice_date_due', '<', last)])
        last = last - relativedelta(months=1)
        tto120 = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', 'journal'),
             ('account_id.internal_type', '=', account),
             ('move_id.invoice_date_due', '>=', last - relativedelta(months=1)),
             ('move_id.invoice_date_due', '<', last)])
        last = last - relativedelta(months=1)
        older = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.internal_type', '=', account),
             ('move_id.invoice_date_due', '<=', last)])
        return {
            'docs': result,
            'doc_model': 'acc.report',
            'current_invoices': current_invoices,
            'oneto30': oneto30,
            'tto60': tto60,
            'tto90': tto90,
            'tto120': tto120,
            'older': older,
        }








