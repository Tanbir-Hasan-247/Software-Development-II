# Generated by Django 5.1.4 on 2024-12-29 14:23

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobPost', '0005_remove_jobpost_last_date_to_apply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contract', 'Contract'), ('Internship', 'Internship'), ('On-Site', 'On-Site'), ('Remote', 'Remote')], max_length=54),
        ),
    ]
