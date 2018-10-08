import re
from distutils.core import setup

def get_version():
  with open('pipy/__main__.py') as inf:
      match = re.search(r"((\d\.){2,5}\d)", inf.read(), re.MULTILINE)

      if match is None:
          raise RuntimeError('Version could not be found.')

return match.groups()[0]

setup(
    name='pipy',
    version=get_version(),
    description='RPi Python Installer',
)
