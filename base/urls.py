from django.contrib.auth.views import LogoutView
from django.urls import path
from base.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, \
    TaskDelete, CustomLoginView, RegisterView

urlpatterns = [
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),

    path('',TaskList.as_view(), name='tasks'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
    path('task/<str:pk>/',TaskDetail.as_view(), name='task-detail'),
    path('task-update/<str:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-Delete/<str:pk>/',TaskDelete.as_view(), name='task-delete'),

]