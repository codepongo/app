import db
import fetcher
import json

def import_from_github():
    paths = fetcher.from_github()
    data = []
    for path in paths:
        with open(path, 'rb') as f:
            d = json.load(f)
            if not d['fork']:
                data.append({'name':d['name'], 
                    'github':d['html_url'], 
                    'description':d['description'],
                    'update':d['updated_at'],
                    'url':d['homepage']})
    db.to_app(data)

if __name__ == '__main__':
    import_from_github()
