#-*- coding: utf-8 -*-
from odoo import models, fields

class HrDepartment(models.Model):
    _inherit = 'hr.department'
    
    code = fields.Char(
        string='Codigo'
    )    