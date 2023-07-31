# Generated by Django 4.0.2 on 2022-07-05 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='products_category')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='products')),
                ('price', models.IntegerField()),
                ('details', models.TextField()),
                ('is_draft', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('inventory', models.IntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.authorprofile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
