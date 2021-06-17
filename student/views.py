from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'sonam'
    request.session['lname'] = 'Jha'
    return render(request, 'student/setsession.html')

# def delsession(request):
#     if 'name' in request.session:
#         del request.session['name']

#     return render(request, 'student/delsession.html')

def getsession(request):
    name = request.session.get('name')
    lname = request.session.get('lname')
    return render(request, 'student/getsession.html', {'name':name, 'lname':lname})




def delsession(request):
    request.session.flush()
    return render(request, 'student/delsession.html')