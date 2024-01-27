from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("<int:project_id>/result/", views.result, name="result"),
    path("project/<int:project_id>", views.signoff, name="signoff"),
    # path('login',views.login_page,name="login"),
    # path('logout',views.logout_page,name="logout"),

]