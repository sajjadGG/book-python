Func About
==========


Rationale
---------
* https://docs.sqlalchemy.org/en/stable/core/functions.html


Functions
---------
.. csv-table:: SQL and Generic Functions
    :widths: 20,80
    :header: "Object", "Name Description"

    "``AnsiFunction``",          "Define a function in 'ansi' format, which doesn't render parenthesis"
    "``array_agg``",             "Support for the ARRAY_AGG function"
    "``char_length``",           "The CHAR_LENGTH() SQL function"
    "``coalesce``",              ""
    "``concat``",                "The SQL CONCAT() function, which concatenates strings"
    "``count``",                 "The ANSI COUNT aggregate function. With no arguments, emits COUNT *"
    "``cube``",                  "Implement the CUBE grouping operation"
    "``cume_dist``",             "Implement the cume_dist hypothetical-set aggregate function"
    "``current_date``",          "The CURRENT_DATE() SQL function"
    "``current_time``",          "The CURRENT_TIME() SQL function"
    "``current_timestamp``",     "The CURRENT_TIMESTAMP() SQL function"
    "``current_user``",          "The CURRENT_USER() SQL function"
    "``dense_rank``",            "Implement the dense_rank hypothetical-set aggregate function"
    "``Function``",              "Describe a named SQL function"
    "``FunctionAsBinary``",      ""
    "``FunctionElement``",       "Base for SQL function-oriented constructs"
    "``GenericFunction``",       "Define a 'generic' function"
    "``grouping_sets``",         "Implement the GROUPING SETS grouping operation"
    "``localtime``",             "The localtime() SQL function"
    "``localtimestamp``",        "The localtimestamp() SQL function"
    "``max``",                   "The SQL MAX() aggregate function"
    "``min``",                   "The SQL MIN() aggregate function"
    "``mode``",                  "Implement the mode ordered-set aggregate function"
    "``next_value``",            "Represent the 'next value', given a Sequence as its single argument"
    "``now``",                   "The SQL now() datetime function"
    "``OrderedSetAgg``",         "Define a function where the return type is based on the sort expression type as defined by the expression passed to the FunctionElement.within_group() method"
    "``percent_rank``",          "Implement the percent_rank hypothetical-set aggregate function"
    "``percentile_cont``",       "Implement the percentile_cont ordered-set aggregate function"
    "``percentile_disc``",       "Implement the percentile_disc ordered-set aggregate function"
    "``random``",                "The RANDOM() SQL function"
    "``rank``",                  "Implement the rank hypothetical-set aggregate function"
    "``register_function``",     "Associate a callable with a particular func. name"
    "``ReturnTypeFromArgs``",    "Define a function whose return type is the same as its arguments"
    "``rollup``",                "Implement the ROLLUP grouping operation"
    "``ScalarFunctionColumn``",  ""
    "``session_user``",          "The SESSION_USER() SQL function"
    "``sum``",                   "The SQL SUM() aggregate function"
    "``sysdate``",               "The SYSDATE() SQL function"
    "``user``",                  "The USER() SQL function"
