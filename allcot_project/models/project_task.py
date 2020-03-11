# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    x_duration = fields.Integer('Duration in days', stored=True)
    x_end_date = fields.Date('End date', readonly=True, stored=True)
    x_next_task = fields.Many2one('project.task', 'Next task', readonly=True, ondelete='set null',
                                  compute='_compute_next_task')
    x_previous_task = fields.Many2one('project.task', 'Previous task', stored=True, ondelete='set null')
    x_relation = fields.Selection([('finish', 'Finish to start'), ('start', 'Start to start'), ('none', 'No relation')],
                                  'Task relation', stored=True)
    x_start_date = fields.Date('Start date', stored=True)
    x_studio_created_on = fields.Date('Created on', stored=True)
    x_studio_field_9M0pF = fields.Many2one('product.product', 'Product', stored=True, ondelete='set null')
    x_copy_of = fields.Many2one('project.task')

    def _compute_next_task(self):
        for record in self:
            record.x_next_task = self.env['project.task'].search([('x_previous_task', '=', record.id)], limit=1).id

    def copy(self, default=None):
        default = dict(default or {})
        default['x_copy_of'] = self.id
        return super(ProjectTask, self).copy(default)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def copy(self):
        res = super(ProjectProject, self).copy()
        for task in res.task_ids:
            if task.x_previous_task:
                task.x_previous_task = self.env['project.task'].search([('x_copy_of', '=', task.x_previous_task.id)], order='id desc', limit=1)
        return res
