from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets, status
from .models import UserRole, Account, Keys, Logs, BaseModel
from .serializers import UserRoleSerializer, AccountSerializer, KeysSerializer, LogsSerializer, BaseModelSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.utils.datastructures import MultiValueDictKeyError
# import datetime
# from rest_framework.settings import api_settings

class UserRoleViewSet(viewsets.ModelViewSet):
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all()
    
class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    
class KeysViewSet(viewsets.ModelViewSet):
    serializer_class = KeysSerializer
    queryset = Keys.objects.all()
    
class LogsViewSet(viewsets.ModelViewSet):
    serializer_class = LogsSerializer
    queryset = Logs.objects.all()
    
class BaseModelViewSet(viewsets.ModelViewSet):
    serializer_class = BaseModelSerializer
    queryset = BaseModel.objects.all()


# authentication_classes = (JSONWebTokenAuthentication,)
# permission_classes = (IsAuthenticated,)

# def jwt_payload_handler_user(user):
#     exp = datetime.now() + api_settings.JWT_EXPIRATION_DELTA

#     payload = {
#         "id": user.id,
#         "date": get_user_join_date(user),
#         "username": user.username,  # needs to be in the payload for the payload to be valid
#         "messages": get_error_messages(error_type, error_content),
#         "name": get_user_info_json(user),
#         "organizations": get_orgs_json(user),
#         'exp': format(exp, 'U')
#     }

#     if api_settings.JWT_ALLOW_REFRESH:
#         payload['iat'] = timegm(
#             datetime.utcnow().utctimetuple()
#         )

#     if api_settings.JWT_AUDIENCE is not None:
#         payload['aud'] = api_settings.JWT_AUDIENCE

#     if api_settings.JWT_ISSUER is not None:
#         payload['iss'] = api_settings.JWT_ISSUER

#     return payload
    
# class Login(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = AccountSerializer
      
    
#     def post(request):
#         try:
#           if request.data['username'] and request.data['password']:
#             try:
#               user = Account.objects.get(username=request.data['username'])
#             except Account.DoesNotExist:
#               return Response({'type': 'error', 'content': 'Invalid username.'}, status=status.HTTP_400_BAD_REQUEST)

#             if user:
#               if user.check_password(request.data['password']):
#                   payload = jwt_payload_handler_user(user)
#                   token = jwt_encode_handler(payload)
#                   return Response({'token': token}, status=status.HTTP_200_OK)
#               else:
#                 return Response({'type': 'error', 'content': 'Invalid password.'}, status=status.HTTP_400_BAD_REQUEST)

#         except MultiValueDictKeyError:
#           return Response({'type': 'error', 'content': 'Please provide username/password'}, status=status.HTTP_400_BAD_REQUEST)