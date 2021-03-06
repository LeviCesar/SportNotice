# Generated by Django 3.1.2 on 2020-10-05 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.TextField(blank=True, verbose_name='Subtitle')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='sports.sports')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ArticleBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=100, verbose_name='Topic')),
                ('text', models.TextField(blank=True, verbose_name='Text')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Image')),
                ('image_author', models.CharField(max_length=100, verbose_name='Image Author')),
                ('image_description', models.CharField(max_length=150, verbose_name='Image Description')),
                ('file', models.FileField(blank=True, upload_to='', verbose_name='File attachment')),
                ('url', models.CharField(blank=True, max_length=150, verbose_name='Link')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_bodies', to='news.article')),
            ],
            options={
                'verbose_name': 'Body',
                'verbose_name_plural': 'Bodies',
            },
        ),
    ]
