from rest_framework import routers
from users.viewsets import StudentsViewSets, StudentDetailViewSets

router = routers.DefaultRouter()

router.register(
    'students',
    StudentsViewSets
)
router.register(
    'student-detail',
    StudentDetailViewSets
)