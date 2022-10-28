import json
import logging

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .actions import get_token, set_enode_endpoint
from core.tasks import sample_task


@api_view(['GET'])
def enode_token_view(request):
    token = get_token()
    sample_task()
    logging.info(token)
    if token:
        return Response({"current_token": token}, status=status.HTTP_200_OK)
    return Response({"message": "fail to get token"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def enode_link_view(request, id=None):
    user_id = request.user.id
    return set_enode_endpoint(request, f'users/{user_id}/link', 'POST')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_enode_user(request, id=None):
    return set_enode_endpoint(request, 'me')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vehicle(request, id=None):
    return set_enode_endpoint(request, 'vehicles')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vehicle_id(request, vehicle_id, field=None):
    endpoint = f'vehicles/{vehicle_id}'
    if field:
        endpoint += f'/{field}'
    return set_enode_endpoint(request, endpoint)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_charger(request):
    endpoint = f'chargers'
    return set_enode_endpoint(request, endpoint)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_charger_action(request, action_id):
    endpoint = f'vehicles/actions/{action_id}'
    return set_enode_endpoint(request, endpoint)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_schedules(request):
    endpoint = 'schedules'
    if request.method == 'POST':
        body = json.loads(request.body)
        return set_enode_endpoint(request, endpoint, method='POST', data=body)
    return set_enode_endpoint(request, endpoint)


# {
#   "targetId": "601a28bf-eb2d-49e8-8e95-22b4857e3a7a",
#   "chargingLocationId": null,
#  "defaultShouldCharge": false,
#   "rules": [
#     {
#       "shouldCharge": true,
#       "hourMinute": {
#         "from": "22:00",
#         "to": "06:00"
#       },
#       "weekdays": [0]
#     }
#   ],
#   "targetType": "vehicle"
# }

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_car_health(request):
    endpoint = f'health/ready'
    return set_enode_endpoint(request, endpoint)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_available_vendors(request):
    endpoint = f'health/vehicles'
    return set_enode_endpoint(request, endpoint)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def control_charging(request, vehicle_id):
    endpoint = f'vehicles/{vehicle_id}/charging'
    body = json.loads(request.body)
    return set_enode_endpoint(request, endpoint, method='POST', data=body)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def webhook(request):
    endpoint = 'webhooks/firehose/test'
    return set_enode_endpoint(request, endpoint, method='POST')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def schedule_statistics(request):
    endpoint = 'statistics/charging'
    return set_enode_endpoint(request, endpoint)
