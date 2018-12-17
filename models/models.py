# -*- coding: utf-8 -*-
from odoo import models, fields, api


class application(models.Model):
    _name='seek.application'
    application_date=fields.Date("Applying Date",default=fields.datetime.now())
    application_state=fields.Selection([('draft', 'Draft'), ('accepted', "Accepted"), ('rejected', "Rejected")])
    # seeker_id=fields.Many2one('seek.seeker')
    seeker_id=fields.Many2one('res.partner')
    job_id=fields.Many2one('seek.job')

    app_education_level=fields.Selection([('bachelor', "Bachelor's Degree"), 
    ('master', "Master's Degree"),
    ('phd', "PHD Degree")])

    app_experience_years=fields.Selection([('one_to_two', "1-2 Years"), 
    ('three_to_five', "3-5 Years"),
    ('six_to_ten', "6-10 Years"),
    ('more_than_ten', "10+ Years")])

    app_spicality=fields.Selection([('engeneering', "Engeneering"), 
    ('business', "business"),
    ('medical', "Medical"),
    ('marketing', "Marketing")])

    app_status=fields.Selection([('full_time', 'Full Time'), ('part_time', "Part Time")])

    app_job_type=fields.Selection([('employee', "Employee"), 
    ('volunteer', "Volunteer"),
    ('internship', "Internship"),
    ('contract', "Contract")])

    app_job_salary=fields.Selection([('two_to_five', "2000-5000 SDG"), 
    ('five_to_ten', "5000-10000 SDG"),
    ('ten_to_fifteen', "10000-15000 SDG"),
    ('more_than_fifteen', "15000+ SDG")])

    app_cv=fields.Binary()


 

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

    # job_requierd_spicality=fields.Selection([('engeneering', "Engeneering"), 
    # ('business', "business"),
    # ('medical', "Medical"),
    # ('marketing', "Marketing")])
    
    #///////////////////////////////////////////////////////////////////////////////////////////
    job_status=fields.Selection([('full_time', 'Full Time'), ('part_time', "Part Time")])

    job_type=fields.Selection([('employee', "Employee"), 
    ('volunteer', "Volunteer"),
    ('internship', "Internship"),
    ('contract', "Contract")])

    job_salary=fields.Selection([('two_to_five', "2000-5000 SDG"), 
    ('five_to_ten', "5000-10000 SDG"),
    ('ten_to_fifteen', "10000-15000 SDG"),
    ('more_than_fifteen', "15000+ SDG")])
    #///////////////////////////////////////////////////////////////////////////////////////////
    
    job_state=fields.Selection([('avaliable', "Avaliable"), ('not_avaliable', "Not Avaliable")])

    application_id = fields.Many2one(
        comodel_name='seek.application')

    company_id= fields.Many2one(
        comodel_name='res.company')

    skills=fields.One2many('seek.skill','job_id')

    # education=fields.One2many('seek.education','job2_id')

    education_level=fields.Selection([('bachelor', "Bachelor's Degree"), 
    ('master', "Master's Degree"),
    ('phd', "PHD Degree")])

    experience=fields.One2many('seek.experience','job3_id')

    specialization=fields.Many2one('seek.specialization','Major')

    seeker_id=fields.Many2one('res.partner')



    # def apply_for_job(self):

    #     app_obj = self.env['seek.application']
    #     current_partner = self.env.user.partner_id
    #     # self.ensure_one()
    #     application = app_obj.create({
    #         'job_id':self.id,
    #         'application_date':fields.Datetime.now(), 
    #         'seeker_id':current_partner.id,
    #         'seeker_education_level':current_partner.seeker_education_level,
    #         'seeker_experience_years':current_partner.seeker_years_of_experince,
    #         'seeker_spicality':current_partner.specialization,
    #         'seeker_status':current_partner.seeker_job_status,
    #         'seeker_job_type':current_partner.seeker_job_type,
    #         'seeker_job_salary':current_partner.seeker_job_salary,
    #         'seeker_cv':current_partner.seeker_cv,
    #          })
            
        # for app in self:
        #     score=0
        #     if app.education_level == app.seeker_id.seeker_education_level:
        #         score+=1
        #     if app.job_experience_years == app.seeker_id.seeker_years_of_experince:
        #         score+=1
        #     if app.specialization == app.seeker_id.seeker_specialization:
        #         score+=1
        #     if app.job_status == app.seeker_id.seeker_job_status:
        #         score+=1
        #     if app.job_type == app.seeker_id.seeker_job_type:  
        #         score+=1
        #     if app.job_salary == app.seeker_id.seeker_job_salary:  
        #         score+=1
        # if score>3 :
        #         self.application_state='accepted'
        # else:
        #             self.application_state='rejected'

