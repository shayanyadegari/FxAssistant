from django.contrib import admin
from .models import ChatMessage,ChatSession

class SessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

class ChatAdmin(admin.ModelAdmin):
    list_display = ('session', 'role', 'content', 'created_at')


admin.site.register(ChatMessage, ChatAdmin)
admin.site.register(ChatSession, SessionAdmin)