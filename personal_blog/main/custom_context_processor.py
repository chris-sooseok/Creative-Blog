from .models import Setting
import json
from django.contrib.auth.decorators import login_required
from config.settings import DISPLAY_APPS
# pass app_display_dict from setting model if the value is set

def apps(request):
    if request.user.is_authenticated:
        user = request.user
        setting = Setting.objects.get(user=user)
        if setting.app_display_dict != None:
            return {'APP_DISPLAY_DICT':json.loads(setting.app_display_dict), 'DISPLAY_APPS': DISPLAY_APPS}
        else:
            return {'emtpy':"empty"}
    else:  
        return {'empty':'empty'}

