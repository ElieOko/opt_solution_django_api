from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Section, Option, Promotion
from .serializer import SectionSerializer, OptionSerializer, PromotionSerializer


# Create your views here.
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    #
    # def get(self, request):
    #     items = Promotion.objects.all().order_by('libellePromotion')
    #     list = []
    #     for item in items:
    #         tabResult = {}
    #         tabResult['id'] = item.id
    #         tabResult['libellePromotion'] = item.libellePromotion
    #         list.append(tabResult)