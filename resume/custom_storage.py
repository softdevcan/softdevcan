from django.conf import settings

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage

    class MediaStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'

    class DocumentStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'

    class ImageStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'

else:
    from storages.backends.s3boto3 import S3Boto3Storage

    class MediaStorage(S3Boto3Storage):
        bucket_name = settings.MEDIA_LOCATION
        location = 'media'
        file_overwrite = False
        default_acl = 'public-read'

    class DocumentStorage(S3Boto3Storage):
        location = settings.DOCUMENT_LOCATION
        file_overwrite = False
        default_acl = 'public-read'

    class ImageStorage(S3Boto3Storage):
        location = settings.IMAGES_SETTINGS_LOCATION
        file_overwrite = False
        default_acl = 'public-read'