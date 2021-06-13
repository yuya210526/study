from django.urls import path, include
from master import views

app_name = 'master'
urlpatterns = [
    # path("parent/", include('master.parent.urls'), name="parent"),
    path('', views.master, name='master'),
    path('parent/', views.ParentView.parent_edit, name='parent_list'),
    path('parent/<int:target_id>/', views.ParentView.parent_edit, name='parent_list_by_id'),
    path('parent/put/', views.ParentView.parent_edit, name='parent_put'),
    path('parent/put/<int:target_id>/', views.ParentView.parent_edit, name='parent_put'),
    path('parent/new/', views.ParentView.parent_edit, name='parent_new'),
    path('parent/add/', views.ParentView.parent_edit, name='parent_add'),
    path('parent/del/<int:target_id>/', views.ParentView.parent_del, name='parent_del'),
]
