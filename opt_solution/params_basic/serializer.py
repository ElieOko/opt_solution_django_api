from rest_framework import serializers
from .models import Option, Section, Promotion, Student, TypeFraisAcademique, FraisAcademique, FraisAcademiqueStudent


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        # ['libelleSection']


class OptionSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=False, read_only=True)

    class Meta:
        model = Option
        fields = '__all__'
        # ['libelleOption']


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'
        # ['PromotionOption']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TypeFraisAcademiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFraisAcademique
        fields = '__all__'


class FraisAcademiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraisAcademique
        fields = '__all__'


class FraisAcademiqueStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraisAcademiqueStudent
        fields = '__all__'

