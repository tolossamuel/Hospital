# myapp/middleware.py

from django.contrib.auth import logout
from datetime import datetime, timedelta
from django.conf import settings

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity is not None:
                timeout_duration = timedelta(seconds=settings.SESSION_COOKIE_AGE)
                if datetime.now() - datetime.fromisoformat(last_activity) > timeout_duration:
                    logout(request)
                    request.session.flush()

        response = self.get_response(request)

        if request.user.is_authenticated:
            request.session['last_activity'] = datetime.now().isoformat()

        return response
