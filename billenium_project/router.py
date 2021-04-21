from kanban.api.viewsets import *
from kanban.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Tasks', TasksViewSet)
router.register('Columns', ColumnsViewSet)
router.register('Rows', RowsViewSet)
router.register('Cells', CellsViewSet)
