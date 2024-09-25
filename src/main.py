import pandas as pd
import polars as pl

def pandas_summary(filepath):
    df = pd.read_csv(filepath)
    return df['Total'].describe()

def polars_summary(filepath):
    df = pl.read_csv(filepath)
    return df.select([
        pl.col('Total').mean().alias('mean'),
        pl.col('Total').median().alias('median'),
        pl.col('Total').std().alias('std')
    ])

if __name__ == "__main__":
    print(pandas_summary('data/medals_total.csv'))
    print(polars_summary('data/medals_total.csv'))
