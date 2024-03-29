# Generated by Django 3.2.4 on 2021-07-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_uservote_mat_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('count', models.IntegerField(default=0, null=True)),
                ('position', models.CharField(max_length=500, null=True)),
                ('is_count', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
