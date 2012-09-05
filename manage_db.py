#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(url='postgresql://emily@0.0.0.0/my_metrics', debug='False', repository='migration_repo')
