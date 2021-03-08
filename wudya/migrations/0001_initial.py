# Generated by Django 3.1.7 on 2021-03-04 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=200)),
                ('votes_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OptionPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes_a', models.IntegerField(default=0)),
                ('votes_b', models.IntegerField(default=0)),
                ('prompt_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prompt_a', to='wudya.option')),
                ('prompt_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prompt_b', to='wudya.option')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='other',
            field=models.ManyToManyField(through='wudya.OptionPair', to='wudya.Option'),
        ),
    ]
