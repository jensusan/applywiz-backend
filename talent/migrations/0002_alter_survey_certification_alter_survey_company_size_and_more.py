# Generated by Django 4.0.3 on 2022-03-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='certification',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='company_size',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='disability',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='education',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='expected_salary',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='languages',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='role_important',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='role_level',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='role_time',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='specific_industry',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='sponsorship',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='start_date',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='veteran',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='email',
            field=models.EmailField(max_length=100, null=b'I01\n', unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='first_name',
            field=models.CharField(max_length=30, null=b'I01\n', verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='last_name',
            field=models.CharField(max_length=30, null=b'I01\n', verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='phone_number',
            field=models.CharField(max_length=15, null=b'I01\n', verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='survey',
            field=models.ForeignKey(blank=True, null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to='talent.survey'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=b'I01\n', verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='talent',
            name='zip_code',
            field=models.CharField(blank=True, max_length=15, null=b'I01\n', verbose_name='Zipe Code'),
        ),
    ]