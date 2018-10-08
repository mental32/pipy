import os
import time
import argparse
import subprocess
import contextlib

__version__ = '0.0.1'

_BASH_DEPENDENCIES = '''
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
sudo apt-get install libncursesw5-dev libgdbm-dev libc6-dev
sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
sudo apt-get install libssl-dev openssl
sudo apt-get install libffi-dev
'''

_BASH_FILE = '''
wget https://www.python.org/ftp/python/{v}/Python-{v}.tgz
tar xzvf Python-{v}.tgz
rm -f Python-{v}.tgz
cd Python-{v}
./configure
make
sudo make altinstall
cd ..
rm -rf Python-{v}
'''

@contextlib.contextmanager
def install(version):
    fp = 'pipy_{v}_{t}.sh'.format(v=version, t=int(time.time()))

    with open(fp, 'w') as inf:
        inf.write(_BASH_FILE.format(v=version).strip())
        inf.write('\n')

    yield fp

def main(args):
    if os.getuid():
        print('you cannot perform this operation unless you are root.')
        return

    with install(args.version) as fp:
        if args.deps:
            subprocess.check_output(' && '.join(cmd for cmd in _BASH_DEPENDENCIES.split('\n')), shell=True)

        subprocess.check_output('bash %s' % fp, shell=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('version', metavar='version', help='The version to try and install.')
    parser.add_argument('--all', dest='deps', action='store_true', default=False, help='Install all dependencies.')
    main(parser.parse_args())
