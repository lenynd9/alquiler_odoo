# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Piso(models.Model):
    _name = "alq.piso"

    NPiso = fields.Char(string="Piso")
    edificio_id = fields.Many2one("alq.edificio",string="Edificio")

