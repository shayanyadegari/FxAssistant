from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatSession(models.Model):
    """
    Represents one conversation or chat session. 
    You could link this to a specific user, 
    or leave it anonymous if your use case doesn't require auth.
    """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Helpful in admin/debugging
        return f"ChatSession {self.pk} (user={self.user})"


class ChatMessage(models.Model):
    """
    Stores a single message in a session. 
    role: 'user' or 'assistant' or 'system'
    """
    ROLE_CHOICES = [
        ('system', 'System'),
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]

    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} - {self.content[:30]}..."
