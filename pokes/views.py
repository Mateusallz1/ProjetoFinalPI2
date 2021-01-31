from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from pokes.models import Pokemon, Type, Trainer, Researcher
from pokes.serializers import PokemonSerializer, TypeSerializer, TypeDetailSerializer, TrainerSerializer, TrainerDetailSerializer, ResearcherSerializer, PokemonDetailSerializer, ResearcherDetailSerializer, UserSerializer


class ListPokes(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    name = 'pokemon-list'


class DetailPokes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonDetailSerializer
    name = 'pokemon-detail'


class ListTypes(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'types-list'


class DetailTypes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeDetailSerializer
    name = 'type-detail'


class ListTrainers(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    name = 'trainer-list'


class DetailTrainers(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerDetailSerializer
    name = 'trainer-detail'


class ListResearchers(generics.ListCreateAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializer
    name = 'researcher-list'


class DetailResearchers(generics.RetrieveUpdateDestroyAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherDetailSerializer
    name = 'researchers-detail'


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class DetailUsers(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'pokemon': reverse(ListPokes.name, request=request),
            'types': reverse(ListTypes.name, request=request),
            'trainers': reverse(ListTrainers.name, request=request),
            'researchers': reverse(ListResearchers.name, request=request),
            'users': reverse(ListUsers.name, request=request),
        })
