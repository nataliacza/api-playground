from pprint import pprint

import requests

json_url = "https://jsonplaceholder.typicode.com/posts"

get_posts = requests.get(json_url)

if get_posts.ok:
    result_json = get_posts.json()

    find_title = input("Provide text to search in title: ")

    titles = [item for item in result_json if find_title in item["title"]]
    if len(titles) != 0:
        print(f"Results: {len(titles)} of {len(result_json)}")
        pprint(titles)
    else:
        print(f"No results with '{find_title}' found.")

else:
    print("Unable to get data from requested source.")
