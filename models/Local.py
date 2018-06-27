# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Local(models.Model):
    _name = "alq.local"

    NLocal = fields.Char(string="Numero de local")
    Area = fields.Integer(string="Area m2")
    Melect = fields.Integer(string="Medidor de Electricidad")
    MeAgua = fields.Integer(string="Medidor de Agua")
    piso_id = fields.Many2one("alq.piso",string="Piso")
