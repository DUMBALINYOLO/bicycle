from rest_framework.routers import DefaultRouter
from .apis import KlassViewSet

router = DefaultRouter()

router.register('classes', KlassViewSet, basename='classes')

print(router.urls)


urlpatterns = router.urls
