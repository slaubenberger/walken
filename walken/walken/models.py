from django.contrib.auth.models import User as DjangoUser
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    imdb_id = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name

    def rating(self):
        rating_sum = self.ratings.aggregate(models.Sum('rating'))
        return rating_sum['rating__sum'] / self.ratings.count()


class File(models.Model):
    movie = models.ForeignKey('walken.Movie')
    user = models.ForeignKey('walken.User')
    path = models.TextField()
    desc = models.TextField(null=True)

    def __unicode__(self):
        return self.path


class User(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s' % (self.name)


class Rating(models.Model):
    movie = models.ForeignKey('walken.Movie', related_name="ratings")
    user = models.ForeignKey('walken.User')
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=False, null=True)

    def __unicode__(self):
        return u'%s - %s - %s' % (self.movie, self.user, self.rating)
