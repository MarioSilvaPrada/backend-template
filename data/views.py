import ftplib
import xlrd
import json
from datetime import datetime
import logging


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import EnergyPrice

files_map = [{
    "cwd": '/Elspot/Elspot_prices/Sweden/SE4_Malmo/',
    "file": 'malmo22.xls',
    "region": "SE4"
}]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_energy_prices(request):
    f = ftplib.FTP("ftp.nordpoolgroup.com")
    f.login("reampab", "rea593?")

    files = []

    data = {
        "SE1": {},
        "SE2": {},
        "SE3": {},
        "SE4": {}
    }

    for item in files_map:
        f.cwd(item["cwd"])
        f.dir(files.append)
        filename = item["file"]
        local_file = open(filename, 'wb')
        f.retrbinary("RETR " + filename, local_file.write)
        local_file.close()
        f.quit()

        region = item["region"]

        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_index(0)
        for rowx in range(6, sheet.nrows):
            row = sheet.row_values(rowx)[0:26]
            if isinstance(row[0], float):
                date = datetime(*xlrd.xldate_as_tuple(row[0], 0))
                if date not in data[region]:
                    row.pop(0)

                    values = [item for item in row if item != '']
                    if len(values):
                        region_values[region] = values
                        data[region][str(date)] = values

        logging.warning(data)
        print(data)

    # f.cwd('/Elspot/Elspot_prices/Sweden/SE4_Malmo/')
    # f.dir(files.append)

    # filename = 'malmo22.xls'
    # local_file = open(filename, 'wb')
    # f.retrbinary("RETR " + filename, local_file.write)

    # local_file.close()
    # f.quit()

    # workbook = xlrd.open_workbook(filename)
    # sheet = workbook.sheet_by_index(0)

    # for rowx in range(6, sheet.nrows):
    #     row = sheet.row_values(rowx)[0:26]
    #     if isinstance(row[0], float):
    #         date = datetime(*xlrd.xldate_as_tuple(row[0], 0))
    #         if date not in data:
    #             row.pop(0)
    #             values = [item for item in row if item != '']
    #             if len(values):
    #                 data[str(date)] = values

    # EnergyPrice.objects.create(
    #     date=date, values=json.dumps(values))

    return Response({"files": files, "rows": data}, status=200)
