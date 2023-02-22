from django.shortcuts import render
from .models import Student

# Create your views here.



def index(request):

    if request.method == 'POST':
        age = request.POST.get('age')
        personality = request.POST.get('personality-type')
        if int(age)<=18 and int(age)>=12:
            std = 'Teenage'
        elif int(age)>=18 and int(age)<=25:
            std = 'Young'
        elif int(age)>=25 and int(age)<=45:
            std = 'Adult'
        elif int(age)<=12:
            std = 'Children'
        else:
            std = 'Old'

        book = Student.objects.filter(age=std, personality=personality)
        return render(request, 'new.html', {'book':book})

        
    return render(request, 'index.html')