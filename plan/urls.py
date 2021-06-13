from django.urls import path, include
from plan import views

app_name = 'plan'
urlpatterns = [
    path('date/<str:target_date>/category/<int:target_category>/id/<int:target_id>/', views.PlanView.plan_edit, name='plan_edit'),
]
