from __future__ import unicode_literals
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.
class Index(models.Model):
    service = models.CharField(max_length=30,default="General cleaning")
    # context =models.TextField()
    timestamp = models. DateTimeField(default=datetime.datetime.now)
    picture = models.ImageField(default='default.png')
    
class About(models.Model):
    
    service = models.CharField(max_length=30)
    # context =models.TextField()
    timestamp = models. DateTimeField(default=datetime.datetime.now)
    

    
class Service(models.Model):
    Name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70,blank=True)
    location = models.CharField(max_length=30)
    service = models.CharField(max_length=50)
    # cleaning =models.CharField(max_length=30,choices=cleaning_options)
    
    # Phonenumber = models.CharField()
    
    timestamp = models. DateTimeField(auto_now_add=True, blank=True)
    
class Contact(models.Model):
    user = models.ForeignKey(User, null=True)
    phonenumber = models.CharField(max_length=15, null=True)
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.user.email
 


class Snippet(models.Model):
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
    
