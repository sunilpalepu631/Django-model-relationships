# Generated by Django 5.0.1 on 2024-01-26 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='myapp.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
