from django.urls import path
from .views import MainListFunction, SettingUpdateFunction

urlpatterns = [
    path('', MainListFunction, name='home'),
    path('settings/', SettingUpdateFunction, name="update_setting"),
]