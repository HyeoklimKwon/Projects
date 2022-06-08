from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer
from django.http.response import JsonResponse

User = get_user_model()

@api_view(['GET'])
def profile(request, username):    
    person = get_object_or_404(get_user_model(), username=username)
        # Set your variables here
    # email = person.email
    # email_hash = hashlib.md5(request.user.email.encode('utf-8').strip().lower()).hexdigest() #gravatar hash 
    context ={
        'username': person.username,
        'email': person.email,
        'created_at': person.date_joined,
        'followers':person.followers.count(),
        'followings':person.followings.count(),
        # 'email_hash':email_hash,
    }
    return JsonResponse(context)
    
@api_view(['POST'])
def follow(request, username):

    person = get_object_or_404(get_user_model(), username=username)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            follow = True
        else:
            person.followers.add(user)
            follow = False
        follow_status ={
            'follow':follow,
            'count':person.followers.count(),
        }
        return JsonResponse(follow_status)
    