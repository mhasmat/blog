from django.contrib import admin
from .models import Post, Comentario, Categoria

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Categoria)