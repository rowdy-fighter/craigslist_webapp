# Generated by Django 3.0.1 on 2020-01-09 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20200108_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Search',
            new_name='volume',
        ),
        migrations.AlterModelOptions(
            name='volume',
            options={'verbose_name_plural': 'Volume'},
        ),
    ]