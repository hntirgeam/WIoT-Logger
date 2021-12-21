import csv
import datetime

from django.http.response import HttpResponse

from home_logger_drf.home_logger import models


def create_device_csv(request, pk):
    device = models.Device.objects.get(id=pk)
    records = device.records.all()

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{request.user}_device_{device.name}_{datetime.date.today()}.csv"'

    writer = csv.writer(response, dialect="excel", delimiter=";")

    writer.writerow(["Device info"])
    writer.writerow(["Name", "Description", "Local IP", "Date added", "api_key"])
    writer.writerow([device.name, device.description, device.ip_address, device.date_added, device.api_key])
    writer.writerow([""])

    writer.writerow(["Timestamp", "Temp", "Humidity", "Pressure", "CO2", "eTVOC"])

    for record in records:
        writer.writerow([record.timestamp, record.temp, record.humidity, record.pressure, record.co2, record.etvoc])

    return response
