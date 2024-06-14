# Generated by Django 4.2.3 on 2023-08-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst_task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.CharField(blank=True, max_length=29, null=True)),
                ('domain', models.CharField(blank=True, max_length=100, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('area', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='myfile',
        ),
    ]
