from django.urls import path
from .views import view_shortlist, add_to_shortlist, remove_from_shortlist

urlpatterns = [
    path('view', view_shortlist, name="view_shortlist"),
    path('add', add_to_shortlist, name="add_to_shortlist"),
    path('remove', remove_from_shortlist, name="remove_from_shortlist")
]