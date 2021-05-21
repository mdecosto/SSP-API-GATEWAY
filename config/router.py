from api.views import UserRoleViewSet, AccountViewSet, KeysViewSet, LogsViewSet, BaseModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('userrole', UserRoleViewSet)
router.register('account', AccountViewSet)
router.register('keys', KeysViewSet)
router.register('logs', LogsViewSet)
router.register('base_model', BaseModelViewSet)