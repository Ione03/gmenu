# Generated by Django 3.2.5 on 2021-07-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={},
        ),
        migrations.RemoveField(
            model_name='menu',
            name='is_admin_menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='kinds',
            field=models.CharField(blank=True, choices=[('frontend_unlogin', 'Frontend Unlogin'), ('frontend_login', 'Frontend Login'), ('backend_login', 'Backend Login')], default='frontend_unlogin', max_length=20),
        ),
    ]
