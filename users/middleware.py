import json
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.utils.deprecation import MiddlewareMixin


class UserAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.user_info = None
        session_key = request.COOKIES.get("session_key")
        if session_key and Session.objects.filter(session_key=session_key).exists():
            session = Session.objects.get(session_key=session_key)
            if session.expire_date >= timezone.now():
                user_info = json.loads(session.session_data)
                request.user_info = user_info
