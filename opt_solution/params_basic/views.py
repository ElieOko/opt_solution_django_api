from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Section, Option, Promotion
from .serializer import SectionSerializer, OptionSerializer, PromotionSerializer
# https://blog.devgenius.io/viewset-and-modelviewset-in-drf-690ab99a7afa


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticated]

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
            return Response(status=status.HTTP_201_CREATED, data={"message": "Enregistrement réussi avec succès",
                                                                  'section': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    lookup_field = 'libelleOption'
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
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
