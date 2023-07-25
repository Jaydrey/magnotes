from django.contrib import admin
from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from authentication.views import NoteAppGraphView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api", csrf_exempt(NoteAppGraphView.as_view(graphiql=True)), ),
]
