import urllib, json

def getData():
    url = "https://content.guardianapis.com/search?q=ocbc&api-key=335c72ad-092f-4b03-a101-5a0b0babfc7c"
    response = urllib.urlopen(url)
    data = json.loads(response.read())["response"]

    total_records = data["total"]
    page_size = data["pageSize"]
    pages = total_records/page_size

    if total_records % page_size != 0:
        pages += 1

    file_list = []
    for pg in range(pages):
        for dat in data["results"]:
            file = dict()
            # print page["source"]
            file["id"] = len(file_list)
            file["publish_date"] = dat["webPublicationDate"]
            file["url"] = dat["webUrl"]
            file["title"] = dat["webTitle"]
            file["content"] = ""
            file["author"] = ""
            file_list.append(file)
        # print response
    with open("data_file.json", "w") as write_file:
        json.dump(file_list, write_file)

getData()
