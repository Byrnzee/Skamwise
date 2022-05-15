from django.contrib import admin, sites
#from .models import Home

# Register your models here.

#admin.site.register(Home)

from django.contrib import admin
from .models import Post  # New
# Register your models here.
admin.site.register(Post)  # New