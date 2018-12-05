# -*- coding: utf-8 -*-
from odoo import models, fields, api


class application(models.Model):
    _name='seek.application'
    application_date=fields.Date("Applying Date",default=fields.datetime.now())
#     application_state=fields.Selection([('draft', 'Draft'), ('accepted', "Accepted"), ('rejected', "Rejected")])
    seeker_id=fields.Many2one('seek.seeker')
    job_id=fields.Many2one('seek.job')

class job(models.Model):

    _name='seek.job'

    #job_info
    company_pic=fields.Binary("Upload pic")
  
    job_name=fields.Char("Job Name")
    job_posted_date=fields.Date("Posted Date", default=lambda self: fields.datetime.now() )
    job_career_level=fields.Selection([('manager', "Manager"), 
    ('experienced', "Experienced"),
    ('entry', "Entry Level")])    
    job_closes_date=fields.Date("Job Closes Date ")
    Job_vacancies=fields.Integer("Vacancies")
    job_location=fields.Text("Job location")
    job_description=fields.Text("Job description")
     
    #target employee

    job_requierd_education_level=fields.Selection([('bachelor', "Bachelor's Degree"), 
    ('master', "Master's Degree"),
    ('phd', "PHD Degree")])

    job_experience_years=fields.Selection([('one_to_two', "1-2 Years"), 
    ('three_to_five', "3-5 Years"),
    ('six_to_ten', "6-10 Years"),
    ('more_than_ten', "10+ Years")])

    job_requierd_spicality=fields.Selection([('engeneering', "Engeneering"), 
    ('business', "business"),
    ('medical', "Medical"),
    ('marketing', "Marketing")])
    
    job_status=fields.Selection([('full_time', 'Full Time'), ('part_time', "Part Time")])

    job_type=fields.Selection([('employee', "Employee"), 
    ('volenteer', "Volenteer"),
    ('internship', "Internship"),
    ('project', "Project")])

    job_salary=fields.Selection([('two_to_five', "2000-5000 SDG"), 
    ('five_to_ten', "5000-1000 SDG"),
    ('ten_to_fifteen', "1000-1500 SDG"),
    ('more_than_fifteen', "1500+ SDG")])
    
    # Job_state=fields.Selection([('avaliable', 'Avaliable'), ('applied', "applied")])

    application_id = fields.Many2one(
        comodel_name='seek.application')

    company_id= fields.Many2one(
        comodel_name='seek.company')


class seeker(models.Model):
    _name = 'seek.seeker'
    _inherits = {'res.partner':'partner_id'}
    partner_id=fields.Many2one('res.partner')

    seeker_date_of_birth=fields.Date()
    seeker_gender=fields.Selection([('male', 'Male'), ('female', "Female")])
    seeker_nationalty=fields.Char()

    #Target Job

    seeker_education_level=fields.Selection([('bachelor', "Bachelor's Degree"), 
    ('master', "Master's Degree"),
    ('phd', "PHD Degree")])

    seeker_years_of_experince=fields.Selection([('one_to_two', "1-2 Years"), 
    ('three_to_five', "3-5 Years"),
    ('six_to_ten', "6-10 Years"),
    ('more_than_ten', "10+ Years")])

    seeker_specialization=fields.Selection([('engeneering', "Engeneering"), 
    ('business', "business"),
    ('medical', "Medical"),
    ('marketing', "Marketing")])
    
    seeker_job_status=fields.Selection([('full_time', 'Full Time'), ('part_time', "Part Time")])

    seeker_job_type=fields.Selection([('employee', "Employee"), 
    ('volenteer', "Volenteer"),
    ('internship', "Internship"),
    ('project', "Project")])

    seeker_job_salary=fields.Selection([('two_to_five', "2000-5000 SDG"), 
    ('five_to_ten', "5000-1000 SDG"),
    ('ten_to_fifteen', "1000-1500 SDG"),
    ('more_than_fifteen', "1500+ SDG")])

class company(models.Model):
    _name='seek.company'
    _inherit = 'res.company'
    # company_pict=fields.Binary("Upload Company photo")
    # company_name=fields.Char("Company name")
    # company_name=fields.Text("Company Address")
    brif_description=fields.Text("Brif Description about the company")
    company_jobs= fields.One2many('seek.job', "company_id")

    
    # seekers_job_applications=fields.One2many('seek.application','seekers_job_application')


    