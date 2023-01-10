from django.contrib import admin
from django.urls import path, include
from app.views import snippet

urlpatterns = [
        path('snippet/', snippet.SnippetView.as_view()),
        path('snippet/<int:pk>/', snippet.GetSnippet.as_view()),
        path('snippet/update/', snippet.UpdateSnippet.as_view()),
]

