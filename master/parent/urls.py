from django.urls import path, include
from master.parent import views

app_name = 'parent'
urlpatterns = [
    path('', views.ParentView.as_view(), name='parent_list'),
    path('<int:target_id>', views.ParentView.parent_edit, name='parent_list_by_id'),
    path('put/<int:target_id>/', views.ParentView.parent_edit, name='parent_put'),
    # path('parent/', views.ParentListView.as_view(), name='parent_list'),
    # path('parent/add/', views.ParentView.parent_edit, name='parent_add'),
    # path('parent/del/<int:parent_id>/', views.ParentView.parent_del, name='parent_del'),
    # path('child/<int:parent_id>/', views.ChildListView.as_view(), name='child_list'),
    # path('navigation/', views.NavigationView.as_view(), name='navigation'),
]
