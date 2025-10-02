from django.contrib import admin
from .models import Artist, Album, Track


# admin.register(Artist)
# admin.register(Album)
# admin.register(Track)

class TrackInline(admin.TabularInline):  # Можно заменить на StackedInline
    model = Track
    extra = 1  # Количество пустых форм по умолчанию
    fields = ('title', 'genre')
    show_change_link = True  # Ссылка для перехода на редактирование трека отдельно


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')
    search_fields = ('title', 'artist__name')
    list_filter = ('release_date',)
    ordering = ('release_date',)
    inlines = [TrackInline]  # Добавляем треки прямо в альбом


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'genre')
    search_fields = ('title', 'album', 'genre')
    list_filter = ('genre', 'created_at')
    ordering = ('title',)


