from kanban.api.viewsets import *
from kanban.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Task', TaskViewSet)
router.register('Column', ColumnViewSet)
