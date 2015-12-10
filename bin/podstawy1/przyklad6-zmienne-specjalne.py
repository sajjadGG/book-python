def gdzie_jestem():
    print(__name__)
    print(__file__)


gdzie_jestem()



def run_HTTP_server(*args, **kwargs):
    pass


def runHTTPServer(*args, **kwargs):
    import warnings
    warnings.warn(PendingDeprecationWarning, 'You should use \'run_HTTP_server()\' instead.')
    return run_HTTP_server(*args, **kwargs)



"""
escape'owanie

\xac
\u7723
\n
\b
\r
\t
\'


"""