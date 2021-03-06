# Generated by Django 3.0.6 on 2020-06-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('High', 'HIGH'), ('Mid', 'MIDIUM'), ('Low', 'LOW')], default='Low', max_length=7)),
            ],
        ),
    ]
