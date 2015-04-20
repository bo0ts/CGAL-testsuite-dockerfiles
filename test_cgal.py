#!/usr/bin/env python2
# Copyright (c) 2015 GeometryFactory (France). All rights reserved.
# All rights reserved.
#
# This file is part of CGAL (www.cgal.org).
# You can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# Licensees holding a valid commercial license may use this file in
# accordance with the commercial license agreement provided with the software.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#
# Author(s)     : Philipp Moeller

import argparse
import os
from os import path
import urllib2

cgal_release_url='https://cgal.geometryfactory.com/CGAL/Members/Releases/'

def get_latest():
    # Better error handling
    response = urllib2.urlopen(cgal_release_url + 'LATEST')
    return response.read()

def get_cgal(latest):
    # Better error handling
    response = urllib2.urlopen(cgal_release_url + latest)
    return ''

def main():
    parser = argparse.ArgumentParser(
        description='''This script launches docker containers which run the CGAL testsuite.''')
    parser.add_argument('--testsuite', metavar='/path/to/testsuite',
                        help='Absolute path where the release is going to be stored.',
                        default=os.path.abspath('./testsuite'))
    parser.add_argument('--testresults', metavar='/path/to/testresults',
                        help='Absolute path where the testresults are going to be stored.',
                        default=os.path.abspath('./testresults'))
    parser.add_argument('--upload-results', action='store_true', help='Actually upload the test results.')
    parser.add_argument('--use-local', action='store_true', help='Actually upload the test results.')
    # TODO make internal releases and latest public?
    parser.add_argument('--user', help='Username for CGAL Members')
    parser.add_argument('--passwd', help='Password for CGAL Members')
    # TODO Add the default by parsing docker ps
    parser.add_argument('--containers', nargs='*', help='List of containers to launch, defaults to all prefixed with cgal-testsuite-dockerfiles')

    args = parser.parse_args()
    assert os.path.isabs(args.testsuite)
    assert os.path.isabs(args.testresults)

    # Prepare urllib to use the magic words
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, cgal_release_url, args.user, args.passwd)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    if not args.use_local:
        print 'Downloading CGAL'
        latest = get_latest()
        get_cgal(latest)
        # unzip_cgal
    else:
        print 'Using local CGAL'

    # launch_containers
    # upload_results


if __name__ == "__main__":
    main()