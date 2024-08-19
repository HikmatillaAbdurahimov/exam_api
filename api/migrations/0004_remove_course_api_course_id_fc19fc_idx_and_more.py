# Generated by Django 5.1 on 2024-08-19 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_student_image'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='course',
            name='api_course_id_fc19fc_idx',
        ),
        migrations.RemoveIndex(
            model_name='coursemodul',
            name='api_coursem_id_f2049d_idx',
        ),
        migrations.RemoveIndex(
            model_name='questions',
            name='api_questio_id_07352f_idx',
        ),
        migrations.RemoveIndex(
            model_name='student',
            name='api_student_id_887aa7_idx',
        ),
        migrations.RemoveIndex(
            model_name='studentcomment',
            name='api_student_id_823c27_idx',
        ),
        migrations.RemoveIndex(
            model_name='teacher',
            name='api_teacher_id_7c2829_idx',
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursemodul',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentcomment',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='status',
            field=models.CharField(choices=[('ju', 'Junior'), ('mi', 'Middle')], default='ju', max_length=5),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['id', 'course_name', 'price'], name='api_course_id_7e1264_idx'),
        ),
        migrations.AddIndex(
            model_name='coursemodul',
            index=models.Index(fields=['id', 'course_module_name'], name='api_coursem_id_1f446b_idx'),
        ),
        migrations.AddIndex(
            model_name='questions',
            index=models.Index(fields=['id', 'questions'], name='api_questio_id_3af8d4_idx'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['id', 'first_name', 'last_name'], name='api_student_id_22f192_idx'),
        ),
        migrations.AddIndex(
            model_name='studentcomment',
            index=models.Index(fields=['id', 'comment'], name='api_student_id_b596c9_idx'),
        ),
        migrations.AddIndex(
            model_name='teacher',
            index=models.Index(fields=['id', 'first_name', 'last_name'], name='api_teacher_id_1b8dce_idx'),
        ),
    ]