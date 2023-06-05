import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_otp.oath import totp
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    phone_number = PhoneNumberField(null=True, blank=True)
    email = models.CharField(max_length=255)
    is_verified_email = models.BooleanField(default=False)


class AuthToken(models.Model):
    user = models.OneToOneField(to="auth.User", on_delete=models.CASCADE, verbose_name=_("user"))
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # In test mode, always return TEST_TOKEN
        self.token = settings.TEST_TOKEN if settings.ENABLE_TEST else totp(key=self.generate_key(), digits=6)

        return super().save(force_insert=force_insert, force_update=force_update, using=using,
                            update_fields=update_fields)

    @staticmethod
    def generate_key():
        return binascii.hexlify(os.urandom(20))

    class Meta:
        verbose_name = _("authentication token")
        verbose_name_plural = _("authentication tokens")

    def __str__(self):
        return str(self.user)
