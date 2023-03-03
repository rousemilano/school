# -*- coding: utf-8 -*-

from odoo import fields, models


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "School Teacher"

    name = fields.Char(string="Name", required=True)
    profile = fields.Text(string="Profile", required=True)
    subject_ids = fields.One2many("school.subject.line", "teacher_id", string="Subjects")

