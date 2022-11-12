
import logging
import requests
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
from .models import EnodeTokenModel
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response


username = getattr(settings, "ENODE_CLIENT_ID", None)
password = getattr(settings, "ENODE_CLIENT_SECRET", None)


def generate_enode_token():
    if username and password:
        url = 'https://oauth.sandbox.enode.io/oauth2/token'
        auth = HTTPBasicAuth(username, password)
        data = {"grant_type": "client_credentials"}
        response = requests.post(url, auth=auth, data=data)
        data = response.json()

        now = datetime.today()
        expires_in_date = now + timedelta(seconds=data['expires_in'])

        params = {
            "access_token": data['access_token'],
            "expires_in": data['expires_in'],
            "scope": data['scope'],
            "token_type": data['token_type'],
            "expires_date": expires_in_date
        }

        return params


def get_token():
    Token = EnodeTokenModel.objects.all().exists()
    if not Token:
        params = generate_enode_token()
        EnodeTokenModel.objects.create(**params)
        return params['access_token']

    current_token = EnodeTokenModel.objects.all()[0]
    if current_token.is_token_expired():
        params = generate_enode_token()
        current_token.access_token = params['access_token']
        current_token.expires_in = params['expires_in']
        current_token.scope = params['scope']
        current_token.token_type = params['token_type']
        current_token.expires_date = params['expires_date']
        current_token.save()
        return params['access_token']

    return current_token.access_token


def set_enode_endpoint(request, endpoint, method='GET', data=None):
    token = get_token()
    if token:
        user_id = request.user.id
        url = f'https://enode-api.sandbox.enode.io/{endpoint}'
        headers = {"Authorization": f"Bearer {token}",
                   "Enode-User-Id": f"{user_id}"}
        if method == 'GET':
            response = requests.get(url, headers=headers)
        if method == 'POST':
            response = requests.post(url, headers=headers, json=data)
        if method == 'PUT':
            response = requests.put(url, headers=headers, json=data)
        data = response.json()
        status_code = response.status_code
        return Response(data, status=status_code)
    return Response({"message": "failed to get Enode token"}, status=status.HTTP_400_BAD_REQUEST)


def set_webhook_endpoint(request, endpoint, method='PUT', data=None):
    token = get_token()
    logging.warning(token)
    if token:
        url = f'https://enode-api.sandbox.enode.io/{endpoint}'
        headers = {"Authorization": f"Bearer {token}",
                   "Accept": "application/json"}
        if method == 'GET':
            response = requests.get(url, headers=headers)
        if method == 'POST':
            response = requests.post(url, headers=headers, json=data)
        if method == 'PUT':
            response = requests.put(url, headers=headers, json=data)
        data = response.json()
        status_code = response.status_code
        return Response(data, status=status_code)
    return Response({"message": "failed to get Enode token"}, status=status.HTTP_400_BAD_REQUEST)
