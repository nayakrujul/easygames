from setuptools import setup, find_packages

long_description = 'A collection of 1-player games.'

setup(
  name = 'oneplayergames',
  version = '0.0.1',
  license='Apache',
  description = 'A collection of 1-player games',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/easygames',
  download_url = '', # TODO: create release
  keywords = ['game', 'games', '1-player'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points ={
            'console_scripts': [
              
            ]
  }
)
