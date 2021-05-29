from modeltranslation.translator import translator, TranslationOptions

from .models import Category, Movie, Genre, Actor, MovieShots

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Category, CategoryTranslationOptions)
translator.register(Movie, MovieTranslationOptions)
translator.register(Genre, CategoryTranslationOptions)
translator.register(Actor, CategoryTranslationOptions)
translator.register(MovieShots, MovieTranslationOptions)