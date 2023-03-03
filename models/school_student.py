# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models

from odoo.exceptions import UserError


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    name = fields.Char(string="Name", required=True)
    birth_date = fields.Date(string="Birth Date", required=True)
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    final_exam_grade = fields.Float(string="Final Exam Grade")
    subject_ids = fields.Many2many(string="Subjects", comodel_name="school.subject")

    @api.constrains('subject_ids')
    def _constrain_max_subject(self):
        for rec in self.subject_ids:
            if len(rec.student_ids) > rec.max_students:
                raise UserError("This subject can't be add. Limit of students allowed exceeded")

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            rec.age = relativedelta(datetime.now(), rec.birth_date).years