# Generated by Django 4.2.2 on 2023-12-03 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bestfriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_company', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100, null=True)),
                ('date_of_joining', models.DateField(null=True)),
                ('bestfriend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.bestfriends')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.location')),
            ],
        ),
    ]