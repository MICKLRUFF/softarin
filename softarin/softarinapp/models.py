from django.db import models

class Services(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services_images/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class ServicesImages(models.Model):
    services_item = models.ForeignKey(Services, related_name='services_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='services_images/')

    def __str__(self):
        return f"Image for {self.services_item.name}" 
    
class ServicesDescript2(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    services_item = models.ForeignKey(Services, related_name='services_description', on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Description for {self.services_item.name}"
    

class Projects(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects_images/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Stages(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='stages_images/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class AboutDescription(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services_images/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Feedback(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects_images/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    contact_name = models.CharField(max_length=255, db_index=True)
    contact_phone = models.CharField(max_length=255, db_index=True)
    contact_email = models.CharField(max_length=255, db_index=True)
    time_create = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name