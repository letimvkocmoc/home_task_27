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
                if 'is_published' == 'TRUE':
                    rows['is_published'] = True
                else:
                    rows['is_published'] = False

            result.append({'model': model, 'fields': rows})

    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(result, ensure_ascii=False))


csv_to_json('../data/categories.csv', '../data/categories.json', 'ads.category')
csv_to_json('../data/ads.csv', '../data/ads.json', 'ads.ad')
