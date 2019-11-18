from django.urls import path
from . import views
app_name = "colegio"
urlpatterns = [
    path("", views.PensumListView.as_view(), name="index"),
    path("<int:pk>/", views.PensumDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.PensumUpdateView.as_view(), name="update"),
    path("create/", views.PensumCreateView.as_view(), name="create"),
]
