import ftplib
import xlrd
import json
from datetime import datetime


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

from .models import EnergyPrice


files_map = [
    {
        "cwd": '/Elspot/Elspot_prices/Sweden/SE1_Lulea/',
        "file": 'lulsek22.xls',
        "region": "SE1"
    },
    {
        "cwd": '/Elspot/Elspot_prices/Sweden/SE2_Sundsvall/',
        "file": 'sundsek22.xls',
        "region": "SE2"
    },
    {
        "cwd": '/Elspot/Elspot_prices/Sweden/SE3_Stockholm/',
        "file": 'stosek22.xls',
        "region": "SE3"
    },
    {
        "cwd": '/Elspot/Elspot_prices/Sweden/SE4_Malmo/',
        "file": 'malsek22.xls',
        "region": "SE4"
    }
]

username = getattr(settings, "NORDPOOL_FTP_USERNAME", None)
password = getattr(settings, "NORDPOOL_FTP_PASSWORD", None)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_energy_prices(request):
    f = ftplib.FTP("ftp.nordpoolgroup.com")
    f.login(username, password)

    data = {}

    for index, item in enumerate(files_map):
        print(index, item)
        f.cwd(item["cwd"])
        filename = item["file"]
        local_file = open(filename, 'wb')
        f.retrbinary("RETR " + filename, local_file.write)
        local_file.close()
        if index + 1 == len(files_map):
            f.quit()

        region = item["region"]

        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_index(0)
        for rowx in range(6, sheet.nrows):
            row = sheet.row_values(rowx)[0:26]
            if isinstance(row[0], float):
                date = datetime(*xlrd.xldate_as_tuple(row[0], 0))
                date_string = str(date)
                row.pop(0)
                values = [item for item in row if item != '']
                if date_string not in data:
                    if len(values):
                        data[date_string] = {}
                        data[date_string][region] = []
                        data[date_string][region] = values
                else:
                    if len(values):
                        data[date_string][region] = []
                        data[date_string][region] = values

    EnergyPrice.objects.all().delete()
    for date in data.keys():
        print(date)
        format = "%Y-%m-%d %H:%M:%S"
        date_time = datetime.strptime(date, format).date()
        values = json.dumps(data[date][region])
        EnergyPrice.objects.create(
            date=date_time,
            SE1=json.dumps(data[date]["SE1"]),
            SE2=json.dumps(data[date]["SE2"]),
            SE3=json.dumps(data[date]["SE3"]),
            SE4=json.dumps(data[date]["SE4"]),
        )

    return Response(data, status=200)
