from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Func, F

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics

from app.models import Snippet
from app.serializer import SnippetSerializer
from app.elo import calculate_elo

import random

K = 25

class SnippetView(APIView):

    def get_two_random_snippets(self):
        snippets = Snippet.objects.all()
        snippet_one = random.choice(snippets)
        snippet_two = random.choice(snippets)

        while snippet_one == snippet_two:
            snippet_two = random.choice(snippets)

        return [snippet_one, snippet_two]

    def get(self, request):

        #  snippets = Snippet.objects.all()
        #  snippet_one = random.choice(snippets)

        #  snippet_two = Snippet.objects.filter(score__lt=snippet_one.score).order_by('-score')
        #  if len(snippet_two) == 0:
            #  snippet_two = Snippet.objects.filter(score__gt=snippet_one.score).order_by('score')

        #  #  print(snippet_one.code)
        #  snippetx = [snippet_one, snippet_two[0]]

        snippets = self.get_two_random_snippets()
        serializer = SnippetSerializer(snippets,  many=True)

        return Response({ "snippets": serializer.data })


    def post(self, request):
        try:
            code = request.data["code"]
            author = request.data["author"]

            Snippet.objects.create(code=code, author=author)
            return Response({ "message": "snippet created" })
        except Exception as e:
            print(e)
            return Response({ "message": "some error occured" })

class GetSnippet(generics.RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UpdateSnippet(APIView):
    def put(self, request, *args, **kwargs):
        try:
            hot = request.data["hot"]
            nt = request.data["not"]
            
            hot_snippet = Snippet.objects.get(id=hot)
            not_snippet = Snippet.objects.get(id=nt)

            hot_snippet_score = hot_snippet.score
            not_snippet_score = not_snippet.score

            elo_points = calculate_elo(hot_snippet_score, not_snippet_score)

            hot_snippet_score += K * (1 - elo_points)
            not_snippet_score += K * (0 - elo_points)
            
            Snippet.objects.filter(id=hot).update(score=hot_snippet_score)
            Snippet.objects.filter(id=nt).update(score=not_snippet_score)

            return Response({ "message": "updated snippets", "hot": hot_snippet_score, "not": not_snippet_score })

        except ObjectDoesNotExist as e:
            print(e)
            print("snippet does not exist")
