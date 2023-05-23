# Generated by Django 4.2 on 2023-05-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('answer', models.CharField(max_length=10, null=True)),
                ('result', models.CharField(max_length=10)),
                ('is_correct', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
