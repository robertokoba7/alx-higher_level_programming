#!/usr/bin/python3
"Execute safe function"

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
