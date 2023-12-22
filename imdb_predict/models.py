from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import datetime
# Create your models here.

def change_file_name_totime(instance,filename):
    str_date = datetime.now().strftime("%Y%m%d%H%M%S")
    extention = filename.split('.')[-1]
    
    full_name=filename.split('.')[-2]+'-'+str_date+'.'+extention
    return f'csv_files/{full_name}'



class File(models.Model):
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to=change_file_name_totime,validators=[FileExtensionValidator(allowed_extensions=['csv'])],)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name