import http.client
import json
from pandas import DataFrame
from mage_ai.data_preparation.shared.secrets import get_secret_value
import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
current_date = datetime.date.today()
if current_date.month > 6:
    CURRENT_SEASON_STR = str(current_date.year)
else:
    CURRENT_SEASON_STR = str(current_date.year - 1)
API_ENDPOINT = 'fixtures'
API_QUERY = '&'.join([f'season={CURRENT_SEASON_STR}',
                      'league=61'])


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': get_secret_value('api_key'),
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }
    generated_api_query = f"/v3/{API_ENDPOINT}?{API_QUERY}"
    print(f'targeting:"{generated_api_query}')
    conn.request("GET", generated_api_query, headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(data)

    data_dec = data.decode("utf-8")
    data_dict = json.loads(data_dec)
    print(json.dumps(data_dict, indent=4))

    df = DataFrame.from_dict(data_dict['response'])
    print(df)

    return df


@test
def test_output(output, *args) -> None:
    """
    testing if output is empty
    """
    assert output is not None, 'The output is empty'


@test
def test_output_type(output, *args) -> None:
    """
    testing if output is a pandas dataframe
    """
    assert type(output) is DataFrame, "The output is not a dataframe"
