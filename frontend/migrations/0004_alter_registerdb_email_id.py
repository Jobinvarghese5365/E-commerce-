# Generated by Django 4.2.6 on 2023-12-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_rename_email_registerdb_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdb',
            name='email_id',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
