from django import forms
from django.contrib import admin

from .models import NationalOrganization, ActivityReportForm, StakeholderDirectory, \
OrganizationTarget, GeographicActivity, FundingSource, TargetGroupPreventionMessage, \
OtherQuestion, EndOfYearQuestion, GeneralComment

from .models import IECMaterial, AdolecentsReached, OutOfSchool, SexWorker, Inmate, \
CorrectionalFaciltyStaff, PersonsWithDisabilty, MobileWorker, MenWithMen, \
CondomProgramming, CriticalEnabler, SynergyDevelopmentSector, CommunityHealthSystem, \
VulnerablePeople

from .forms import StakeholderDirectoryModelForm

# INLINES FOR STAKEHOLDER DIRECTORY ADMIN
# *************************************************
class GeographicActivityInline(admin.TabularInline):
    model = GeographicActivity
    verbose_name_plural = 'Geographic Activities'
    extra = 1

class FundingSourceInline(admin.TabularInline):
    model = FundingSource
    extra = 1

class TargetGroupPreventionMessageInline(admin.TabularInline):
    model = TargetGroupPreventionMessage
    extra = 1

class OtherQuestionInline(admin.TabularInline):
    model = OtherQuestion
    extra = 1

class EndOfYearQuestionInline(admin.TabularInline):
    model = EndOfYearQuestion
    extra = 1

class GeneralCommentInline(admin.StackedInline):
    model = GeneralComment
    extra = 1

# INLINES FOR ACTIVITY REPORT FORM ADMIN
# *************************************************
class MaterialInline(admin.TabularInline):
    model = IECMaterial
    verbose_name = 'IEC Material'
    verbose_name_plural = 'How many IEC materials were distributed by your organization this quarter? \
        Which of your materials were localized (produced according to local condition, culture, language etc.)? '
    extra = 1

class AdolencentsInline(admin.TabularInline):
    model = AdolecentsReached
    verbose_name_plural = 'Number of adolescents and young people aged 10-24 reached by IEC materials \
        by your organization this quarter'
    extra = 1

class OutOfSchoolInline(admin.TabularInline):
    model = OutOfSchool
    verbose_name_plural = 'Number of Out of School children and young people aged 10-24 years provided \
        with life skills- based comprehensive sexuality education within this quarter'
    extra = 1

class SexWorkerInline(admin.TabularInline):
    model = SexWorker
    verbose_name_plural = 'How many sex workers were reached with HIV prevention programmes by your \
        organization this quarter'
    extra = 1

class InmateInline(admin.TabularInline):
    model = Inmate
    verbose_name_plural = 'How many inmates were reached with HIV prevention programmes by your organization \
        this quarter?'
    extra = 1

class CorrectionalFaciltyStaffInline(admin.TabularInline):
    model = CorrectionalFaciltyStaff
    verbose_name_plural = 'How many correctional facility staff were reached with HIV prevention programmes \
        this quarter?'

class PersonsWithDisabiltyInline(admin.TabularInline):
    model = PersonsWithDisabilty
    verbose_name_plural = 'How many persons with disability were reached with HIV prevention programmes by your \
        organization this quarter?'
    extra = 1

class MobileWorkerInline(admin.TabularInline):
    model = MobileWorker
    verbose_name_plural = 'How many mobile workers were reached with HIV prevention programmes by your organization \
        this quarter?'
    extra = 1

class MenWithMenInline(admin.TabularInline):
    model = MenWithMen
    verbose_name_plural = 'How many men who have sex with men (MSM) were reached with HIV prevention programmes by \
        your organization this quarter?'
    extra = 1

class CondomProgrammingInline(admin.TabularInline):
    model = CondomProgramming
    verbose_name_plural = 'How many condom service distribution points were supplied by your organization this \
        quarter? (*excluding health facilities) How many male and/or female condoms were distributed to end users by \
        your organization this quarter (*excluding health facilities)?'
    extra = 1

class CriticalEnablerInline(admin.TabularInline):
    model = CriticalEnabler
    verbose_name_plural = 'Number of people who experienced physical or sexual violence and were referred for Post \
        Exposure Prophylaxis (PEP) within 72 hours in accordance with national guidelines this quarter.'
    extra = 1
    
class SynergyDevelopmentSectorInline(admin.TabularInline):
    model = SynergyDevelopmentSector
    verbose_name_plural = 'How many employees were reached through workplace programmes by your organization this quarter?'
    extra = 1

class CommunityHealthSystemInline(admin.TabularInline):
    model = CommunityHealthSystem
    verbose_name_plural = 'How many PLHIV support groups set up by your organisation are currently active? How many PLHIV \
        are currently enrolled in the active PLHIV support groups by your organisation?'
    extra = 1

