# Generated by Django 3.2 on 2021-05-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_about_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter',
            field=models.URLField(),
        ),
    ]