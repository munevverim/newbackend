from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CustomUser

@receiver(user_logged_in, sender=User)
def set_initial_credit(sender, user, request, **kwargs):
    custom_user, created = CustomUser.objects.get_or_create(id=user.id, password=user.password, email=user.email, username=user.username, defaults={'credit': 200, 't1':'', 't2':'', 't3':'', 't4':'', 't5':'', 'c1': {"width": 768, "height": 768, 'lastLayerCounter': 0, "objects": []}, 'c2': {"width": 768,"height": 768, 'lastLayerCounter': 0,"objects": []}, 'c3': {"width": 768,"height": 768, 'lastLayerCounter': 0,"objects": []}, 'c4': {"width": 768,"height": 768, 'lastLayerCounter': 0,"objects": []}, 'c5': {"width": 768,"height": 768, 'lastLayerCounter': 0,"objects": []}})
    if created:
        custom_user.save()