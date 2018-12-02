import json

with open('tunisia.json') as f:
    data = json.load(f)
    d = dict()
    for item in data["objects"]["delegations"]["geometries"]:
        try:
            if(item['properties']['circo_na_1'][-1].isdigit()):
                d[item['properties']['circo_na_1'][:-2]].append(item)
            else:
                d[item['properties']['circo_na_1']].append(item)
        except KeyError:
            if(item['properties']['circo_na_1'][-1].isdigit()):
                d[item['properties']['circo_na_1'][:-2]] = [item]
            else:
                d[item['properties']['circo_na_1']] = [item]
    for key, value in d.items():
        delegate = dict()
        delegate['type'] = data['type']
        delegate['transform'] = data['transform']
        delegate['arcs'] = data['arcs']
        delegate['objects'] = {
            'delegates': {
                "type": "GeometryCollection",
                'geometries': value
            }
        }
        with open(value[0]['properties']['gov_name_f']+'.json', 'w', encoding='utf8') as fp:
            json.dump(delegate, fp, ensure_ascii=False)
