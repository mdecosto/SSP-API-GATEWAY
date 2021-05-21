from django.contrib import admin
from django.urls import path, include
from .router import router
# from api.views import Login
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # #Simple JWT vvv    
    # path('api/token/', TokenObtainPairView.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view()),
    # #Simple JWT ^^^
    # path('api/user/', include('users.urls', namespace='users')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # path('token/obtain/$', Login.as_view(), name='authenticate-login'),
    # path('token/refresh/', TokenRefresh.as_view()),
    # path('token/verify/', verify_jwt_token),
    
    

]