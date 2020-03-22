from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'website/home.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        messsge_email = request.POST['message-email']
        message = request.POST['message']
        # try:
        send_mail(
            message_name,
            message,
            messsge_email,
            ['fakeemailforreal113@gmail.com'],
            fail_silently=True,)
        # except:
        # return render(request, 'website/contact.html', {})
        return render(request, 'website/contact.html', {'message_name': message_name})
    else:
        pass
        return render(request, 'website/contact.html', {})
