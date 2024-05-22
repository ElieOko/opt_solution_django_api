from rest_framework import routers
from .views import (SectionViewSet, OptionViewSet, PromotionViewSet, StudentViewSet, TypeFraisAcademiqueViewSet,
                    FraisAcademiqueStudentViewSet, FraisAcademiqueViewSet)

router = routers.DefaultRouter(use_regex_path=False)
router.register(r'section', SectionViewSet)
router.register(r'option', OptionViewSet)
router.register(r'promotion', PromotionViewSet)
router.register(r'student', StudentViewSet)
router.register(r'frais/academique/student', FraisAcademiqueStudentViewSet)
router.register(r'type/frais/academique', TypeFraisAcademiqueViewSet)
router.register(r'frais/academique', FraisAcademiqueViewSet)
urlpatterns = router.urls
