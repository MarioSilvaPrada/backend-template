import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .actions import get_token


@api_view(['GET'])
def enode_token_view(request):
    token = get_token()
    if token:
        return Response({"current token": token}, status=status.HTTP_200_OK)
    return Response({"message": "fail to get token"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def enode_link_view(request, id=None):
    token = get_token()
    print('token', token)
    if token:
        user_id = request.user.id
        print('user_id', user_id)
        urlLink = f'https://enode-api.sandbox.enode.io/users/{user_id}/link'
        headers = {"Authorization": f"Bearer {token}",
                   "Content-Type": "application/json"}
        linkResponse = requests.post(urlLink, headers=headers)
        data = linkResponse.json()
        return Response(data, status=status.HTTP_200_OK)
    return Response({"message": "failed to get Enode token"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_enode_user(request, id=None):
    token = get_token()
    if token:
        user_id = request.user.id
        url = f'https://enode-api.sandbox.enode.io/me'
        headers = {"Authorization": f"Bearer {token}",
                   "Enode-User-Id": f"{user_id}"}
        response = requests.get(url, headers=headers)
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    return Response({"message": "failed to get Enode token"}, status=status.HTTP_400_BAD_REQUEST)
