cgal-testsuite-dockerfiles
==========================

Dockerfiles and tools to run the CGAL testsuite inside containers.

Initially you need to build the images which you would like to use:

    cd CentOS-6
    docker build -t cgal-testsuite/centos6
    cd ..

To run the testsuite using this image:

    ./test_cgal.py --username **** --passwd **** --images cgal-testsuite/centos6

If you would like to use an already extraced internal release:

    ./test_cgal.py --use-local --testsuite /path/to/release --images cgal-testsuite/centos6

SELinux issues
--------------
On Linux system using SELinux (such as the default setting for the recent
versions of Fedora, RHEL, and CentOS), you might need to relabel the host
files and directories used as volumes by the containers:

    chcon -Rt svirt_sandbox_file_t ./docker-entrypoint.sh ./testsuite ./testresults

If you use the options `--testsuite /path/to/testsuite` or `--testresults /path/to/testresults`, then the pointed directories must also be relabeled with `svirt_sandbox_file_t`:

    chcon -Rt svirt_sandbox_file_t /path/to/testresults /path/to/testresults
