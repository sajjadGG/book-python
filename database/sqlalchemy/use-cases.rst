SQLAlchemy Use Cases
====================


Use Case - 0x01
---------------
* SQLAlchemy to Pandas

    from sqlalchemy import create_engine
    import pandas as pd


    # DATABASE powinen zaczynać się od sqlite:///
    DATABASE = 'sqlite:///myfile.db'

    SQL = """

        SELECT *
        FROM astronauts;

    """

    # %%timeit -r 1 -n 1
    # with create_engine(DATABASE).connect() as db:
    #    df = pd.read_sql(SQL, db)
    # 2.47 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
    #
    # %%
    # df.info(memory_usage='deep')

    with create_engine(DATABASE).connect() as db:
        df = pd.read_sql(SQL, db)

    print(df)
