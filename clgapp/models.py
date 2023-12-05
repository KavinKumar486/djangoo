from django.db import models
'''
class Stu(models.Model):
    name = models.CharField(max_length=200)
    reg = models.IntegerField()
    class Meta:
        db_table = 'student'
class Teacher(models.Model):
    tname = models.CharField(max_length=200)
    tid = models.IntegerField()
    class Meta:
        db_table='teacher'

class Tadmin(models.Model):
    teachername = models.CharField(max_length=200)
    teacherid = models.IntegerField()
    trating = models.DecimalField(max_digits=20,decimal_places=5,default=0.0)

    class Meta:
        db_table = 'admin_teacher'
class Adminsss(models.Model):
    sname = models.CharField(max_length=200)
    sreg = models.IntegerField()
    sphn = models.IntegerField()
    scourse = models.CharField(max_length=200)
    saddress = models.CharField(max_length=300)
    semail = models.EmailField()
    admndate = models.DateField()
    stc = models.CharField(max_length=200)
    sfather =models.CharField(max_length=200)
    smother = models.CharField(max_length=200)
    sfphn = models.PositiveBigIntegerField()
    sfoccupation = models.CharField(max_length=200)
    sfincome =  models.CharField(max_length=200)
    sdob = models.CharField(max_length=15)
    saadhar = models.CharField(max_length=16)
    sbld = models.CharField(max_length=200)
    class Meta:
        db_table = 'adminn'

class Attendence(models.Model):
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    sub4 = models.IntegerField()
    sub5 = models.IntegerField()
    sub6 = models.IntegerField()
    sub7 = models.IntegerField()
    sub8 = models.IntegerField()
    class Meta:
        db_table = 'attendence'



from django.db import models

class Attendence(models.Model):
    sname = models.CharField(max_length=200)
    sreg = models.IntegerField()
    p1 = models.CharField(max_length=7,default='100')
    p2 = models.CharField(max_length=7,default='100')
    p3 = models.CharField(max_length=7,default='100')
    p4 = models.CharField(max_length=7,default='100')
    p5 = models.CharField(max_length=7,default='100')
    p6 = models.CharField(max_length=7,default='100')
    p7 = models.CharField(max_length=7,default='100')
    p8 = models.CharField(max_length=7,default='100')

    class Meta:
        db_table = 'attendence'

'''