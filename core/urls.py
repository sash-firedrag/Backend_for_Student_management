from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = router.urls
