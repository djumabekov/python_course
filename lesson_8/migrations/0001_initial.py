# Generated by Django 3.2.8 on 2021-11-04 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('platform', models.CharField(max_length=64)),
                ('year', models.DateField()),
                ('genre', models.CharField(max_length=64)),
                ('publisher', models.CharField(max_length=64)),
                ('na_sales', models.FloatField()),
                ('eu_sales', models.FloatField()),
                ('jp_sales', models.FloatField()),
                ('other_sales', models.FloatField()),
                ('global_sales', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GamerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GamerLibraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('game', models.ManyToManyField(to='lesson_8.GameModel')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson_8.gamermodel')),
            ],
        ),
    ]
