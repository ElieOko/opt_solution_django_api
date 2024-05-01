from rest_framework import routers
from .views import SectionViewSet, OptionViewSet, PromotionViewSet

router = routers.DefaultRouter(use_regex_path=False)
router.register(r'section', SectionViewSet)
router.register(r'option', OptionViewSet)
router.register(r'promotion', PromotionViewSet)
# router.register(r'promotion/details', PromotionViewSet.promotion_detail)
urlpatterns = router.urls
