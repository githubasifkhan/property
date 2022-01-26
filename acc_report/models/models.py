from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from datetime import datetime
from datetime import timedelta


class AccountReport(models.TransientModel):
    _name = 'acc.report'

    account_type = fields.Selection([
        ('receive', 'Receivable'),
        ('pay', 'Payable'),
    ], string='Account', default='receive')

    def menu_report_action(self):
        data = {
            'form': self.read()[0],
        }
        return self.env.ref('acc_report.test_report_pdf').report_action(self, data=data)

    def get_current_invoices(self, partner, context):
        print(context)
        print(self.account_type)
        if self.account_type == 'receive':
            account = 'Account Receivable'
            journal = 'Customer Invoices'
        else:
            account = 'Account Payable'
            journal = 'Vendor Bills'

        current_invoices = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.name', '=', account),
             ('move_id.invoice_date_due', '=', datetime.today().date())])
        last = datetime.today().date() - relativedelta(months=1)
        oneto30 = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.name', '=', account),
             ('move_id.invoice_date_due', '>=', last), ('move_id.invoice_date_due', '<', datetime.today().date())])
        tto60 = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.name', '=', account),
             ('move_id.invoice_date_due', '>=', last - relativedelta(months=1)),
             ('move_id.invoice_date_due', '<', last)])
        last = last - relativedelta(months=1)
        tto90 = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.name', '=', account),
             ('move_id.invoice_date_due', '>=', last - relativedelta(months=1)),
             ('move_id.invoice_date_due', '<', last)])
        last = last - relativedelta(months=1)
        tto120 = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', 'journal'),
             ('account_id.name', '=', account),
             ('move_id.invoice_date_due', '>=', last - relativedelta(months=1)),
             ('move_id.invoice_date_due', '<', last)])
        last = last - relativedelta(months=1)
        older = self.env['account.move.line'].search(
            [('partner_id', '=', partner.id), ('journal_id.name', '=', journal),
             ('account_id.name', '=', account),
             ('move_id.invoice_date_due', '<=', last)])
        if context == 'current':
            return current_invoices
        if context == 'oneto30':
            return oneto30
        if context == 'tto60':
            return tto60
        if context == 'tto90':
            return tto90
        if context == 'tto120':
            return tto120
        if context == 'older':
            return older



