# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_candidat(models.Model):
	_name='hr_recrutement.candidat'
	_inherit='hr.employee'
	_description="Informations du Candidat"
	#_inherits = {'resource.resource': "resource_id"}
	

	situation=fields.Selection(string="Situation",selection=[('Nouveau','Nouveau'),('RDV Thechnique','RDV Technique'),('RDV RH','RDV RH'),('Disqualifie','Disqualifie'),('Annulation','Annulationn'),('Recrut sur mission','Recrut sur mission'),('Proposition faite','Proposition faite'),('Contrat signe','Contrat signe')])
	fonction=fields.Selection(string="Fonctions", selection=[('Consultant','Consultant'),('CP','CP'),('IED','IED')])
	mobilite=fields.Selection(string="Mobilité", selection=[('local','Local'),('Region','Region'),('Pays','Pays'),('Continent','Continent'),('Monde','Monde')])
	date_disp=fields.Date(string="Disponibilité",)
	permet_cond=fields.Selection(string="Permet de conduite", selection=[('Aucun','Aucun'),('Categorie A','Categorie A'),('Categorie B','Categorie B')])
	contrat=fields.Selection(string="Type de contrat", selection=[('CDD','CDD'),('CDI','CDI'),('CDI de chantier','CDI de chantier'),('Intérim','Interim'),('Contrat d’apprentissage','Contrat d’apprentissage'),('Contrat de professionnalisation','Contrat de professionnalisation'),('Convention de stage','Convention de stage'),('Freelance','Freelance')])
	domaine_ids=fields.One2many(comodel_name='hr_recrutement.domaine', inverse_name='id_cand', string='Domaines')
	langue_ids=fields.One2many(comodel_name='hr_recrutement.langue', inverse_name='id_cand', string='Langues')
	logiciel_ids=fields.One2many(comodel_name='hr_recrutement.logiciel', inverse_name='id_cand', string='Logiciels')
	langage_ids=fields.One2many(comodel_name='hr_recrutement.langage_prog', inverse_name='id_cand', string='Langages de Programmation')
	#country_id = fields.Many2one('res.country', 'Nationality')
	#emp_id = fields.Many2one('hr.employee', string="Employee", ondelete='cascade')
	#name_related = fields.related('resource_id', 'name', type='char', string='Name', readonly=True, store=True)
    #candidat_country_id = fields.related('id_cand','country', readonly=True, type='many2one',relation='res.country', string='Country')
	#emp_id = fields.Many2one('hr.employee', string='Employee')
	#department_id=fields.Many2one('hr.department', 'Department'),
	#employee_ids=fields.Many2many(comodel='hr.employee', relation='cand_empl_rel', column1='id_cand', column2='emp_id', string="Employee")
	#work_phone = fields.Char('Work Phone', readonly=False),
    #mobile_phone = fields.Char('Work Mobile', readonly=False),
    #work_email = fields.Char('Work Email', size=240),
    #work_location = fields.Char('Office Location'),
    #notes = fields.Text('Notes')	

class hr_domaine(models.Model):
	_name='hr_recrutement.domaine'
	_description="cette classe contient les differents domaines"

	nom=fields.Char(string="Domaine", size=50, required=True)
	annee_exp=fields.Integer(string="Année d'experience")
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='hr_recrutement.candidat', string='candidat', ondelete='cascade')

	#_sql_constraints =[('unique_nom','unique(nom)','ce domaine existe deja ! ')]


class hr_logiciel(models.Model):
	_name='hr_recrutement.logiciel'
	_description='cette classe contient les differents type de logiciels'

	nom=fields.Char(string="Logiciel", size=50, required=True)
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='hr_recrutement.candidat', string='candidat', ondelete='cascade')

	#_sql_constraints=[('unique_nom','unique(nom)','ce logiciel existe deja !')]


class hr_langue(models.Model):
	_name='hr_recrutement.langue'
	_description='cette classe contient les differentes langues'

	nom=fields.Char(string="Langue", size=50, required=True)
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='hr_recrutement.candidat', string='candidat', ondelete='cascade')

	#_sql_constraints=[('unique_nom','unique(nom)','cette langue existe deja !')]


class hr_langage_prog(models.Model):
	_name='hr_recrutement.langage_prog'
	_description='cette classe contient les differents types de langage de programmation'


	nom=fields.Char(string="langage de programmation", size=50, required=True)
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='hr_recrutement.candidat', string='candidat', ondelete='cascade')

	#_sql_constraints=[('unique_nom','unique(nom)','ce langage existe deja !')]


class hr_cvtheque(models.Model):
	_name='hr_recrutement.cvtheque'
	_description='cette classe contient les liens vers les CV'

	nom=fields.Char(string="CV", size=50, required=True)
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='hr_recrutement.candidat', string='candidat', ondelete='cascade')

	#_sql_constraints=[('unique_nom','unique(nom)','erreur de lien  !')]