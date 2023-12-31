import os
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Lans License File Detect Tool')
    #parser.add_argument('-u', '--user', required=True,
    #                    help='***required*** Put your username to login to Bugdb service')
    #parser.add_argument('-p', '--password', required=True,
    #                    help='***required*** Put your user password to login to Bugdb service')
    #parser.add_argument('-b', '--url', required=True,
    #                    help='***required*** Put Bugdb api url (production or staging)')
    #parser.add_argument('action', choices=['create', 'get', 'generate_notes', 'post_notes'],
    #                    help='***required*** Bugz tool supported actions')
    #parser.add_argument('--cve', metavar=('CVE-YYYY-NNNN'), nargs='*',
    #                    help='CVE-YYYY-NNNN'),
    #parser.add_argument('--arch', metavar=('ARCHITECTURE'),
    #                    help='ex: x86_64, aarch64'),
    #parser.add_argument('--path', metavar=('(JENKINS)BUILD_LOG_PATH'),
    #                    help='path to build.log'),
    #parser.add_argument('--feature', action='store_true')
    #parser.add_argument('--no-feature', dest='feature', action='store_false')
    parser.add_argument('action', choices=['name', 'version', 'longver'],
                        help='***required*** types to process the package name')
    #parser.add_argument('--package', '-p', nargs='?',
    #                    help='looking for specific package')
    parser.add_argument('--package', '-p',
                        help='looking for specific package')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='debug mode')
    #parser.set_defaults(feature=True)
    return parser
