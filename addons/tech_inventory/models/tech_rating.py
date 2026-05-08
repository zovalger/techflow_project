from odoo import models, fields, api

class TechRating(models.Model):
    _name = 'tech.rating'
    _description = 'Valoracion de Equipo Tecnológico'
    _order = 'name'


    equipment_id = fields.Many2one(
        'tech.equipment', 
        string='Equipo',
        required=True
    )

    evaluated_by_id = fields.Many2one(
        'res.users', 
        string='Evaluador',
        default= lambda self: self.env.user,
        required=True
    )
    
    rating_date = fields.Date(string='Fecha de Compra')