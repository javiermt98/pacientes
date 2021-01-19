#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class pacientes_app(models.Model):
    _name = 'pacientes_app.visitas_model'
    _description = 'Modelo de Visitas'

    name = fields.Many2one("pacientes_app.pacientes_model", string="Pacientes")
    fecha = fields.Datetime(string="Fecha de la visita", required=True, default=fields.Datetime.now)
    detalle = fields.Html(string="Detalle de la consulta", required=True)
    visitas_id = fields.Many2one("pacientes_app.pacientes_model", "Paciente")


