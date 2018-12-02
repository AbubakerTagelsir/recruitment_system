# -*- coding: utf-8 -*-
from odoo import models, fields, api

# class recruitment(models.Model):

class application(models.Model):
    _name='seek.application'
    application_date=fields.Date("Applying Date")
    application_state=fields.Selection([('draft', 'Draft'), ('accepted', "Accepted"), ('rejected', "Rejected")])
    seeker_id=fields.Many2one('seek.seeker')
    job_id=fields.One2many('seek.job','application_id')
    seekers_job_application=fields.Many2one('seek.company')

class job(models.Model):

    _name='seek.job'
    job_name=fields.Char("Job Name", compute='generate_jobe_name')
    
    posted_date=fields.Date("Posted Date")
    company_id=fields.Many2one('seek.company')
    job_pic=fields.Binary("Upload pic")
    job_experience_years=fields.Char("Years of Experiece")
    job_career_level=fields.Char("Career Level")
   
    
    job_closes_date=fields.Date("Job Closes Date ")
    Job_vacancies=fields.Integer("Vacancies")
    
    job_location=fields.Text("Job location")
    job_requierd_education_level=fields.Char("Education Level")
    iob_related_industry=fields.Text("Industry")
    job_requierd_spicality=fields.Char("Spicality")
    job_description=fields.Text("Job description")
     
    #target employee
    iob_role=fields.Text("Job Role")
    job_status=fields.Selection([('full_time', 'Full Time'), ('part_time', "Part Time")])
    job_type=fields.Char("Job Type")
    job_salary=fields.Float("Job salary")
    
    # Job_state=fields.Selection([('avaliable', 'Avaliable'), ('applied', "applied")])

    application_id = fields.Many2one(
        comodel_name='seek.application',
        ondelete='set null',)

    company_jobs= fields.Many2one(
        comodel_name='seek.company',
        ondelete='set null',)

    @api.one
    def generate_jobe_name(self):
        self.name = "JOB-00" + str(self.id)


class seeker(models.Model):
    _name = 'seek.seeker'
    _inherit = 'res.partner'
    seeker_date_of_birth=fields.Date()
    seeker_gender=fields.Selection([('male', 'Male'), ('female', "Female")])
    seeker_nationalty=fields.Char()
    seeker_residence_country=fields.Char()
    seeker_city=fields.Char()
    seeker_years_of_experince=fields.Char()
    seeker_specialization=fields.Char()
     
    #Target Job
    seeker_job_type=fields.Char("Job Type")
    seeker_job_status=fields.Selection([('full_time', 'Full Time'), ('part_time', "Part Time")])
    seeker_iob_role=fields.Text("Job Role")
    seeker_job_salary=fields.Float("Job salary")



    application_id=fields.Many2one('seek.application','application')

class company(models.Model):
    _name='seek.company'
    # _inherit = 'res.partner'
    company_jobs= fields.One2many('seek.job', "company_jobs")
    
    seekers_job_applications=fields.One2many('seek.application','seekers_job_application')


    