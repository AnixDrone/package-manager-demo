from simple_module.utils.fetch_food import fetch_food_generic


def get_food_list(page_number, page_size):
    """
    Fetches food data from the USDA Food Composition Databases API
    :param page_number: the page number to fetch
    :param page_size: the number of items to fetch per page
    :return: the response from the API
    """
    # Get the API key from the environment
    params = {
        'pageNumber': page_number,
        'pageSize': page_size
    }
    return fetch_food_generic(params, 'v1/foods/list')


def get_food_list_by_query(query, page_number, page_size):
    """
    Fetches food data from the USDA Food Composition Databases API
    :param page_number: the page number to fetch
    :param page_size: the number of items to fetch per page
    :return: the response from the API
    """
    # Get the API key from the environment
    params = {
        'query': query,
        'pageNumber': page_number,
        'pageSize': page_size
    }
    return fetch_food_generic(params, 'v1/foods/search')


if __name__ == "__main__":
    data = get_food_list_by_query('apple', 1, 2)
    print(data)
