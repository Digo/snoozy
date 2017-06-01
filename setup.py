from setuptools import setup, find_packages

version = '1.0'

setup(name='snoozy',
      version=version,
      description='A decorator for creating lazy properties in Python.',
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='decorator lazy attribute property',
      author='Chuong Ngo',
      author_email='cngo.github@gmail.com',
      url='https://github.com/cngo-github/snoozy',
      license='MIT License',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      test_suite='snoozy.tests',
)
