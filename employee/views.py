from django.shortcuts import render,HttpResponse,redirect
from employee.forms import formEXample,studentForm,teacherForm
from employee.models import Student,Teacher
from django.contrib.auth.decorators import login_required


def staticExample(request):

    return render(request, 'static_example.html')

def create_tech(request):
    form = teacherForm()
    if request.method == 'POST':
        form = teacherForm(request.POST)
        if form.is_valid():
            form.save()
            #OR
            # stu = Teacher()
            # stu.name = form.cleaned_data['name']
            # stu.student_id = request.POST['student']
            # stu.email = form.cleaned_data['email']
            # stu.city = form.cleaned_data['city']
            # stu.gender = form.cleaned_data['gender']
            # stu.is_active = form.cleaned_data['is_active']
            # stu.save()

            return redirect('index_tech')
    return render(request, 'tech/create.html', {'form': form})
@login_required(login_url='/signin')
def index_tech(request):

    data = Teacher.objects.all()
    return render(request, 'tech/index.html', {'data': data})

def view(request,pk):

    data = Student.objects.get(id=pk)
    return render(request, 'view.html', {'data':data})


def delete(request, pk):

    data = Student.objects.get(id=pk)
    data.delete()
    return redirect('index')

def update(request, pk):

    data = Student.objects.get(id=pk)
    #select * from student where id = pk

    form = studentForm(instance=data)
    if request.method == 'POST':
        form = studentForm(request.POST, instance=data)
        if form.is_valid():
            #form.save()
            stu = Student()
            stu.id = pk
            stu.name = form.cleaned_data['email'].split('@')[0]
            stu.email = form.cleaned_data['email']
            stu.address = form.cleaned_data['address']
            stu.save()
            return redirect('index')
    return render(request, 'update.html', {'form': form})

@login_required(login_url='/signin')
def index(request):

    data = Student.objects.all()
    #select * from student
    return render(request, 'index.html', {'data':data})

@login_required(login_url='/signin')
def create(request):

    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
           #form.save()

           stu = Student()
           stu.name = form.cleaned_data['email'].split('@')[0]
           stu.email = form.cleaned_data['email']
           stu.address = form.cleaned_data['address']
           stu.save()

           return redirect('index')
    return render(request, 'tech/create.html', {'form': form})

def formTest(request):

    form = formEXample()
    if request.method == 'POST':

        form = formEXample(request.POST)
        if form.is_valid():

            print(form.cleaned_data['email'])
            pass

    return render(request, 'formTest.html', {'form':form})



def helloDjango(request):

    data = {}
    return render(request, 'hello.html', data)


def helloPython(request):

    return render(request, 'hello_python.html')
