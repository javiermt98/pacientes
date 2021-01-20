#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, date


class pacientes_app(models.Model):
    _name = 'pacientes_app.pacientes_model'
    _description = 'Modelo de Pacientes'

    name = fields.Char(string="Nombre", size=20, required=True)
    dni = fields.Char(string="DNI", required=True, )
    apellidos = fields.Char(string="Apellidos",size=30, required=True)
    telf = fields.Integer(string="Telefono", size=15, required=True)
    email = fields.Char(string="Email", required=True)
    fechanacim = fields.Date(string="Fecha de Nacimiento", required=True, default=fields.Date.context_today)
    foto = fields.Binary()
    visitas = fields.One2many("pacientes_app.visitas_model", "visitas_id", string="Visitas")
    numvisitas = fields.Integer(string="Número de visitas", compute="_getNumpaci", store=True, readonly=True)

    @api.constrains("dni")
    def _comprobarDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")

    @api.constrains("fechanacim")
    def _mayoredad(self):
        fechanow = date.today()
        if int(fechanow.year - self.fechanacim.year) <18:
            raise ValidationError("Debe ser mayor de edad")

    @api.constrains("email")
    def _correoValido(self):
        if "@" not in self.email:
            raise ValidationError("El correo electrónico debe tener un formato válido")

    @api.depends("visitas")
    def _getNumpaci(self):
        self.numvisitas = len(self.visitas)

    def eliminaTareas(self):
        self.visitas.unlink()


