# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AircargoCity(models.Model):
    _name = 'aircargo.city'

    name = fields.Char()
    description = fields.Text()


class AircargoCustoms_place(models.Model):
    _name = 'aircargo.customs_place'

    name = fields.Char()
    description = fields.Text()


class AircargoShipper(models.Model):
    _name = 'aircargo.shipper'

    name = fields.Char()
    description = fields.Text()


class AircargoTerminal(models.Model):
    _name = 'aircargo.terminal'

    name = fields.Char()
    description = fields.Text()


class AircargoTransport_mean(models.Model):
    _name = 'aircargo.transport_mean'

    name = fields.Char()
    description = fields.Text()
