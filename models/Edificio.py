# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Edicio(models.Model):
    _name = "alq.edificio"

    NEdificio = fields.Char(string="Edificio")
    Direccion = fields.Char(string="Direccion")
    AreaT = fields.Integer(string="Area m2 de Terreno")
    AreaC = fields.Integer(string="Area m2 de Construccion")
    ValorR = fields.Integer(string="Valor Real")
    ValorF = fields.Integer(string="Valor Fiscal")
