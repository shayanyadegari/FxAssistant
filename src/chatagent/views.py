from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ChatSession, ChatMessage
from .openai_utils import get_ai_response

def create_session(request):
    """
    Create a new ChatSession and redirect user to some 'chat' page.
    """
    session = ChatSession.objects.create(user=request.user if request.user.is_authenticated else None)
    return redirect('view_chat', session_id=session.pk)

def view_chat(request, session_id):
    session = get_object_or_404(ChatSession, pk=session_id)
    messages = session.messages.order_by('created_at')

    # Fetch all sessions for the sidebar
    all_sessions = ChatSession.objects.order_by('-created_at')

    return render(request, 'chatagent/chat.html', {
        'session': session,
        'messages': messages,
        'all_sessions': all_sessions,
    })

# chatagent/views.py


def post_message(request, session_id):
    if request.method == "POST":
        session = get_object_or_404(ChatSession, pk=session_id)
        user_text = request.POST.get('message', '')

        # 1. Store user message
        user_msg = ChatMessage.objects.create(
            session=session,
            role='user',
            content=user_text
        )

        # 2. Get AI response
        ai_reply = get_ai_response(session)

        # 3. Store AI response
        assistant_msg = ChatMessage.objects.create(
            session=session,
            role='assistant',
            content=ai_reply
        )

        # 4. Return partial HTML for these 2 new messages
        #    We'll render a small template snippet containing
        #    both the user bubble + assistant bubble
        new_messages = [user_msg, assistant_msg]
        return render(request, 'chatagent/_new_messages.html', {
            'messages': new_messages
        })

    return redirect('view_chat', session_id=session_id)
