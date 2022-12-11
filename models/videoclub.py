
# Importamos de Odoo las clases 
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class pelicula(models.Model):
     _name = 'videoclub.pelicula'
     _description = 'Pelicula que se almacenará en el videoclub'

     titulo = fields.Char('Título')
     autor_ids = fields.Many2many('res.partner',string='Autor')
     duracion = fields.Float('Duración en minutos')
     descripcion = fields.Text('Descripción')

     @api.onchange('duracion')
     def _comprobar_duracion(self):
         for record in self:
             if record.duracion and not(record.duracion > 39 and record.duracion < 181):
                raise models.ValidationError('La duración debe estar comprendida entre 40 y 180 minutos.')
