from django.core.files.storage import FileSystemStorage


class MediaStorage(FileSystemStorage):
    file_overwrite = False


class DocumentStorage(FileSystemStorage):
    file_overwrite = False


class ImageSettingStorage(FileSystemStorage):
    file_overwrite = False
