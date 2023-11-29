from simple_module.utils.fetch_food import fetch_food_generic


def get_food_list(page_number, page_size):
    params = {
        'pageNumber': page_number,
        'pageSize': page_size
    }
    return fetch_food_generic(params, 'v1/foods/list')


def get_food_list_by_query(query, page_number, page_size):
    params = {
        'query': query,
        'pageNumber': page_number,
        'pageSize': page_size
    }
    return fetch_food_generic(params, 'v1/foods/search')


if __name__ == "__main__":
    data = get_food_list_by_query('apple', 1, 2)
    print(data)
