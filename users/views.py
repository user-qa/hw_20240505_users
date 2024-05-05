from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.forms import UserModelForms
from users.models import UserModel


def UserListView(request):
    users = UserModel.objects.all()
    q = request.GET.get('q')
    if q:
        users = users.filter(full_name__icontains = q)
    context = {
        'users': users,
    }

    return render(request, 'user-list.html', context=context)


def UserRegisterView(request):
    if request.method == 'POST':
        form = UserModelForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('users:list')
        else:
            return HttpResponse('We Could Not Add The User To Our Database!')

    else:
        return render(request, 'user-register.html')


def UserDetailView(request, pk):
    current_user = UserModel.objects.filter(id=pk).first()
    if current_user:
        context = {
            'user': current_user,
        }

        return render(request, 'user-detail.html', context=context)
    else:
        return HttpResponse('User Could Not Be Found!')


def UserDownloadView(request, pk):
    current_user = UserModel.objects.filter(id=pk).first()
    print(current_user.certificate)
    if current_user:
            file_path = current_user.certificate.path
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/pdf')
                return response
    else:
        return HttpResponse('User Could Not Be Found!')

