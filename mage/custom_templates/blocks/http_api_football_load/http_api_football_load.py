from mage_ai.data_preparation.shared.secrets import get_secret_value

from mage.utils.helpers import http_load
from mage.utils.helpers import load_tests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
API_ENDPOINT = 'add api endpoint here'
API_HOST = "api-football-v1.p.rapidapi.com"
API_HOST_SUFFIX = "v3/"


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    execution_date = kwargs.get('execution_date')
    current_season_str = str(execution_date.year) if execution_date.month > 6 else str(execution_date.year - 1)

    #add api serach query here
    api_query = '&'.join([f'season={current_season_str}',
                          'league=61'])

    return http_load.http_load_json_data(api_host=API_HOST,
                                         api_query=api_query,
                                         api_endpoint=API_ENDPOINT,
                                         api_key=get_secret_value('api_key'),
                                         api_host_suffix=API_HOST_SUFFIX)


@test
def test_output(output, *args) -> None:
    """
    testing if output is empty
    """
    load_tests.test_output(output,*args)


@test
def test_output_type(output, *args) -> None:
    """
    testing if output is a pandas dataframe
    """
    load_tests.test_output_type(output,*args)
