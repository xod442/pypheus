from distutils.core import setup
setup(
    name = 'pypheus',
    packages = ['pypheus'],
    version = '0.1.1',
    description = 'A python binding to work with the Morpheus API',
    author = 'Rik Kauffman',
    author_email = 'rick@rickkauffman.com',
    url = 'https://github.com/xod442/pypheus',
    download_url = 'https://github.com/xod442/pypheus/archive/refs/tags/v.0.1.1.tar.gz',
    keywords = ['morpheus', 'api', 'python'],
    install_requires=[            # I get to this in a second
          'requests',
          'urllib3',
      ],
    classifiers = [],
)
