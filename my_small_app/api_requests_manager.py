import requests


def get_beer_details(pk):
    """ Sends GET request to get beer information based on id(pk)

        Method:             GET
        Url:                /api/beer/pk/
        Request headers:
                            {
                                "Content-Type": "application/json",
                                "Accept": "application/json",
                            }
        Request body:       None
        Response:
                            {
                                beer.object.dict
                            }
        """
    get_url = "http://127.0.0.1:8000/api/beer/{}/".format(pk)
    response = requests.get(get_url)
    print(response.json())


get_beer_details(3)


def create_new_beer(data):
    """ Sends POST request to create new beer

        Method:             POST
        Url:                /api/beer/
        Request headers:
                        {
                            "Content-Type": "application/json",
                            "Accept": "application/json",
                        }
        Request body:       {
                                'name': '{beer_name}',
                                'beer_type': {beer_type},
                                'description' : {beer_description}
                            }
        Response:
                        {
                            201_CREATED with the newly created beer object
                        }
            """
    post_url = "http://127.0.0.1:8000/api/beer/"
    response = requests.post(url=post_url, data=data)
    print(response.json())


new_beer = {
    'name': "Kameni4ka",
    'beer_type': 'ST',
    "description": "Mnogo ailqk bira"
}

create_new_beer(new_beer)


def get_whiskey_list():
    """ Sends GET request to get whiskey objects

            Method:             GET
            Url:                /api/whiskey/
            Request headers:
                                {
                                    "Content-Type": "application/json",
                                    "Accept": "application/json",
                                }
            Request body:       None
            Response:
                                {
                                    whiskey objects dictionary
                                }
            """
    get_url = "http://127.0.0.1:8000/api/whiskey"
    response = requests.get(get_url)
    print(response.json())


get_whiskey_list()


def create_new_whiskey(data):
    """ Sends POST request to create new beer

            Method:             POST
            Url:                /api/whiskey/
            Request headers:
                            {
                                "Content-Type": "application/json",
                                "Accept": "application/json",
                            }
            Request body:       {
                                    'brand': '{whiskey_brand}',
                                    'age': {whiskey_age},
                                    'description' : {whiskey_description}
                                }
            Response:
                            {
                                201_CREATED with the newly created whiskey object
                            }
                """
    post_url = "http://127.0.0.1:8000/api/whiskey/"
    response = requests.post(url=post_url, data=data)
    print(response.json())


whiskey_data = {
    'brand': 'Black Ram',
    'age': '12',
    'description': 'Bulgarian Whiskey, very bad, do not buy it'
}
create_new_whiskey(whiskey_data)