class VulnerablePeopleInline(admin.TabularInline):
    model = VulnerablePeople
    verbose_name_plural = 'How many vulnerable people in total received care and support from your organisation this \
    quarter? What types of care and support does your organization provide? (select all that apply)'
    extra = 1

# ADMIN CLASSES
# *************************************************
class StakeholderDirectoryAdmin(admin.ModelAdmin):
    list_filter = ('national_orgnaization_name', 'organization_district')
    list_display = ('organization_name', 'key_contact_name', 'telephone_number', 'start_year')

    form = StakeholderDirectoryModelForm

    MenWithMenInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    CriticalEnablerInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    CommunityHealthSystemInline.max_num = 1
    MenWithMenInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    CriticalEnablerInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    CommunityHealthSystemInline.max_num = 1
    OtherQuestionInline.max_num = 1
    EndOfYearQuestionInline.max_num = 1
    GeneralCommentInline.max_num = 1
    
    fieldsets = (
        ('Basic details on the organization', {
            #'classes':('collapse',),
            'fields': ('national_orgnaization_name','organization_name', 'organization_district', 
            'organization_address', 'start_year', 'gps', 'website', 'description_of_organization')
        }),
        ('Contact details', {
            'fields': ('key_contact_name', 'position_within_organization', 'telephone_number', 
            'telephone_number_alternative', 'email_address'),
        }),
        ('Staff details', {
            'fields': ( ('permanent_employee_female', 'permanent_employee_male'), ('temporary_employee_female', 
                'temporary_employee_male'), ('volunteer_employee_female', 'volunteer_employee_male') ),
            'description':('<b><p class="description_fit_in">Employee\'s fall in different groups. Permanent employees \
                are those who is hired to work without any time frame for his/her exit. Temporary employees are those that \
                are hired for a limited period of time. <br/>They are usually hired on a casual, part-time, or full-time \
                basis, but the employment is temporary. Volunteer employees donate their time and energy without receiving \
                financial gain. These employees <br/>usually do not displace any other employee types and usually not \
                entitled to many benefits as compared to other employee types.</p></b>'),
        }),
        ('Organization classification', {
            'fields': ('organization_type', 'organization_target')
        })
    )

    inlines = [GeographicActivityInline, FundingSourceInline, TargetGroupPreventionMessageInline,
        OtherQuestionInline, EndOfYearQuestionInline, GeneralCommentInline]

    class Media:
        css = { "all" : ("css/hide_admin_original.css",) }

class ActivityReportFormAdmin(admin.ModelAdmin):
    list_filter = ('location_province', 'location_district', 'location_ward')
    list_display = ('stake_holder_name', 'location_district', 'quarter_been_reported_on')
    
    AdolencentsInline.max_num = 1
    OutOfSchoolInline.max_num = 1
    SexWorkerInline.max_num = 1
    InmateInline.max_num = 1
    CorrectionalFaciltyStaffInline.max_num = 1
    PersonsWithDisabiltyInline.max_num = 1
    MobileWorkerInline.max_num = 1
    MenWithMenInline.max_num = 1
    CondomProgrammingInline.max_num = 1
    CriticalEnablerInline.max_num = 1
    SynergyDevelopmentSectorInline.max_num = 1
    CommunityHealthSystemInline.max_num = 1
    VulnerablePeopleInline.max_num = 1

    fieldsets = (
        ('Contact details', {
            'fields':('report_date', 'quarter_been_reported_on', 'stake_holder_name', 
            ('location_province', 'location_district', 'location_ward'), ('name', 
            'telephone_number', 'email_address')
            ),
        }),
        ('What types of care and support does your organization provide? (select all that apply)', {
            'fields': ('food_and_nutrition', 'shelter_and_care', 'protection_and_legal_aid', 'healthcare', 
            'psychosocial', 'social_support', 'spiritual_support', 'education_and_vocational_training',
            'economic_strengthening'),
        }),
    )

    inlines = [MaterialInline, AdolencentsInline, OutOfSchoolInline, SexWorkerInline, InmateInline, 
        CorrectionalFaciltyStaffInline, PersonsWithDisabiltyInline, MobileWorkerInline, MenWithMenInline,
        CondomProgrammingInline, CriticalEnablerInline, SynergyDevelopmentSectorInline, CommunityHealthSystemInline, 
        VulnerablePeopleInline]

    class Media:
        css = { "all" : ("css/hide_admin_original.css",) }

class OrganizationTargetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Organization Target', {
            'fields': ('organization_target_option',)
        }),
    )

# Register National Organization models
admin.site.register(NationalOrganization)

# Register StakeHolder models
admin.site.register(StakeholderDirectory, StakeholderDirectoryAdmin)

# Register HIV Activities Organization Participates in
admin.site.register(ActivityReportForm, ActivityReportFormAdmin)

# note: uncomment to have a user be flexible to enter there own targets to the list
admin.site.register(OrganizationTarget)
