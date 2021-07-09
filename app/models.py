from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserVote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mat_no = models.CharField(max_length=150 )
    voters_id = models.CharField(max_length=200, blank=False)
    is_voted = models.BooleanField(null=False, default=False)
   


    def __str__(self):
        return self.mat_no

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        UserVote.objects.create(user=instance)
    instance.uservote.save()

class Candidates(models.Model):
    name = models.CharField(null=True, max_length=200)
    count = models.IntegerField(null=True, default=0)
    position = models.CharField(null=True , max_length=500)
    is_count = models.BooleanField(default=False , null=True)

    def __str__(self):
        return self.name
   