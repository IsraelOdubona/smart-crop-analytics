import csv
from crops.models import CropData

with open('crop_data.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        year = row['year'].strip()

        if not year or year == '(blank)':
            continue

        CropData.objects.create(
            year=int(year),
            region=row['region'].strip(),
            crop=row['crop'].strip(),
            production=float(row['production']) if row['production'] else None,
            yield_amount=float(row['yield']) if row['yield'] else None
        )