from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.FileField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    client = models.CharField(max_length=255)
    date_project = models.DateField()
    url_project = models.CharField(max_length=255)
    pictures = models.ManyToManyField("portfolio.PictureProject", related_name='pictures_project')

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class PictureProject(models.Model):
    picture = models.FileField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'PictureProject'
        verbose_name_plural = 'PictureProjects'

    def __str__(self):
        return self.picture

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    picture = models.FileField()
    message = models.TextField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name