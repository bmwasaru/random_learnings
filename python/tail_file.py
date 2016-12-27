"""
    A python implementation of Unix "tail -f | grep command"
"""


import time


def tail(file):
    """Mimic the UNIX 'tail -f' used to monitor log files"""
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.001)
            continue
        yield line


def grep(lines, search_text):
    """Look for a substring in a sequence of lines"""
    for line in lines:
        if search_text in line:
            yield line


apache_error_log = tail(open("/var/log/apache2/error.log"))
command_lines = grep(apache_error_log, "command")

for line in command_lines:
    print line,
