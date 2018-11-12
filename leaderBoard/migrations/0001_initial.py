# Generated by Django 2.0.1 on 2018-11-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('team_id', models.CharField(max_length=8)),
                ('color', models.CharField(choices=[('FEKETE', 'Fekete'), ('SARGA', 'Sárga'), ('PIROS', 'Piros'), ('KEK', 'Kék'), ('FEHER', 'Fehér')], max_length=10)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]