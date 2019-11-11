from django.db import models
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.text import slugify


class Match(models.Model):
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)
    score = models.CharField(max_length=10, null=True)
    datetime = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.home_team + ' ' + (self.score if self.score else ':') + ' ' + self.away_team

    def get_absolute_url(self):
        return reverse('match-detail', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        slug = slugify(f'{self.home_team}-{self.away_team}-{self.datetime.strftime("%Y%m%d")}')
        unique_slug = slug
        num = 1
        while Match.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class VideoGoal(models.Model):
    permalink = models.CharField(max_length=255, unique=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    url = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=200, null=True)
    minute = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title
