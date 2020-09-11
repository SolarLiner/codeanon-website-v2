# Generated by Django 2.2.16 on 2020-09-06 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(verbose_name='Post date')),
                ('intro', models.CharField(max_length=250)),
                ('content', wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock()), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('cpp', 'C++'), ('c', 'C'), ('java', 'Java'), ('ocaml', 'OCaml'), ('haskell', 'Haskell'), ('rust', 'Rust'), ('python3', 'Python 3'), ('bash', 'Bash/Shell'), ('javascript', 'Javascript'), ('css', 'CSS'), ('html', 'HTML'), ('julia', 'Julia'), ('nginx', 'Nginx configuration file'), ('numpy', 'NumPy'), ('django', 'Django'), ('jinja', 'Jinja'), ('docker', 'Docker'), ('jinja', 'Jinja'), ('yaml', 'YAML'), ('json', 'JSON'), ('plpgsql', 'PL/pgSQL'), ('psql', 'PostgreSQL console (psql)')], null=False)), ('caption', wagtail.core.blocks.CharBlock(blank=True, nullable=True, required=False)), ('src', wagtail.core.blocks.TextBlock())]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='blog.BlogPage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
