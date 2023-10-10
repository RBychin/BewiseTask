from django.urls import path, include

from api.views import QuestionView

urlpatterns = [
    path('', QuestionView.as_view())
]
