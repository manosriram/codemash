from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from app.views import snippet


handler404 = 'app.views.view_404' 
urlpatterns = [
        path('', snippet.SnippetView.as_view()),
        #  path('snippet/', snippet.SnippetView.as_view()),
        path('snippet/<int:pk>/', snippet.GetSnippet.as_view()),
        path('snippet/update/', snippet.UpdateSnippet.as_view()),
        path('upload/', snippet.UploadSnippetPageView.as_view()),
        path('ranks/', snippet.RankSnippetPageView.as_view()),
        #  path('<path:path>', lambda request, path: redirect('/', permanent=False)),
]

