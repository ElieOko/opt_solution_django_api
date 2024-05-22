from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Section, Option, Promotion, Student, FraisAcademique, TypeFraisAcademique, FraisAcademiqueStudent
from .serializer import (SectionSerializer, OptionSerializer, PromotionSerializer, StudentSerializer,
                         TypeFraisAcademiqueSerializer, FraisAcademiqueStudentSerializer, FraisAcademiqueSerializer)


# https://blog.devgenius.io/viewset-and-modelviewset-in-drf-690ab99a7afa


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['libelleSection']
    lookup_field = "libelleSection"
    # permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        section = self.get_object()
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"Message": "Suppression réussie avec succès"})

    def update(self, request, *args, **kwargs):
        section = self.get_object()
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Modification réussie avec succès", 'section': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        section = Section.objects.all()
        serializer = SectionSerializer(section, many=True)
        return Response(data={'section': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={"message": "Enregistrement réussi avec succès",
                                                                  'section': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # lookup_field = 'libelleOption'
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['libelleOption']
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={"message": "Enregistrement réussi avec succès",
                                                                  'option': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        option = Option.objects.all()
        serializer = OptionSerializer(option, many=True)
        return Response(data={'options': serializer.data})

    def update(self, request, *args, **kwargs):
        option = self.get_object()
        serializer = SectionSerializer(option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Modification réussie avec succès", 'option': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        option = self.get_object()
        option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Suppression réussie avec succès"})


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def create(self, request, *args, **kwargs):
        serializer = PromotionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'promotion': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        promotion = self.get_object()
        serializer = SectionSerializer(promotion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Modification réussie avec succès", 'promotion': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        promotion = Promotion.objects.all()
        serializer = PromotionSerializer(promotion, many=True)
        return Response(data={'promotions': serializer.data})

    def destroy(self, request, *args, **kwargs):
        promotion = self.get_object()
        promotion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Suppression réussie avec succès"})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['matricule']

    def create(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'promotion': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = StudentSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Modification réussie avec succès", 'student': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(data={'students': serializer.data})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Suppression réussie avec succès"})


class FraisAcademiqueStudentViewSet(viewsets.ModelViewSet):
    queryset = FraisAcademiqueStudent.objects.all()
    serializer_class = FraisAcademiqueStudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = FraisAcademiqueStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'frais_academique_student': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = FraisAcademiqueStudentSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Modification réussie avec succès",
                                  'frais_academique_student': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(data={'frais_academique_student': serializer.data})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Suppression réussie avec succès"})


class FraisAcademiqueViewSet(viewsets.ModelViewSet):
    queryset = FraisAcademique.objects.all()
    serializer_class = FraisAcademiqueSerializer

    def create(self, request, *args, **kwargs):
        serializer = FraisAcademiqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès",
                                  'frais_academique': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = FraisAcademiqueSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Modification réussie avec succès",
                                  'frais_academique': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        data = FraisAcademique.objects.all()
        serializer = FraisAcademiqueSerializer(data, many=True)
        return Response(data={'frais_academique': serializer.data})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Suppression réussie avec succès"})


class TypeFraisAcademiqueViewSet(viewsets.ModelViewSet):
    queryset = TypeFraisAcademique.objects.all()
    serializer_class = TypeFraisAcademiqueSerializer

    def create(self, request, *args, **kwargs):
        serializer = TypeFraisAcademiqueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès",
                                  'type_frais_academique': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = self.get_object()
        serializer = TypeFraisAcademiqueSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Modification réussie avec succès",
                                  'type_frais_academique': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        data = TypeFraisAcademique.objects.all()
        serializer = TypeFraisAcademiqueSerializer(data, many=True)
        return Response(data={'type_frais_academique': serializer.data})

    def destroy(self, request, *args, **kwargs):
        data = self.get_object()
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Suppression réussie avec succès"})
