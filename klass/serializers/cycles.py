from rest_framework import serializers
from klass.models import Klass
from users.models import User


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender']

class KlassCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Klass
        fields = ['grade', 'name', 'students_number',]



class KlassListDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Klass
        fields = [
            'slug',
            'grade',
            'name',
            'created_at',
            'students_number',

        ]
