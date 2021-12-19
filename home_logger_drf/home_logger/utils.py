import csv
import datetime

from django.http.response import HttpResponse

from home_logger_drf.home_logger import models


def create_device_csv(request, pk):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{request.user}_device_{pk}_{datetime.date.today()}.csv"'

    device = models.Device.objects.get(id=pk)
    records = device.records.all()

    writer = csv.writer(response, dialect="excel", delimiter=";")

    writer.writerow(["Device info"])
    writer.writerow(["Name", "Description", "Local IP", "Date added", "UUID"])
    writer.writerow([device.name, device.description, device.ip_address, device.date_added, device.uuid])
    writer.writerow([""])

    writer.writerow(["Timestamp", "Temp", "Humidity", "Pressure", "CO2", "eTVOC"])

    for record in records:
        writer.writerow([record.timestamp, record.temp, record.humidity, record.pressure, record.CO2, record.eTVOC])

    return response
