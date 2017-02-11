from django.db import models
from django.utils import timezone

# Create your models here.
class wygrzewanie(models.Model):
    STATUS_TESTU=(
        ('done','Wygrzany'),
        ("not done","Nie Wygrzany"),
    )
    
    STB_MODEL=(
        ('UHD','UHD'),
        ('WHD','WHD'),  
        ('Dakota', 'DakotaDakota'),  
        ('WHD/UHD','WHD/UHD'),
    )
    
    title=models.CharField(max_length=300)
    titleClass=models.CharField(max_length=300)
    author=models.CharField(max_length=50)
    type_stb=models.CharField(max_length=20,
                              choices=STB_MODEL,
                              default='WHD/UHD' )
    def __str__(self):
        return self.title