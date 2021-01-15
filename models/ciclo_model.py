# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ciclo_model(models.Model):
    _name='convalidaciones.ciclo_model'
    _description = 'Modelo de ciclos'
    _sql_constraints = [
        ("ciclos_cicloUnico","UNIQUE (name)","Nombre ya esta en uso!!"),]

    name =fields.Char(string="Nombre del Ciclo",required=True,index=True,help="Nombre del Ciclo",size=10)
    descripcion=fields.Html(string="Descripcion",required=True,help="Descripcion del Ciclo")
    modulos=fields.One2many("convalidaciones.modulo_model","ciclos_id",string="modulos")


    