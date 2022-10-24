import requests
import os
from requests.auth import HTTPBasicAuth

from rest_framework.views import APIView
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import EnodeTokenSerializer
from django.conf import settings

username = getattr(settings, "ENODE_CLIENT_ID", None)
password = getattr(settings, "ENODE_CLIENT_SECRET", None)


@api_view(['GET'])
def enode_token_view(request):
    if username and password:
        url = 'https://oauth.sandbox.enode.io/oauth2/token'
        auth = HTTPBasicAuth(username, password)
        data = {"grant_type": "client_credentials"}
        response = requests.post(url, auth=auth, data=data)
        data = response.json()

        urlLink = 'https://enode-api.sandbox.enode.io/users/1ab23cd4/link'
        headers = {"Authorization": f"Bearer {data['access_token']}",
                   "Content-Type": "application/json"}

        linkResponse = requests.post(urlLink, headers=headers)

        return Response({"data": data, "link": linkResponse.json()})
    return Response({"message": "fail to get token"})


class EnodeTokenView(APIView):
    # queryset = Project.objects.all()
    serializer_class = EnodeTokenSerializer
    http_method_names = ['get', 'post', 'head']


enode_token = EnodeTokenView.as_view()
