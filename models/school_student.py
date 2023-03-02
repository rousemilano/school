# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    name = fields.Char(string="Name")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    final_exam_grade = fields.Float(string="Final Exam Grade")
    subject_ids = fields.Many2many(string="Subjects", comodel_name="school.subject")

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            rec.age = relativedelta(datetime.now(), rec.birth_date).years