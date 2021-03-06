# Generated by Django 3.1.5 on 2021-01-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210119_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('S', 'Science'), ('f', 'Fiction')], help_text='Enter a book genre (e.g. science, fiction)', max_length=200),
        ),
    ]
