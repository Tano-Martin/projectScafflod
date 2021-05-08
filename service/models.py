from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=255)

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

class Faq(models.Model):
    question = models.CharField(max_length=255)
    reponse = models.TextField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'

    def __str__(self):
        return self.question

class Benefit(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.FileField()

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Benefit'
        verbose_name_plural = 'Benefits'

    def __str__(self):
        return self.title

class Pack(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    period = models.CharField(max_length=255)
    label = models.BooleanField(default=False)
    title_label = models.CharField(max_length=255)
    activate = models.BooleanField(default=False)

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Pack'
        verbose_name_plural = 'Packs'

    def __str__(self):
        return self.title

class Advantage(models.Model):
    label = models.CharField(max_length=255)
    label_activate = models.BooleanField(default=True)
    pack = models.ManyToManyField("service.Pack", related_name="advantage_pack")

        # Champs obligatoires (Convention de NaN)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Advantage'
        verbose_name_plural = 'Advantages'

    def __str__(self):
        return self.label