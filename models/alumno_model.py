# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api
from odoo.exceptions import ValidationError
class alumno_model(models.Model):
    _name='convalidaciones.alumno_model'
    _description = 'Modelo de alumnos'
    

    name =fields.Char(string="Nombre",required=True,index=True,help="Nombre del alumno")
    foto=fields.Binary()
    password=fields.Char(string="Password",help="Password del alumno",size=10)
    edad=fields.Integer(string="Edad",required=True,help="Edad del alumno")
    localidad=fields.Char(string="Localidad",required=True,help="Localidad del alumno",size=100)
    provincia=fields.Char(string="Provincia",required=True,help="Provincia del alumno",size=100)
    email=fields.Char(string="Email",required=False,help="Email del alumno",size=100)
    convalidaciones=fields.One2many("convalidaciones.conva_model","alumno_id",string="convalidaciones")
    profesores=fields.Many2many("convalidaciones.profesor_model",relation="alumnos2profesores_rel",string="profesores")


    def generarPassword(self):
        self.password=""
        self.ensure_one()
        for i in range (10):
            self.password+=random.choice("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    @api.constrains("edad")
    def _check_longitud(self):
        if self.edad < 14:
            raise ValidationError("La edad no puede ser menor de 14!")
            
            
