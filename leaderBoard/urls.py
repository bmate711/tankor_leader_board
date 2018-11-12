from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)

urlpatterns = router.urls