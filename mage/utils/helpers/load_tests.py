from pandas import DataFrame


def test_output(output, *args) -> None:
    """
    testing if output is empty
    """
    assert output is not None, 'The output is empty'


def test_output_type(output, *args) -> None:
    """
    testing if output is a pandas dataframe
    """
    assert type(output) is DataFrame, "The output is not a dataframe"
