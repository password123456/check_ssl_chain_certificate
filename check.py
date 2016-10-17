# -*- coding: utf-8 -*-

__author__ = 'https://github.com/password123456/'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def DO_CHECK_CERTIFICATE(url):
    try:
        user_agent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36', 'Connection':'keep-alive'}
        r = requests.get(url, headers=user_agent, verify=True, timeout=05)
        result = '%s %s %s' % ( url, r.status_code, r.headers['server'])
        print '%s[-] OK::%s %s %s' % (bcolors.OKGREEN, bcolors.OKBLUE, result, bcolors.ENDC)
    except Exception as e:
        error = '%s' % e
        if 'CERTIFICATE_VERIFY_FAILED' in error:
            print '%s[-] ERROR::%s %s CERTIFICATE_VERIFY_FAILED %s' % (bcolors.WARNING, bcolors.FAIL, url, bcolors.ENDC)
    else:
        r.close()

def READ_URL():
    f = open('url.txt', 'r')

    for line in f.readlines():
        line = line.strip()
        line = 'https://%s' % line
        DO_CHECK_CERTIFICATE(line)

def main():
    READ_URL()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception, e:
        print '%s[-] Exception::%s%s' % (bcolors.WARNING, e, bcolors.ENDC)
