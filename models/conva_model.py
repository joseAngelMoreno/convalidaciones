# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class conva_model(models.Model):
    _name='convalidaciones.conva_model'
    _description = 'Modelo de Convalidaciones'

    fecha=fields.Date(string="Fecha",required=True,help="Fecha obligatoria para convalidar",default=datetime.today())
    modulo_id=fields.Many2one("convalidaciones.modulo_model","modulo")
    alumno_id=fields.Many2one("convalidaciones.alumno_model","alumno")