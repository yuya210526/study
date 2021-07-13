from django.urls import path
from sample import views

app_name = 'sample'
urlpatterns = [
    path('parent/', views.ParentListView.as_view(), name='parent_list'),
    path('parent/add/', views.ParentView.parent_edit, name='parent_add'),
    path('parent/put/<int:parent_id>/', views.ParentView.parent_edit, name='parent_put'),
    path('parent/del/<int:parent_id>/', views.ParentView.parent_del, name='parent_del'),
    path('child/<int:parent_id>/', views.ChildListView.as_view(), name='child_list'),
    path('navigation/', views.NavigationView.as_view(), name='navigation'),
    path('navigation2/', views.NavigationView2.as_view(), name='navigation2'),
]
