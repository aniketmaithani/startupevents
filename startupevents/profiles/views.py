from django.views.generic import View
from django.shortcuts import render
from .models import UserProfile
from startupevents.customuser.models import User


class Registration(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'profiles/registration.html')

    def post(self, request, *args, **kwargs):
        template_name = 'profiles/registration.html'

        try:
            email_id = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            user = User.objects.create(
                email=email_id, password=password1,
                is_staff=True, is_superuser=False, first_name=first_name, last_name=last_name)
            if password1 == password2:
                user.set_password(password1)
                user.save()
            else:
                render(request, template_name, {'error': "Password Do not match"})
            mobile_number = request.POST['mobile']
            UserProfile.objects.create(user=user, mobile=mobile_number)
            return render(request, template_name, {'success': "Registration Successful"})
        except:
            context = "Please Check the Details. Invalid Form Fill Up"
            return render(request, template_name, {'error': context})
