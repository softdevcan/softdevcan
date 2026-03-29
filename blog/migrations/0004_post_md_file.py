from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_blog_post_publish_idx_blog_post_publish_a3f863_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='md_file',
            field=models.FileField(
                blank=True,
                null=True,
                upload_to='blog_md/',
                verbose_name='Markdown File',
                help_text='Upload a .md file to auto-populate content. Re-upload to update content.',
            ),
        ),
    ]
