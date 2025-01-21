import requests

API_TOKEN_QIITA = "YOUR QIITA TOKEN"
API_TOKEN_NOTION ="YOUR NOTION TOKEN"

API_ID_DB = "YOUR DATABASE ID"

API_URL_ITEMS = "https://qiita.com/api/v2/authenticated_user/items"
API_URL_USER = "https://qiita.com/api/v2/users/{USERNAME}"
API_URL_DB_POST = "https://api.notion.com/v1/pages"
API_URL_DB_QUERY = f"https://api.notion.com/v1/databases/{API_ID_DB}/query"

API_HEADERS_QIITA = {
    "Authorization": f"Bearer {API_TOKEN_QIITA}"
}

API_HEADERS_NOTION = {
    "Authorization": f'Bearer {API_TOKEN_NOTION}',
    "Notion-Version": '2022-06-28'
}

res_user = requests.get(API_URL_USER)
num_page = 10
num_count = res_user.json()["items_count"]
num_items =  num_count// num_page
list_allitem = []
list_itemid = []

for i in range(num_items + 1):
    res_articles = requests.get(f'{API_URL_ITEMS}?page={i + 1}&per_page={num_page}', headers=API_HEADERS_QIITA)
    for l, item in enumerate(res_articles.json()):
        data = {
            "id": num_count - ((num_page * i) + l),
            "title":item["title"],
            "url":item["url"],
            "date":item["created_at"]
        }
        list_allitem.append(data)

list_allitem = sorted(list_allitem, key=lambda x : x["id"])


for l in requests.post(API_URL_DB_QUERY, headers=API_HEADERS_NOTION).json()["results"]:
    list_itemid.append(l['properties']['ID']["number"])

for db_new in list_allitem:
    try:
        list_itemid.index(db_new["id"])
        print(f'{db_new["id"]}:Skipped (Already Exists)')
    except:
        data_db = {
          "parent": { "database_id": API_ID_DB },
          "properties": {
                  "ID": {
                      "number":db_new["id"]
                  },
                  "記事タイトル": {
                      "title": [{"type":"text","text": {"content":db_new["title"]}}]
                  },
                  "記事URL": {
                      "url": db_new["url"]
                  },
                  "作成日": {
                      "date": {
                              "start": db_new["date"]
                            }
                  }
              }
        }
        res_db = requests.post(API_URL_DB_POST, json=data_db, headers=API_HEADERS_NOTION)
        if(res_db.ok):
            print(f'{db_new["id"]}:Posted (Succeed))')
        else:
            print(f'{db_new["id"]}:Skipped (Faild)')
