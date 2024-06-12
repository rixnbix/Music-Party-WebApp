from django.db import models
import string
import random


def generate_unique_code():
    length = 6
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) # Concatanates 6 random uppercase alphabets
        if Room.objects.filter(code=code).count() == 0: # Checks if any of the objects of Room have the same code 
            break
        
    return code    
        

# Create your models here.

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True) # Unique code for room
    host = models.CharField(max_length=50, unique=True) # Room can have atmost 1 host
    guest_can_pause = models.BooleanField(null=False, default=False) # Permission for guest to pause
    votes_to_skip = models.IntegerField(null=False, default=1) # Votes to skip song
    created_at = models.DateTimeField(auto_now_add=True) # Date and time when created
    