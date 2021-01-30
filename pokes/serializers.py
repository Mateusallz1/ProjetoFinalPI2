from rest_framework import serializers
from pokes.models import Pokemon, Type, Trainer, Researcher


class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(queryset=Type.objects.all(), slug_field='name')

    class Meta:
        model = Pokemon
        fields = ('url', 'name', 'type')


class PokemonDetailSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(queryset=Type.objects.all(), slug_field='name')

    class Meta:
        model = Pokemon
        fields = ('name', 'description', 'type')


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('url', 'name')


class TypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'description')


class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ('url', 'name', 'age')


class TrainerDetailSerializer(serializers.ModelSerializer):
    pokemon = serializers.SlugRelatedField(queryset=Pokemon.objects.all(), many=True, slug_field='name')

    class Meta:
        model = Trainer
        fields = ('name', 'age', 'region', 'pokemon')


class ResearcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Researcher
        fields = ('name',)


class ResearcherDetailSerializer(serializers.ModelSerializer):
    trainers = serializers.SlugRelatedField(queryset=Trainer.objects.all(), slug_field='name')

    class Meta:
        model = Researcher
        fields = ('name', 'trainers')