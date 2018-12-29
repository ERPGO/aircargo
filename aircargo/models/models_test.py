# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AircargoCity(models.Model):
    _name = 'aircargo.city'

    name = fields.Char()
    description = fields.Text()

