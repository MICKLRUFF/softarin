# Generated by Django 5.0.7 on 2024-11-10 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softarinapp', '0002_aboutdescription_description_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesDescript2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('name_en', models.CharField(db_index=True, max_length=255, null=True)),
                ('name_uk', models.CharField(db_index=True, max_length=255, null=True)),
                ('name_es', models.CharField(db_index=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
                ('description_es', models.TextField(blank=True, null=True)),
                ('services_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_description', to='softarinapp.services')),
            ],
        ),
        migrations.DeleteModel(
            name='ServicesDescript',
        ),
    ]