from django.shortcuts import render, redirect

from .models import *
# Create your views here.

def login(request):
    valid = request.GET.get('failed')
    return render(request, 'main/login.html', {'valid':valid,})

def check_user(request):
    user = request.POST['user_name']
    password = request.POST['password']
    try:
        if UserInfo.objects.filter(user=user, password=password).exists():
            return redirect(f'/{user}/{password}')
        else:
            return redirect('/?failed=failed')
    except:
        return redirect('/?failed=failed')


#SIGN UP
def sign_up(request):
    user_exists = request.GET.get('user_name_already_exists')
    return render(request, 'main/sign_up.html', {'user_exists':user_exists})

def new_user(request):
    user = request.POST['user_name']
    password = request.POST['password']   

    try:
        if UserInfo.objects.filter(user=user, password=password).exists():
            return redirect('sign_up/?user_name_already_exists=True')
        else :
            new_user = UserInfo(user=user, password=password)
            new_user.save()
            return redirect(f'/{user}/{password}')
    except:
        print("Failed")



def dashboard(request, user, password):
    user_key = UserInfo.objects.get(user=user)
    to_dos = To_doLists.objects.filter(user_name=user_key.user)
    if request.method == 'POST':    
        title = request.POST['title']
        content = request.POST['content']
        new_todo = To_doLists(title=title, to_do=content, user_name=user_key.user)
        new_todo.save()
    
    return render(request, 'main/dashboard.html', {'user':user, 'password':password,'to_dos':to_dos, })


def delete(request, user, password,id):
    deleted = To_doLists.objects.filter(id=id)
    deleted.delete()
    return redirect(f'/{user}/{password}')