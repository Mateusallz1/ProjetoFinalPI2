from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.throttling import ScopedRateThrottle
from pokes.permissions import IsOwnerOrReadOnly
from pokes.models import Pokemon, Type, Trainer, Researcher
from pokes.serializers import PokemonSerializer, TypeSerializer, TypeDetailSerializer, TrainerSerializer, TrainerDetailSerializer, ResearcherSerializer, PokemonDetailSerializer, ResearcherDetailSerializer, UserSerializer


class ListPokes(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    name = 'pokemon-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('name', 'owner',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'number',)
    throttle_scope = 'pokemon-throttle'
    throttle_classes = (ScopedRateThrottle,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailPokes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 
    name = 'pokemon-detail'
    throttle_scope = 'pokemon-throttle'
    throttle_classes = (ScopedRateThrottle,)


class ListTypes(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    name = 'types-list'


class DetailTypes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) 
    name = 'type-detail'


class ListTrainers(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    name = 'trainer-list'
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name','age')
    throttle_scope = 'trainer-throttle'
    throttle_classes = (ScopedRateThrottle,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailTrainers(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 
    name = 'trainer-detail'
    throttle_scope = 'trainer-throttle'
    throttle_classes = (ScopedRateThrottle,)


class ListResearchers(generics.ListCreateAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    name = 'researcher-list'


class DetailResearchers(generics.RetrieveUpdateDestroyAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 
    name = 'researchers-detail'


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated),
    name = 'user-list'


class DetailUsers(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)
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
