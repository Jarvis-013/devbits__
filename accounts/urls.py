from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('create-teacher', views.TeacherRegisterView.as_view(), name='create_teacher'),
    path('teacher-login', views.TeacherLoginView.as_view(), name='teacher_login'),
    path('users/', include([
        path('my-courses', views.EnrolledCoursesListView.as_view(), name='enrolled-courses'),
        path('my-courses/<slug:slug>/view', views.StartLessonView.as_view(), name='course-lessons'),
        path('my-courses/<slug:slug>/lessons/<int:id>', views.LessonView.as_view(), name='course-lessons-single'),
        path('profile', views.ProfileUpdateView.as_view(), name='my-profile'),
    ])),
]
