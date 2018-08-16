from django.contrib import admin

from social_auth.models import SteamUser


@admin.register(SteamUser)
class SteamUserAdmin(admin.ModelAdmin):
    readonly_fields = ('password', 'steamid', 'personaname', 'profileurl', 'avatar', 'avatarmedium', 'avatarfull')
    search_fields = ('steamid', 'personaname')
    list_filter = ('is_superuser',)
    list_display = ('steamid', 'personaname', 'profileurl', 'is_active')
    list_editable = ('is_active',)
