# Generated by Django 5.0.6 on 2024-06-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women')], default='men', max_length=5, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telegram_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telegram ID'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=255, verbose_name='Username'),
        ),
    ]