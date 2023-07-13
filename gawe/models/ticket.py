# -*- coding: utf-8 -*-

from odoo import models, fields # Mandatory


class Ticket(models.Model):
    _name = 'gawe.ticket' # name_of_module.name_of_class 
    _description = 'Ticket Gawe' # Some note of table

    # Header
    name = fields.Char(required=True, string="Nama Gawe")
    date = fields.Date(string="Tanggal")
    description = fields.Html(string="Deskripsi")
    status = fields.Selection([('draft','Draft'),('to_approve','To Approve'),('approved','Approved'),('done','Done')],default='draft')
