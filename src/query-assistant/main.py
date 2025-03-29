import requests


def query_api(user_query):
    # For now, simply hard-code a naive transformation
    transformed_query = "/destinations?query=" + user_query
    response = requests.get("https://swagger.myswitzerland.io" + transformed_query)
    return response.json()


def main():
    user_query = "What are the top destinations in Switzerland?"
    result = query_api(user_query)
    print(result)


if __name__ == "__main__":
    main()
