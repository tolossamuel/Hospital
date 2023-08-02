from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
class SessionExpiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        last_activity_str = request.session.get('last_activity')
        if last_activity_str:
            last_activity = datetime.strptime(last_activity_str, '%Y-%m-%d %H:%M:%S')
        else:
            last_activity = datetime.now()
        now = datetime.now()
        time_difference = now - last_activity
        if time_difference.total_seconds() > 300:
              request.session['last_activity'] = now.strftime('%Y-%m-%d %H:%M:%S')
              return HttpResponseRedirect("/login/logout")
        if not request.is_ajax():
            request.session['last_activity'] = now.strftime('%Y-%m-%d %H:%M:%S')

        response = self.get_response(request)
        return response
