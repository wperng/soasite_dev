from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("<int:project_id>/signoff/", views.signoff, name="signoff"),
    path("project/<int:project_id>", views.project, name="signoff"),
    path('login',views.login, name="login"),
    # path('logout',views.logout_page,name="logout"),

]