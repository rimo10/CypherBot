import requests


def quote_generator():
    url = "https://api.quotable.io/random"
    response = requests.request("GET", url).json()
    return {"content": response["content"], "author": response["author"]}


if __name__ == "__main__":
    print(quote_generator())
