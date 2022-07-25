from re import S
from django.db import models
from users.models import Profile
from django.urls import reverse


class Post(models.Model):

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=300)
    body = models.TextField()
    id = models.BigAutoField(primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(
        default='c2.jpg',
        null=True,
        blank=True,
        upload_to='')

    tags = models.ManyToManyField('Tag', blank=True)
    slug = models.SlugField(max_length=300, null=True, blank=True, unique=True)

    @property
    def reading_time(self):
        word_count = len(self.body.split())
        time = word_count / 200
        round_time = round(time)
        if time < 1:
            time = "1 second"

        else:
            time = f"{round_time} minute"

        return time

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    id = models.BigAutoField(primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
