from django.urls import path
from .views import PendingsList, TaskDetail, CreateTask, EditTask, DeleteTask, Login, SignUpPage
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', PendingsList.as_view(), name='tasks'),
               path('login/', Login.as_view(), name='login'),
               path('signup/', SignUpPage.as_view(), name='signup'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('task/<int:pk>', TaskDetail.as_view(), name='task'),
               path('create-task/', CreateTask.as_view(), name='create-task'),
               path('edit-task/<int:pk>', EditTask.as_view(), name='edit-task'),
               path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task')]
