
from odoo import models, fields

class tinymce(models.Model):
    _name = 'wysiwyg.tinymce'
    _description = 'TinyMce'

    name = fields.Char(string='Nama')
    tanggal = fields.Date(string='Tanggal')
    description = fields.Text(string='Deskripsi')

    
