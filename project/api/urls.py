from django.urls import path

from api.views import QuestionView

urlpatterns = [
    path('', QuestionView.as_view())
]
