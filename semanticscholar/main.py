import requests
import json
import constants
import time
import csv

'''
JSON: Shift + Option + F  

1 request per second for the following endpoints:
/paper/batch
/paper/search
/recommendations
10 requests / second for all other calls
'''

def get_query_from_keywords(file_name):
    with open(file=file_name, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    return ' | '.join(f'"{w}"' for w in data[0])

def or_(qrs):
    return ' | '.join(qrs)

def and_(qrs):
    return '(' + ' '.join(qrs) + ')'

BASE_URL   = 'https://api.semanticscholar.org/graph/v1/paper/search/bulk/'
FIELDS     = 'title,abstract'
SORT_FIELD = 'publicationDate:desc'

KEYWORDS_SHORT = 'Keywords List - Short Version.csv'
KEYWORDS_LONG = 'Keywords List - Long Version.csv'

FILE_NAME  = 'dataset.json'
SLEEP_TIME = 2

HEADERS = {
    'Content-Type': 'application/json', 
    'x-api-key': constants.API_KEY  
}

# In each call a different 'token' is passed as part of the parameters
query_params = {
    'query': get_query_from_keywords(file_name=KEYWORDS_SHORT),
    'fields': FIELDS,
    'sort': SORT_FIELD,
}

def get_abstract_data_batch():
    # Send the API request and store the response in a variable
    # print(query_params)
    response = requests.get(BASE_URL, params=query_params, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    cnt   = 0
    total = 0
    id    = 1

    while True:
        cnt = cnt + 1
        print(f"\nCALL [{cnt}]")
        res = get_abstract_data_batch()

        if res is None:
            print("'res' is None!")
            # Try the same call several times when the res is None
            for i in range(3):
                res = get_abstract_data_batch()
                if res is not None:
                    break
            if res is None:
                break

        # Print info only in the first pass
        if cnt == 1:
            print(f"Approx. num of papers: {res['total']}")

        time.sleep(SLEEP_TIME)
        
        # Store the data
        with open(FILE_NAME, "a") as outfile:
            if res['data'] is None:
                break

            data = res['data']
            total = total + len(data)
            print(f"Number of papers returned: {len(data)}; total number of papers: {total}")

            for jsonObj in data:
                # Only papers with abstract
                if 'abstract' in jsonObj and jsonObj['abstract'] is not None:
                    # Add 'id'
                    new_jsonObj = {'id': id}
                    new_jsonObj.update(jsonObj)

                    id = id + 1
                    json.dump(new_jsonObj, outfile)
                    outfile.write('\n')

        # Get the next batch with the 'continuation token'
        if 'token' in res:
            query_params['token'] = res['token']
        else:
            print('\n\nDONE!')
            break

if __name__ == "__main__":
    main()


