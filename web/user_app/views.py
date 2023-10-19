from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from user_app.form import RegisterForm, UserChangeForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
# Create your views here.

class index(View):
    def get(self, request):
        return render(request,'user_app/index.html')

class loginClass(View):
    def get(self, request):
        return render(request,'user_app/login.html')
    
    def post(self, request):
        user = request.POST.get('username')
        passw = request.POST.get('password')
        myUser = authenticate(username = user, password = passw)
        if myUser is None:
            return HttpResponse('khong ton tai')
        else:
            login(request,myUser)
        return redirect('/')
    
class register(View):
    def get(self, request):
        f = RegisterForm()
        context = {"form": f}
        return render(request,'user_app/reg.html',context)
    
    def post(self, request):
        f = RegisterForm(request.POST) 
        if f.is_valid():
            user = f.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('/login/')
        return render(request, 'user_app/reg.html', {'form': f})
        
class listUser(LoginRequiredMixin,View):
    login_url = '/login'
    
    def get(self, request):
        users = {'list': User.objects.all()}
        return render(request,'user_app/user_list.html', users)
    
# class userChange(LoginRequiredMixin,View):
#     login_url = '/login'
    
#     def get(self, request):
#         f = UserChangeForm()
#         return render(request,'user_app/edit_user.html', {"form": f})
    
#     def post(self, request, user_id):
#         user = get_object_or_404(User, pk=user_id)
#         form = UserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('/user_list')
#         return render(request,'user_app/edit_user.html',{"user": user})

class EditUserView(LoginRequiredMixin,UpdateView):
    login_url = '/login'
    
    model = User
    form_class = UserChangeForm  
    template_name = 'user_app/edit_user.html'
    success_url = '/listuser/'
        