from python_justclick.justclick import JustClickConnection
from django.conf import settings


justClickConnection = JustClickConnection(settings.JUSTCLICK_USERNAME, settings.JUSTCLICK_API_KEY)
