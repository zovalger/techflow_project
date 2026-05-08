from odoo import models, fields, api

class TechRating(models.Model):
    _name = 'tech.rating'
    _description = 'Valoracion de Equipo Tecnológico'
    _order = 'name'


    equipment_id = fields.Many2one(
        'tech.equipment', 
        string = 'Equipo',
        required = True
    )

    evaluated_by_id = fields.Many2one(
        'res.users', 
        string ='Evaluador',
        default = lambda self: self.env.user,
        required = True
    )
    
    rating_date = fields.Date(
        string = 'Fecha de la valoración',
        required = True,
        default = fields.Date.today
        )
    
    rating = fields.Selection([
        ('bad', 'Malo'),
        ('regular', 'Regular'),
        ('good', 'Excelente')
        ], 
        string = 'Valoración',
        required = True,
        default='available',
    )      

    is_recommended = fields.Boolean(
        string = 'Es recomendado',
        store=True,
        compute="_compute_is_recommended",
    )
    
    active = fields.Boolean(
        string = 'Activo',
        required = True,
        default = False
    )

    name = fields.Char(
        string='Nombre de la valoración',
        store=True,
        compute="_compute_name",
    )

    @api.depends('rating') 
    def _compute_is_recommended(self): 
        for record in self:
            if record.rating == 'good':   
                record.is_recommended = True
            else:
                record.is_recommended = False

    @api.depends('rating_date', 'equipment_id') 
    def _compute_name(self): 
        for record in self:
            if record.equipment_id.name and record.rating_date:
                record.name = f"Valoración: {record.equipment_id.name} ({record.rating_date})"
            else:
                record.name = f"Nueva Valoración: ({record.rating_date})"