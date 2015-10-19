from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from app import config


def content_file_name(instance, filename):
    return 'avatars/' + str(instance.user.pk)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.TextField(max_length=256)
    fullname = models.TextField(max_length=256, blank=True)
    about = models.TextField(max_length=1024, blank=True)
    avatar = models.ImageField("Avatar", upload_to=content_file_name, blank=True, null=True)

    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')

    hour_start = models.IntegerField(default=config.DEFAULT_TIME_START,
                                     validators=[MaxValueValidator(23), MinValueValidator(0)])
    hour_span = models.IntegerField(default=config.DEFAULT_TIME_SPAN,
                                    validators=[MinValueValidator(1), MaxValueValidator(config.MAX_TIME_SPAN)])

    def __unicode__(self):
        return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
