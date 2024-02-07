from django.db import models

class UserDetail(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    RELIGION_CHOICES = [
        ('B', 'Buddhism'),
        ('C', 'Christianity'),
        ('I', 'Islam'),
        ('H', 'Hinduism'),
        ('O', 'Other'),
    ]
    id_card_number = models.CharField(max_length=13, unique=True)
    frist_name_en = models.CharField(max_length=255)
    last_name_en = models.CharField(max_length=255)
    frist_name_th = models.CharField(max_length=255)
    last_name_th = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=1, choices=RELIGION_CHOICES)    
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_issue = models.DateTimeField()
    date_of_expiry = models.DateTimeField()
    profile_image = models.BinaryField(blank=True, null=True)

    
