# Generated by Django 4.0.5 on 2022-07-04 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='sub',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
