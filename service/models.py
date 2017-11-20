from django.db import models

# Create your models here.

class SnippetService(models.Model):
    laundry = 'laundry'
    kitchen = 'kitchen'
    compound = 'compound'
    ironing = 'ironing'
    general = 'general'
    #location details
    jamhuri_phase_1 = 'jamhuri_phase_1'
    jamhuri_phase_2 = 'jamhuri_phase_2'
    karen = 'karen'
    hurligham = 'hurligham'
    kileleshwa = 'kileleshwa'
    lavington = 'lavington'
    service_of_choice = (
        (laundry,'laundry'),
        (kitchen ,'kitchen'),
        (compound ,'compound'),
        (ironing ,'ironing'),
        (general ,'general')
        )
    service_of_choice = models.CharField(max_length=30, choices= service_of_choice,null=True,blank=True)
    hours_choice = models.IntegerField()
    rooms = models.CharField(max_length=6,default=1)
    service_summary = models.TextField(blank=True,null=True)
    full_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    location_of_choice = (
        (jamhuri_phase_1 , 'jamhuri_phase_1'),
        (jamhuri_phase_2 , 'jamhuri_phase_2'),
        (karen ,'karen'),
        (hurligham ,'hurligham'),
        (kileleshwa ,'kileleshwa'),
        (lavington , 'lavington')
        )
    location_of_choice = models.CharField(max_length=30,choices =location_of_choice,null=True,blank=True)
    def __str__(self):
        return self.service_of_choice
    