class skill(models.Model):
    _name='seek.skill'  
    _rec_name = 'skill_name'

    skill_name=fields.Char("Skill Name")
    skill_proficiency=fields.Selection([('beginner', "Beginner"), 
    ('intermediat', "Intermediat"),
    ('advanced', "Advanced")])
    years_of_experince=fields.Selection([('less_than_one', "less than Year"), 
     ('one_to_two', "1-2 Years"), 
    ('three_to_five', "3-5 Years"),
    ('six_to_ten', "6-10 Years"),
    ('more_than_ten', "10+ Years")])
     
    job_id=fields.Many2one('seek.job')
    seek_id=fields.Many2one('res.partner')                

class education(models.Model):
    _name='seek.education'

    education_level=fields.Selection([('bachelor', "Bachelor's Degree"), 
    ('master', "Master's Degree"),
    ('phd', "PHD Degree")])
    institute=fields.Char("University/Institute")
    graduation_year=fields.Date("Graduation year")
    grade=fields.Char("Graduation Grade")

    job2_id=fields.Many2one('seek.job')
    seek2_id=fields.Many2one('res.partner')


class experience (models.Model):
    _name='seek.experience'

    company_worked_for=fields.Char("Company worked for")
    position=fields.Char("position worked for")
    start_date=fields.Date("Start Date")
    end_date=fields.Date("End Date")


    job3_id=fields.Many2one('seek.job')
    seek3_id=fields.Many2one('res.partner')

class specialization (models.Model):
    _name='seek.specialization'
    _rec_name = 'specialization_type'

    specialization_type=fields.Char("Specialization Type")

    job4_id=fields.Many2one('seek.job')
    seek4_id=fields.Many2one('res.partner')


class seeker(models.Model):
    # _name = 'seek.seeker'
    _inherit = 'res.partner'
    partner_id=fields.Many2one('res.partner',default=lambda self: self.env.user.partner_id)
    # cc = fields.Boolean(
    #     string=u'cc',
    #     default=lambda self: self._get_cc
    # )
    # def _get_user_id(self):
    #     self.partner_id = self.env['res.users'].search([
    #         ('partner_id', '=', self.id)
    #     ])
    # @api.one
    # def _get_cc(self):
    #     if self.id == self.partner_id:
    #         self.cc = True

    # def view_seeker_profile(self):
        
    #     context = {'partner_id': self.id, },
    #     # view_id = self.ref('souq.')
    #     return {
    #         'name': 'Order Bookings',
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'res_model': 'res.partner',
    #         'domain': [('partner_id', '=', self.id)],
    #         'context': context,
    #         'target': 'current',
    #     }    

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
    
    # specialization=fields.Many2one('seek.specialization','Major')

    seeker_specialization=fields.Many2one('seek.specialization')

    # seeker_specialization=fields.Selection([('engeneering', "Engeneering"), 
    # ('business', "business"),
    # ('medical', "Medical"),
    # ('marketing', "Marketing")])

    #///////////////////////////////////////////////////////////////////////////////////////////
    seeker_job_status=fields.Selection([('full_time', 'Full Time'), ('part_time', "Part Time")])

    seeker_job_type=fields.Selection([('employee', "Employee"), 
    ('volenteer', "Volenteer"),
    ('internship', "Internship"),
    ('project', "Project")])

    seeker_job_salary=fields.Selection([('two_to_five', "2000-5000 SDG"), 
    ('five_to_ten', "5000-10000 SDG"),
    ('ten_to_fifteen', "10000-15000 SDG"),
    ('more_than_fifteen', "15000+ SDG")])
    #///////////////////////////////////////////////////////////////////////////////////////////

    skills=fields.One2many('seek.skill','seek_id')

    education=fields.One2many('seek.education','seek2_id')

    experience=fields.One2many('seek.experience','seek3_id')

    specialization=fields.One2many('seek.specialization','seek4_id')

    seeker_cv=fields.Binary("CV")

class company(models.Model):
    # _name='seek.company'
    _inherit = 'res.company'
    brif_description= fields.Text("Brif Description about the company")

    company_jobs= fields.One2many('seek.job', "company_id")

    
    # seekers_job_applications=fields.One2many('seek.application','seekers_job_application')


    