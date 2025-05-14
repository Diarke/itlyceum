from django.shortcuts import render, get_object_or_404
from .models import Slider, Announcement, AboutUs, ITDirection, ITCourse, Club, ManagementMember, Contact, Footer

def home(request):
    sliders = Slider.objects.all()
    announcements = Announcement.objects.all()
    about_us = AboutUs.objects.first()
    it_direction = ITDirection.objects.first()
    it_courses = ITCourse.objects.all()
    clubs = Club.objects.all()
    management_members = ManagementMember.objects.all()
    contact = Contact.objects.first()
    footer = Footer.objects.first()

    context = {
        'sliders': sliders,
        'announcements': announcements,
        'about_us': about_us,
        'it_direction': it_direction,
        'it_courses': it_courses,
        'clubs': clubs,
        'management_members': management_members,
        'contact': contact,
        'footer': footer,
    }
    return render(request, 'index.html', context)

def about_us(request):
    about_us = AboutUs.objects.first()
    context = {
        'about_us': about_us,
    }
    return render(request, 'about_us.html', context)

def habar(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    context = {
        'announcement': announcement,
    }
    return render(request, 'habar.html', context)

def itb(request, course_id):
    course = get_object_or_404(ITCourse, id=course_id)
    context = {
        'course': course,
    }
    return render(request, 'itb.html', context)

def uirme(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    context = {
        'club': club,
    }
    return render(request, 'uirme.html', context)

def bas(request, member_id):
    member = get_object_or_404(ManagementMember, id=member_id)
    context = {
        'member': member,
    }
    return render(request, 'bas.html', context)