# coding: utf-8

'''
reference: http://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement
'''

import sys
import StringIO
import contextlib
import code
import traceback


@contextlib.contextmanager
def code_ret():
    code_stdout = StringIO.StringIO()
    sys_stdout = sys.stdout
    sys_stderr = sys.stderr

    sys.stdout = code_stdout
    sys.stderr = code_stdout

    yield code_stdout
    sys.stdout = sys_stdout
    sys.stderr = sys_stderr


def run_shell(str_code):
    python_shell = code.InteractiveInterpreter()
    try:
        compile_code = code.compile_command(str_code)
    except:
        etype, value, _ = sys.exc_info()
        exc_ret = ''.join(traceback.format_exception_only(etype, value))
        return exc_ret

    with code_ret() as ret:
        python_shell.runcode(compile_code)
    return ret.getvalue()


def run_source(source_code):
    python_interpreter = code.InteractiveInterpreter()

    with code_ret() as ret:
        python_interpreter.runsource(source_code, '<string>', 'exec')
    return ret.getvalue()
