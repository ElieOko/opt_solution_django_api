from rest_framework import routers
from .views import SectionViewSet, OptionViewSet, PromotionViewSet

router = routers.DefaultRouter()
router.register(r'section', SectionViewSet)
router.register(r'option', OptionViewSet)
router.register(r'promotion', PromotionViewSet)
urlpatterns = router.urls
