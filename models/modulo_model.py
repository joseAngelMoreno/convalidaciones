# -*- coding: utf-8 -*-

from odoo import models, fields, api
class modulo_model(models.Model):
    _name='convalidaciones.modulo_model'
    _description = 'Modelo de modulo'

    name=fields.Char(string="Nombre",required=True,index=True,help="Nombre del modulo",size=10)
    descripcion=fields.Html(string="Descripcion",required=True,help="Descripcion del modulo")
    horas=fields.Integer(string="Carga horaria (Horas)",required=True,help="horas del modulo")
    ciclos_id = fields.Many2one("convalidaciones.ciclo_model","Ciclo")