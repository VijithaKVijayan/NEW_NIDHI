# Generated by Django 4.0.1 on 2022-04-10 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=222)),
                ('Password', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=222)),
                ('Password', models.CharField(max_length=120)),
                ('Canvassed_by', models.CharField(max_length=120)),
                ('Customer_name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='uploads/')),
                ('Signature', models.ImageField(upload_to='uploads/')),
                ('Pancard_no', models.CharField(max_length=200)),
                ('Adarcard_no', models.CharField(max_length=200)),
                ('Date_of_Birth', models.CharField(max_length=200)),
                ('Mobile_no', models.CharField(max_length=200)),
                ('Mobile_number1', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Occupation', models.CharField(max_length=200)),
                ('Annual_income', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('Nominee_name', models.CharField(max_length=200)),
                ('Nominee_relation', models.CharField(max_length=200)),
                ('Customer_status', models.CharField(max_length=200)),
                ('Customer_Plan', models.CharField(choices=[('Silver Plan', 'Silver Plan'), ('Diamond Plan', 'Diamond Plan'), ('Golden Plan', 'Golden Plan'), ('Royal Plan', 'Royal Plan')], max_length=200)),
                ('Deposit_Amount', models.IntegerField(blank=True)),
                ('Deposit_Year', models.IntegerField(blank=True)),
                ('Anuval_stypend', models.FloatField(blank=True)),
                ('Status', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=200)),
                ('Employee_code', models.CharField(max_length=200)),
                ('Employee_photo', models.ImageField(upload_to='uploads/')),
                ('Adharcard', models.FileField(upload_to='uploads/')),
                ('Adhar_number', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Department', models.CharField(max_length=200)),
                ('Designation', models.CharField(max_length=200)),
                ('Branch', models.CharField(max_length=200)),
                ('Employee_status', models.CharField(max_length=200)),
                ('Date_of_joining', models.DateField()),
                ('Reporting_to', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Guardian_name', models.CharField(max_length=200)),
                ('Date_of_birth', models.DateField(blank=True)),
                ('Email', models.CharField(max_length=200)),
                ('Office_phno', models.CharField(max_length=200)),
                ('Emergency_phno', models.CharField(max_length=200)),
                ('Address_pa', models.CharField(max_length=200)),
                ('Address_ps', models.CharField(max_length=200)),
                ('Qualification', models.CharField(max_length=200)),
                ('Blood_Group', models.CharField(max_length=200)),
                ('Date_of_resign', models.DateField(blank=True)),
                ('Reason_of_Resign', models.CharField(max_length=200)),
                ('Basic_pay', models.CharField(max_length=200)),
                ('Daaily_Allowance', models.CharField(max_length=200)),
                ('Other_allowance', models.CharField(max_length=200)),
                ('Bank_name', models.CharField(max_length=200)),
                ('Account_number', models.CharField(max_length=200)),
                ('Ifsc_code', models.CharField(max_length=200)),
                ('Esi_no', models.CharField(max_length=200)),
                ('Pf_no', models.CharField(max_length=200)),
                ('Welfare_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LevelOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=222)),
                ('Password', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='LevelThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=222)),
                ('Password', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='LevelTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=222)),
                ('Password', models.CharField(max_length=120)),
            ],
        ),
    ]
