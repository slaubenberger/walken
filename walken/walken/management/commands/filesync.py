from walken.models import Movie, File, User, Rating

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from requests.exceptions import ConnectionError

import tmdb
#import imdb

import os
import re

FILE_ENDINGS = (
                '.avi',
                '.mpg',
                '.m2ts',
                '.mkv',
                )


class Command(BaseCommand):
    args = ''
    help = 'Synchronizes the specified movie folders with walken database.'

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(name='Stefan')
        tmoviedb_user, created = User.objects.get_or_create(name='The Movie Database')
        tmdb.configure(settings.MOVIE_API_KEY)

        counter = 0
        for dirpath, dirnames, filenames in os.walk('/Volumes/NAS_public/video/movies'):
            for filename in filenames:
                try:
                    if filename.endswith(FILE_ENDINGS):
                        path = ('%s/%s' % (dirpath, filename)).replace('//', '/')
                        
                        # handle file only case
                        name = filename

                        # handle 0000n.m2ts case
                        if name[:4] == '0000':
                            dirs = dirpath.split('/')
                            name = dirs[-3]
                        
                        # remove fileendings
                        for ending in FILE_ENDINGS:
                            name = name.replace(ending, '') 
                        
                        # remove (..) stuff
                        desc = re.search(r'\(.*\)', name)
                        if desc:
                            desc = desc.group().replace('(', '').replace(')', '')
                        name = re.sub(r'\(.*\)', '', name)    
                        
                        # get more movie data
                        try:
                            tmovie = tmdb.Movie(name)
                        except (ValueError, requests.exceptions.ConnectionError), e:
                            print 'GIVE UP %s' % name
                            continue

                        # try to get original name
                        try:
                            name = tmovie.get_original_title()
                        except IndexError, e:
                            pass

                        # try to get original name
                        try:
                            movie_id = tmovie.get_id()
                            imdb_id = tmovie.get_imdb_id(movie_id)
                        except IndexError, e:
                            imdb_id = None

                        # create movie, if not exists
                        movie, created = Movie.objects.get_or_create(name=name, imdb_id=imdb_id)
                        print name

                        # create file object
                        fil, created = File.objects.get_or_create(path=path, user=user, movie=movie)
                        fil.desc = desc
                        fil.save()

                        # try to get vote average
                        try:
                            movie_id = tmovie.get_id()
                            vote_average = tmovie.get_vote_average(movie_id)
                            rating, created = Rating.objects.get_or_create(movie=movie, user=tmoviedb_user)
                            rating.rating = "%s" % vote_average
                            rating.save()
                        except IndexError, e:
                            pass

                        # # asdfasdf
                        # i = imdb.IMDb(accessSystem='http')
                        # # movie_list is a list of Movie objects, with only attributes like 'title'
                        # # and 'year' defined.
                        # movie_list = i.search_movie(name)
                        # # the first movie in the list.
                        # first_match = movie_list[0]

                        # print first_match

                        # # only basic information like the title will be printed.
                        # print first_match.summary()
                        # # update the information for this movie.
                        # i.update(first_match)
                        # # a lot of information will be printed!
                        # print first_match.summary()
                        # # retrieve trivia information and print it.
                        # i.update(first_match, 'trivia')
                        # print m['trivia']
                        # # retrieve both 'quotes' and 'goofs' information (with a list or tuple)
                        # i.update(m, ['quotes', 'goofs'])
                        # print m['quotes']
                        # print m['goofs']
                        # # retrieve every available information.
                        # i.update(m, 'all')

                        counter += 1
                except Exception, e:
                    print "GARNICHTGUT", filename
        self.stdout.write('Successfully synchronized %s files and %s movies.' % (counter, Movie.objects.count()))
