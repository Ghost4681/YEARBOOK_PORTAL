# Generated by Django 4.0.5 on 2022-07-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybapp', '0002_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]