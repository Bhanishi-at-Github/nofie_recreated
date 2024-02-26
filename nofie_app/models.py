from django.db import models

# Create your models here.


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default='Computer Science')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(BaseModel):
    
    semester = models.IntegerField()
    roll_no = models.IntegerField(unique=True, null=False, blank=False)
    
    # image = models.ImageField(upload_to='nofie_images')

    def __str__(self):
        return self.name
    

class Teacher(BaseModel):
    

    # image = models.ImageField(upload_to='nofie_images')
    


    def __str__(self):
        return self.name
    
class Notes(models.Model):
    
    title = models.CharField(
        max_length=100, 
        default='Untitled', 
        null=False,
        blank=False)
    
    description = models.TextField(default='No Description')
    subject = models.CharField(max_length=100)
    semester = models.IntegerField(default=1)
    code = models.CharField(max_length=100)
    file = models.FileField(upload_to='nofie_files')

    def __str__(self):
        return self.name
