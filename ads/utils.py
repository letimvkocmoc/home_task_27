import csv
import json


def csv_to_json(csv_filename, json_filename, model):

    result = []

    with open(csv_filename, encoding='utf-8') as csvfile:

        for rows in csv.DictReader(csvfile):
            del rows['id']

            if 'price' in rows:
                rows['price'] = int(rows['price'])

            if 'is_published' in rows:
                if rows['is_published'] == 'TRUE':
                    rows['is_published'] = True
                else:
                    rows['is_published'] = False

            if 'location_id' in rows:
                rows['location'] = [rows['location_id']]
                del rows['location_id']

            result.append({'model': model, 'fields': rows})

    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(result, ensure_ascii=False))


csv_to_json('../data/data_28/category.csv', '../data/data_28/category.json', 'ads.category')
csv_to_json('../data/data_28/ad.csv', '../data/data_28/ad.json', 'ads.ad')

csv_to_json('../data/data_28/user.csv', '../data/data_28/user.json', 'users.user')
csv_to_json('../data/data_28/location.csv', '../data/data_28/location.json', 'users.location')


