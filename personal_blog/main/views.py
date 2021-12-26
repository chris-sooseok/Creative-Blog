from django.shortcuts import get_object_or_404, render, redirect
from .models import Setting
from django.contrib.auth.decorators import login_required
from .forms import SettingUpdateForm
# Create your views here.


# home page

def MainListFunction(request):
    # list of recent posts
    # list of weather
    if request.user.is_authenticated:
        return render(request, "_home.html")
    else:
        return redirect('account_login')
        

# update setting on home page
@login_required
def SettingUpdateFunction(request):
    context = {}
    user = request.user
    instance = get_object_or_404(Setting, user=user)
    # App
    form = SettingUpdateForm(request.POST or None, request.FILES or None, instance=instance)
  
    if request.method == "POST":
        if form.is_valid():
            update_app = form.save(commit=False)
            update_app.save()
            return redirect("home")
    context.update({
        'form': form,
        'setting': instance
    })
    return render(request, 'settings.html', context)
