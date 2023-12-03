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

    :param api_host:
    :param api_host_suffix:
    :param api_endpoint:
    :param api_query:
    :param api_key:
    :return:
    """

    conn = http.client.HTTPSConnection(api_host)

    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': api_host
    }
    generated_api_query = f"/{api_host_suffix}{api_endpoint}?{api_query}"
    print(f'targeting:"{generated_api_query}')
    conn.request("GET", generated_api_query, headers=headers)

    res = conn.getresponse()
    raise_for_status(res)
    data = res.read()
    print(data)

    data_dec = data.decode("latin-1")
    data_dict = json.loads(data_dec)
    print(json.dumps(data_dict, indent=4))

    df = DataFrame.from_dict(data_dict['response'])
    print(df.head(20))

    return df
