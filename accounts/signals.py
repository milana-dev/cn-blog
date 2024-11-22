from  django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile

"""
post_save - gonderen modelin save olunmasi zamani cagirilir
pre_save = gonderen model save olunmamisdan once cagirilir
post_delete - gonderen modelin silinmesi zamani cagirilir
pre_delete - gonderilenn modeilin obyekti silinmemisden evvel cagirilir

post_migrate - gonderen modelin miqrasiyasi zamani cagirilir 

"""




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)





