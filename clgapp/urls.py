from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index)
]
'''
urlpatterns=[
   
    path('',views.landin),

    path('show/',views.add,name='add'),
    path('insert/',views.insert,name='insert'),
    path('index/',views.index,name='index'),
    path('delete/<int:student_id>/', views.delete, name='delete'), 
    path('edit/<int:student_id>/', views.edit, name='edit'),
    path('login/',views.login,name='login'),
    path('landing/',views.landin),
    path('stuind/',views.stuind,name='stuind'),
    path('teactions',views.teactions,name='teactions'),
    path('teacherind',views.teacherind,name='teacherind'),
    path('about',views.about,name="about"),
    path('placement/',views.placement,name='placement'),
    path('teacherattendence/',views.teacherattendence,name="teacherattendence"),
    path('admnadd',views.admnadd,name='admnadd'),
    path('teacheradd/',views.teacheradd,name='teacheradd'),
    path('admnact',views.admnact,name='admnact'),
    path('admnaddd/',views.admnaddd,name='admnaddd'),
    path('admnteacher/',views.admnteacher,name='adminteacher'),
    path('dept/',views.dept,name='dept'),
    path('admm/',views.admm,name='admm'),
    path('atten/', views.edit_attendance, name='atten'),
    path('sattendence/',views.sattendence,name='sattendence'),
   
    path('teacherauth/',views.teacherauth,name='teacherauth')
    

]
'''