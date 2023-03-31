from datetime import datetime
from random import randrange
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save)
def get_number(**kwargs):
    num = randrange(1000000, 9999999)
    return num