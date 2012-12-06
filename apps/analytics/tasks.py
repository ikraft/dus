from django_rq import job
from .models import Analytics

@job
def save_analytics_data(data):
    analytics = Analytics(
            link = data[0],
            ip = data[1],
            location = data[2],
            user_agent = data[3],
            referer = data[4],
        )
    analytics.save()
save_analytics_data.delay()