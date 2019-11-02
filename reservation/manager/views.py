from django.shortcuts import render, redirect
from login.models import User, Restaurant, Location

# Create your views here.
def m_home(request) :
    return render(request, 'manager/home.html')


def m_accept (request) :
    if request.method == "POST" :
        userid = request.session.get('userid')
        userinfo = User.objects.get(idName=userid)
        userinfo.isManager = True
        userinfo.save()

        request.session['manager'] = True

        restname = request.POST['restName']
        location = request.POST['local']

        local = Location.objects.get(city=location)
        
        rest = Restaurant (
            name = restname,
            location = local,
            user = userinfo
        )

        rest.save()

        return redirect('m_home')
    else :
        return render(request, "manager/accept.html")