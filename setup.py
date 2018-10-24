from setuptools import setup

setup(name='dautils',
      version='0.0.2b2',
      description='Data analysis utilities for Python',
      url='https://lucidex.zangetsu.co',
      author='Naman Bishnoi',
      author_email='lucidex@zangetsu.co',
      license='MIT',
      packages=['dautils'],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose', 'nose-parameterized'],
      install_requires=[
          'appdirs',
          'landslide',
          'pandas-datareader'
      ],
      zip_safe=False)
