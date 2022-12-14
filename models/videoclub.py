
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
     director = fields.Many2one('videoclub.director')

     @api.onchange('duracion')
     def _comprobar_duracion(self):
         for record in self:
             if record.duracion and not(record.duracion > 39 and record.duracion < 181):
                raise models.ValidationError('La duración debe estar comprendida entre 40 y 180 minutos.')


class director(models.Model):
    _name='videoclub.director'
    _description ='Director de la pelicula'
    nombre = fields.Char('Nombre')
    apellido = fields.Char('Apellido')
    peliculas = fields.One2many('videoclub.pelicula','director')

    _rec_name='nombre'

    @api.constrains('nombre')
    def _check_name(self):
        for r in self:
            if len(r.nombre) < 2:
                raise models.ValidationError('La longitud del nombre del director debe ser mayor de 2 caracteres')

    # Not Working
    #@api.one
    #def name_get(self):
    #    res = []
    #    for r in self:
    #        res.append ((r.nombre, r.apellido))
    #    return res    

