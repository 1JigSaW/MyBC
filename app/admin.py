from django.contrib import admin
from .models import Courses, Books, Videos, Articles
from .models import WantCourses, WantBooks, WantVideos, WantArticles

admin.site.register(Courses)
admin.site.register(Books)
admin.site.register(Videos)
admin.site.register(Articles)
admin.site.register(WantCourses)
admin.site.register(WantBooks)
admin.site.register(WantVideos)
admin.site.register(WantArticles)
