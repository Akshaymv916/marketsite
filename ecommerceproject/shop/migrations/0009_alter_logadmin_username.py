# Generated by Django 4.2.3 on 2023-09-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_logadmin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logadmin',
            name='username',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
    ]
