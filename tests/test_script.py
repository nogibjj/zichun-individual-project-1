from script import pandas_summary, polars_summary

def test_pandas_summary():
    assert pandas_summary('../data/medals_total.csv') is not None

def test_polars_summary():
    assert polars_summary('../data/medals_total.csv') is not None
