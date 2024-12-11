from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from users.models import User
from .models import Message
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def chat_view(request, user_id):
    # Obtenir l'utilisateur avec qui discuter
    recipient = get_object_or_404(User, pk=user_id)

    # Affichage des messages
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        # Validation avant d'envoyer un message
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, recipient=recipient, content=content)
            return redirect('chat:chat_view', user_id=user_id)

    return render(request, 'chat/chat.html', {'messages': messages, 'recipient': recipient})


@login_required
def inbox(request):
    messages = Message.get_user_inbox(request.user)
    return render(request, 'chat/inbox.html', {'messages': messages})


def view_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    
    # Vérifie que l'utilisateur est le destinataire
    if request.user == message.recipient:
        message.mark_as_read()  # Marquer comme lu

    return render(request, 'chat/message_detail.html', {'message': message})
