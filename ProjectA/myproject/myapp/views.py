from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse
from .models import person

# Create your views here.

def home_view(request):
    all_persons = person.objects.all()
    return render(request, 'index.html', {'all_persons': all_persons})

def about_view(request):
    return render(request, 'about.html')

def form_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        person.objects.create(
            name=name,
            age=age
        )
        return redirect("/")
    return render(request, 'form.html')

def delete_view(request, person_id):
    person_obj = get_object_or_404(person, pk=person_id)
    person_obj.delete()
    return redirect("/")

def edit_view(request, person_id):
    person_obj = get_object_or_404(person, pk=person_id)
    if request.method == "POST":
        # รับข้อมูลจากฟอร์มที่ส่งมาใหม่
        name = request.POST.get("name")
        age = request.POST.get("age")
        
        # อัปเดตข้อมูลลงฐานข้อมูล
        person_obj.name = name
        person_obj.age = age
        person_obj.save()
        
        # เปลี่ยนเส้นทางไปหน้าแรก
        return redirect("/")
    else:
        # แสดงหน้าฟอร์มแก้ไขข้อมูล
        return render(request, "edit.html", {"person": person_obj})