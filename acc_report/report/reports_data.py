from dateutil.relativedelta import relativedelta

from odoo import models, api
from datetime import date
from datetime import timedelta, datetime


class AccReport(models.AbstractModel):
    _name = 'report.acc_report.test_report_id_print'
    _description = 'Acc Report'

    def get_current_invoices(self, partner, context):
            print(self.account_type)
            if self.account_type == 'receive':
                account = 'Account Receivable'
                journal = 'Customer Invoices'
            else:
                account = 'Account Payable'
                journal = 'Vendor Bills'

            # print(account)
            # print(journal)

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
            # print(current_invoices)
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

    @api.model
    def _get_report_values(self, docids, data=None):
        result = self.env['acc.report'].browse(self.env.context.get('active_ids'))
        if result['account_type'] == 'receive':
            account = 'Account Receivable'
            journal = 'Customer Invoices'
        else:
            account = 'Account Payable'
            journal = 'Vendor Bills'
        print(result['partner_id'].name)
        partner = result['partner_id']
        # partners = self.env['account.move.line'].search([]).mapped('partner_id')
        # print(partners)
        # my_data = {}
        # for partner in partners:
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

        return {
            'docs': result,
            'doc_model': 'acc.report',
            'current_invoices': current_invoices,
            'oneto30': oneto30,
            'tto60': tto60,
            'tto90': tto90,
            'tto120': tto120,
            'older': older,
            # 'partners': partners,

        }








