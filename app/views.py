from django.shortcuts import render
from app.models import Profile

def accept(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        degree = request.POST['degree']
        about = request.POST['about']
        university = request.POST['university']
        school = request.POST['school']
        previous_work = request.POST['previous_work']
        skills = request.POST['skills']

        profile = Profile(
            name=name,
            email=email,
            mobile=mobile,
            degree=degree,
            about=about,
            university=university,
            school=school,
            previous_work=previous_work,
            skills=skills
        )

        profile.save()

    return render(request, 'accept.html')


def list(request):

    profiles = Profile.objects.all()

    return render(request, 'list.html', {'profiles': profiles})


def resume(request, id):

    user_profile = Profile.objects.get(id=id)

    return render(request, 'resume.html', {'user_profile': user_profile})