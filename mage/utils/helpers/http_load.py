"helpfunction to retrieve data from an api, converts to df if given a json"

import http.client
import json
from pandas import DataFrame
from urllib.error import HTTPError


def raise_for_status(response: http.client.HTTPResponse) -> None:
    """
    checks if http response has status 200, otherwise raises error
    :param response: the http response object
    :return: None
    """
    if response.status != 200:
        raise HTTPError(
            url=response.geturl(),
            code=response.status,
            msg=response.reason,
            hdrs=response.headers,
            fp=response.fp,
        )


def http_load_json_data(api_host: str,
                        api_host_suffix: str,
                        api_endpoint: str,
                        api_query: str,
                        api_key: str) -> DataFrame:
    """
    loads data from given endpoint, converts json object to dict
    and transforms into a dataframe, raises for errors given by the api
    :param api_host: host of the api, f.e.api-football-v1.p.rapidapi.com
    :param api_host_suffix: suffix of the host needed to query, this might be versions f.e. v3/
    :param api_endpoint: endpoint which is going to be requested f.e. fixtures
    :param api_query: query which is used to filter results within the api, f.e. livegames=true
    :param api_key: the key needed to be provided within the header
    :return: returns the response['response'] as dataframe
    """
    # building connection
    conn = http.client.HTTPSConnection(api_host)
    # provide connection metadata
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': api_host
    }
    generated_api_query = f"/{api_host_suffix}{api_endpoint}?{api_query}"
    print(f'targeting:"{generated_api_query}')

    # requesting the data
    conn.request("GET", generated_api_query, headers=headers)

    # handle api response
    res = conn.getresponse()
    raise_for_status(res)
    data = res.read()
    print(data)

    # transform the response data
    data_dec = data.decode("latin-1")
    data_dict = json.loads(data_dec)
    print(json.dumps(data_dict, indent=4))

    df = DataFrame.from_dict(data_dict['response'])
    print(df.head(20))

    return df
