from rest_framework.response import Response
from rest_framework.views import APIView
import datetime

class SimpleAPIView(APIView):
    def get(self, request):
        track = request.GET.get('track')
        name = request.GET.get('slack_name')
        utc_date = datetime.datetime.utcnow()
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        current_day = weekdays[datetime.datetime.now().weekday()]
        payload = {
            'slack_name' : name,
            'current_day' : current_day,
            'utc_time' : utc_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'track' : track,
            'github_file_url' : 'https://github.com/Constantine1824/zuriHNGXtask1/task1/task1/views.py',
            'github_repo_url' : 'https://github.com/Constantine1824/zuriHNGXtask1',
            'status_code' : 200
        }
        return Response(data=payload, status=200)