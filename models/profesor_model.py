# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError
letra="TRWAGMYFPDXBNJZSQVHLCKE"
class profesor_model(models.Model):
    _name='convalidaciones.profesor_model'
    _description = 'Modelo de profesor'


    name =fields.Char(string="Nombre",required=True,index=True,help="Nombre del profesor")
    apellidos=fields.Char(string="Apellidos",required=True,help="Apellidos del profesor")
    foto=fields.Binary()
    dni=fields.Char(string="DNI",required=True,help="Dni del profesor")
    alumnos=fields.Many2many("convalidaciones.alumno_model",relation="alumnos2profesores_rel",string="Alumnos")
    numAlumnos=fields.Integer(string="Numero de alumnos",compute="calcAlumnos",store=True)

    @api.depends("alumnos")
    def calcAlumnos(self):
        self.numAlumnos=len(self.alumnos)


   
            

