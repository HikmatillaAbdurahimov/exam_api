# Generated by Django 5.1 on 2024-08-19 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='coursemodul',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='studentcomment',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['id'], name='api_course_id_fc19fc_idx'),
        ),
        migrations.AddIndex(
            model_name='coursemodul',
            index=models.Index(fields=['id'], name='api_coursem_id_f2049d_idx'),
        ),
        migrations.AddIndex(
            model_name='questions',
            index=models.Index(fields=['id'], name='api_questio_id_07352f_idx'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['id'], name='api_student_id_887aa7_idx'),
        ),
        migrations.AddIndex(
            model_name='studentcomment',
            index=models.Index(fields=['id'], name='api_student_id_823c27_idx'),
        ),
        migrations.AddIndex(
            model_name='teacher',
            index=models.Index(fields=['id'], name='api_teacher_id_7c2829_idx'),
        ),
    ]
