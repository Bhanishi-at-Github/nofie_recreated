from django.shortcuts import render, redirect
from nofie_app.models import Student, Teacher, Notes


# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def category(request):

    if request.method == 'POST':

        category = request.POST.get('category')

        if category == 'student':
            return redirect('student/register_student')
        
        elif category == 'teacher':
            return redirect('teachers/register_teacher')
        
    return render(request, 'home/category.html')


# Register Functions

def register_student(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        semester = request.POST.get('semester')
        department = request.POST.get('department')
        roll_no = request.POST.get('roll_no')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # image = request.FILES.get('image')

        student = Student(
            name=name,
            semester=semester,
            department=department,
            roll_no=roll_no,
            email=email,
            
        )

        student.set_password(password)

        student.save()
        return redirect('index')
    return render(request, 'student/register_student.html')


def register_teacher(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        department = request.POST.get('department')
        # image = request.FILES.get('image')

        teacher = Teacher(
            name=name,
            email=email,
            department=department,
            password=password)
        
        
        teacher.save()
        return redirect('index')
    return render(request, 'teachers/register_teacher.html')

# Upload Function

def notes(request):

    if request.method == 'POST':
        
        subject = request.POST.get('subject')
        code = request.POST.get('code')
        file = request.FILES.get('file')
        semester = request.POST.get('semester')
        code = request.POST.get('code')
        description = request.POST.get('description')

    
        note = Notes(
            subject=subject,
            code=code,
            file=file, 
            semester=semester,
            description=description,

        )

        note.save()
        return redirect('view_notes')
    
    return render(request, 'notes/upload_notes.html')


# View Functions

def view_notes(request):

    notes = Notes.objects.all()
    return render(request, 'notes/view_notes.html', {'notes': notes})

def view_students(request):

    students = Student.objects.all()
    return render(request, 'student/view_students.html', {'students': students})

def view_teachers(request):

    teachers = Teacher.objects.all()
    return render(request, 'teachers/view_teachers.html', {'teachers': teachers})



# Delete Functions

def delete_student(request, id):

    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_students')

def delete_teacher(request, id):

    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('view_teachers')

def delete_notes(request, id):

    note = Notes.objects.get(id=id)
    note.delete()
    return redirect('view_notes')


# Update Functions

def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        student.name = request.POST.get('name')
        student.year = request.POST.get('year')
        student.semester = request.POST.get('semester')
        student.department = request.POST.get('department')
        student.roll_no = request.POST.get('roll_no')
        student.email = request.POST.get('email')
        # student.image = request.FILES.get('image')

        student.save()
        return redirect('view_students')

    return render(request, 'update_student.html', {'student': student})


def update_teacher(request, id):

    teacher = Teacher.objects.get(id=id)

    if request.method == 'POST':

        teacher.name = request.POST.get('name')
        teacher.image = request.FILES.get('image')

        teacher.save()
        return redirect('view_teachers')

    return render(request, 'update_teacher.html', {'teacher': teacher})


def update_notes(request, id):

    note = Notes.objects.get(id=id)

    if request.method == 'POST':

        note.subject = request.POST.get('subject')
        note.code = request.POST.get('code')
        note.file = request.FILES.get('file')

        note.save()
        return redirect('view_notes')

    return render(request, 'update_notes.html', {'note': note})

