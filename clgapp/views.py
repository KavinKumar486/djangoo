from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
def index(request):
    return HttpResponse('kini')
'''
from .models import Stu,Adminsss,Teacher,Tadmin,Attendence,Tadmin


def add(request):
    return render(request,'add.html')
def insert(request):
    if request.method == 'POST':
        name = request.POST.get('sname', '')
        reg = request.POST.get('sreg', '')
        
        if name and reg:
            a = Stu(name=name, reg=reg)
            b = Attendence(sname=name,sreg=reg)
            b.save()
            a.save()

            return redirect('index')

    return HttpResponse('Invalid form submission')

def edit_attendance(request):
    temp_list = Attendence.objects.all()
   
    student_id = request.POST.get('student_id', None)
    if student_id is not None:
        for temp in temp_list:
            if str(temp.id) == student_id:
                   
                    p1 = request.POST['p1']
                    a1 = request.POST['a1']
                    p2 = request.POST['p2']
                    a2 = request.POST['a2']
                    p3 = request.POST['p3']
                    a3 = request.POST['a3']
                    p4 = request.POST['p4']
                    a4 = request.POST['a4']
                    p5 = request.POST['p5']
                    a5 = request.POST['a5']
                    p6 = request.POST['p6']
                    a6 = request.POST['a6']
                    p7 = request.POST['p7']
                    a7 = request.POST['a7']
                    p8 = request.POST['p8']
                    a8 = request.POST['a8']
                    tot1 = int(p1) + int(a1)
                    tot2 = int(p2) + int(a2)
                    tot3 = int(p3)+ int(a3)
                    tot4 = int(p4)+ int(a4)
                    tot5 = int(p5) + int(a5)
                    tot6 = int(p6) + int(a6)
                    tot7 = int(p7) + int(a7)
                    tot8 = int(p8) + int(a8)
                    temp_p1=((((int(p1)/tot1)*float(temp.p1))+100)/2)
                    temp_p2=((((int(p2)/tot2)*float(temp.p2))+100)/2)
                    temp_p3=((((int(p3)/tot3)*float(temp.p3))+100)/2)
                    temp_p4=((((int(p4)/tot4)*float(temp.p4))+100)/2)
                    temp_p5=((((int(p5)/tot5)*float(temp.p5))+100)/2)
                    temp_p6=((((int(p6)/tot6)*float(temp.p6))+100)/2)
                    temp_p7=((((int(p7)/tot7)*float(temp.p7))+100)/2)
                    temp_p8=((((int(p8)/tot8)*float(temp.p8))+100)/2)
                    temp_p1 = round(temp_p1,2)
                    temp_p2 = round(temp_p2,2)
                    temp_p3 = round(temp_p3,2)
                    temp_p4 = round(temp_p4,2)
                    temp_p5 = round(temp_p5,2)
                    temp_p6 = round(temp_p6,2)
                    temp_p7 = round(temp_p7,2)
                    temp_p8 = round(temp_p8,2)

                    temp.p1=temp_p1
                    temp.p2=temp_p2
                    temp.p3=temp_p3
                    temp.p4=temp_p4
                    temp.p5=temp_p5
                    temp.p6=temp_p6
                    temp.p7=temp_p7
                    temp.p8=temp_p8
                    
                    temp.save()
                    
    return render(request, 'attendenceee.html', {'temp_list': temp_list})    

          

def admnadd(request):
    if request.method == 'POST':        
        tname = request.POST['sname']
        treg = request.POST['sreg']
        tscourse = request.POST['scourse']
        tsphn = request.POST['sphn']
        tsaddress = request.POST['saddress']
        tsemail = request.POST['semail']
        tadmndate =request.POST['admndate']
        tstc = request.POST['stc']
        tsfather = request.POST['sfather']
        tsmother = request.POST['smother']
        tsfphn = request.POST['sfphn']
        tsfoccupation = request.POST['sfoccupation']
        tsfincome = request.POST['sfincome']
        tsdob = request.POST['sdob']
        taadhar = request.POST['saadhar']
        tbld = request.POST['sbld']
        b = Stu(name=tname,reg=treg)
        c = Attendence(sname = tname,sreg = treg)
        a = Adminsss(sname=tname,sreg=treg,sphn=tsphn,scourse=tscourse,saddress=tsaddress,semail=tsemail,admndate=tadmndate,stc=tstc,sfather=tsfather,smother=tsmother,sfphn=tsfphn,sfoccupation=tsfoccupation,sfincome=tsfincome,sdob=tsdob,saadhar=taadhar,sbld = tbld)
        if not all([tname, treg, tsphn, tsaddress, tsemail, tadmndate, tstc, tsfather, tsmother, tsfphn, tsfoccupation, tsfincome, tsdob, taadhar, tbld]):
            error_message = "Please fill in all required fields."
            return render(request, 'admnadd.html',   {'error_message': error_message})
        else:
            a.save()
            b.save()
            c.save()
            return HttpResponse('Add Success')
            
def admnaddd(request):
    return render(request,'admnadd.html')


def index(request):
    students = Stu.objects.all()
    query = request.GET.get('q')
    if query:
        students = Stu.objects.filter(reg__icontains=query)
  
    return render(request, 'teacherindex.html', {'students': students})
def stuind(request):
    students = Stu.objects.all()    
    return render(request,'index.html',{'students':students})
def delete(request,student_id):
    student = get_object_or_404(Stu, pk=student_id)
    astu =  get_object_or_404(Attendence,pk=student_id)
    tstu = get_object_or_404(Adminsss,pk=student_id)
    astu.delete()
    tstu.delete()
    student.delete()
    return redirect('index')
def edit(request, student_id):
    student = get_object_or_404(Stu, pk=student_id)
    astu =  get_object_or_404(Attendence,pk=student_id)
    tstu = get_object_or_404(Adminsss,pk=student_id)
    if request.method == 'POST':
        name = request.POST.get('sname')
        reg = request.POST.get('sreg')
        astu.sname = name
        astu.sreg = reg
        tstu.sname = name
        tstu.sreg = reg
        astu.save()
        tstu.save()
        student.name = name
        student.reg = reg
        student.save()

        return redirect('index')

    return render(request, 'eedit.html', {'student': student})
def landin(request):
    return render(request,'landing.html')


def login(request):
    if request.method == 'POST':
        vname = request.POST['lname']
        vreg = request.POST['lreg']

        try:
            student = Stu.objects.get(name=vname, reg=vreg)
        except Stu.DoesNotExist:
            return HttpResponse('Fail')   
        else:
            return redirect('stuind')
    return render(request, 'login.html')   
def teactions(request):
    return render(request,'teeacheractions.html')
def teacherind(request):
    return render(request,'teacherindex.html')
def about(request):
    return render(request,'about.html')
def placement(request):
    return render(request,'placement.html')
def teacherattendence(request):
    return render(request,'teachatt.html')
def teacheradd(request):
    if request.method == 'POST':
        ttname = request.POST['tname']
        ttid = request.POST['tid']
        a = Tadmin(teachername=ttname,teacherid=ttid)
        a.save()
        return HttpResponse("add success")
    
def admnact(request):
    return render(request,'admnactions.html')
def admnteacher(request):
    return render(request,'adminaddteacher.html')
def dept(request):
    if request.method == 'post':
        s = request.POST.get['dept']
        return redirect(request,'login.html')
    return render(request,'dept.html')

def admm(request):
    name = request.POST['admnname']
    pas = request.POST['admnpass']
    name = name.lower()
    
    if name == 'admin' and pas == 'AdmiN@45264':
        return redirect('admnact')
    return render(request,'wrongpass.html')
def sattendence(request):
    a = Attendence.objects.all()
    return render(request,'attendence.html',{'a':a})

def teacherauth(request):
    if request.method == 'POST':
        t_tname = request.POST['tname']
        t_tid = request.POST['tid']
        try:
            a = Tadmin.objects.get(teachername=t_tname,teacherid=t_tid)
        except Teacher.DoesNotExist:
            return HttpResponse('Does Not Exist')
        else:
            return render(request,'teeacheractions.html')
    return render(request,'teacherlogin.html')
'''