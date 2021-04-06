from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PrivateMediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    file_overwrite = False

    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(PrivateMediaStorage, self)._save(name, content)
