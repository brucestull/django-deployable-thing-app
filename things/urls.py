from django.urls import path
from . import views

app_name = "things"
urlpatterns = [
    path("", views.ThingListView.as_view(), name="thing_list"),
    path("<int:pk>/", views.ThingDetailView.as_view(), name="thing_detail"),
    path("create/", views.ThingCreateView.as_view(), name="thing_create"),
    path("<int:pk>/update/", views.ThingUpdateView.as_view(), name="thing_update"),
    path("<int:pk>/delete/", views.ThingDeleteView.as_view(), name="thing_delete"),
]
