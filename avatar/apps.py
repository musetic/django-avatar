from django.apps import AppConfig
from django.conf import settings

from PIL import Image


class AvatarAppConfig(AppConfig):
    name = 'avatar'
    verbose_name = 'Avatars'


class AvatarSettings(object):
    AVATAR_DEFAULT_SIZE = 80
    AVATAR_LARGER_SIZE = 200
    AVATAR_RESIZE_METHOD = Image.ANTIALIAS
    AVATAR_STORAGE_DIR = 'avatars'
    AVATAR_DEFAULT_URL = 'musetic/img/avatars/default-avatar.png'
    AVATAR_MAX_SIZE = 1024 * 1024
    AVATAR_THUMB_FORMAT = 'JPEG'
    AVATAR_THUMB_QUALITY = 85
    AVATAR_HASH_FILENAMES = True
    AVATAR_HASH_USERDIRNAMES = True
    AVATAR_ALLOWED_FILE_EXTS = ('JPEG', 'PNG',)
    AVATAR_CACHE_TIMEOUT = 60 * 60
    AVATAR_STORAGE = settings.DEFAULT_FILE_STORAGE
    AVATAR_CLEANUP_DELETED = False
    AVATAR_AUTO_GENERATE_SIZES = (80, 200,)

    def configure_auto_generate_avatar_sizes(self, value):
        return value or getattr(settings, 'AUTO_GENERATE_AVATAR_SIZES',
                                (self.AVATAR_DEFAULT_SIZE, self.AVATAR_LARGER_SIZE,))
