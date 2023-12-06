# Generated by Django 4.2.8 on 2023-12-05 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_code', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=30)),
                ('dept_chief', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=30)),
                ('student_dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.department')),
            ],
        ),
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField()),
                ('amount', models.IntegerField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.student')),
            ],
        ),
    ]