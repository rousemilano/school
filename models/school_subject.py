# -*- coding: utf-8 -*-

from odoo import fields, models


class SchoolSubject(models.Model):
    _name = "school.subject"
    _description = "School Subject"

    name = fields.Char(string="Name", required=True)
    credits = fields.Integer(string="Credits", required=True)
    max_students = fields.Integer(string="Students Max")
    active = fields.Boolean(string="Active", default=True)
    student_ids = fields.Many2many(string="Students", comodel_name="school.student", readonly=True)
    teacher_id = fields.Many2one(string="Teacher", comodel_name="school.teacher", required=True)


class SchoolSubjectLine(models.Model):
    _name = "school.subject.line"
    _description = "School Subject Line"

    subject_id = fields.Many2one(string="Subjects", comodel_name="school.subject")
    name = fields.Char(string="Name", related='subject_id.name', store=True)
    credits = fields.Integer(string="Credits", related='subject_id.credits', store=True)
    max_students = fields.Integer(string="Students Max", related='subject_id.max_students', store=True)
    teacher_id = fields.Many2one(string="Teacher", comodel_name="school.teacher")
