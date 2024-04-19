from django.conf import settings

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage

    class MediaStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'

else:
    from storages.backends.s3boto3 import S3Boto3Storage

    class MediaStorage(S3Boto3Storage):
        bucket_name = settings.MEDIA_LOCATION
        location = 'media'
        file_overwrite = False
        default_acl = 'public-read'