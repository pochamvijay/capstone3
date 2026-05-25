from django.shortcuts import render, redirect
from app.models import Profile


# HOME PAGE + SAVE DATA

def accept(request):

    if request.method == "POST":

        profile = Profile.objects.create(

            name=request.POST['name'],

            email=request.POST['email'],

            mobile=request.POST['mobile'],

            degree=request.POST['degree'],

            about=request.POST['about'],

            university=request.POST['university'],

            school=request.POST['school'],

            previous_work=request.POST['previous_work'],

            skills=request.POST['skills']
        )

        return redirect(f'/resume/{profile.id}/')

    return render(request, 'app/index.html')


# RESUME PAGE

def resume(request, id):

    user_profile = Profile.objects.get(id=id)

    return render(request, 'app/resume.html', {
        'user_profile': user_profile
    })