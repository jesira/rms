# Generated by Django 3.1.4 on 2020-12-29 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(choices=[('201132', '201132'), ('301132', '301132'), ('401132', '401132'), ('501132', '501132'), ('601132', '601132')], max_length=200, null=True)),
                ('course_id', models.CharField(choices=[('IIT01', 'IIT01'), ('IIT02', 'IIT02'), ('IIT03', 'IIT03')], max_length=200, null=True)),
                ('class_test_mark', models.FloatField(null=True)),
                ('final_mark', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]