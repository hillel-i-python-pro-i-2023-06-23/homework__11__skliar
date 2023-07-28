from django.urls import path
from . import views

apps_name = "base"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name="index"),
]
