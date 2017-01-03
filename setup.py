from setuptools import setup


def readme():
    with open('README.rst') as file:
        return file.read()


setup(
    name='compose_diff',
    version='0.4.0',
    description='diff docker-compose files',
    long_description=readme(),
    url='http://github.com/funkwerk/compose_diff',
    author='Stefan Rohe',
    license='MIT',
    packages=['compose_diff'],
    install_requires=['pyaml'],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Environment :: Console',
        'Operating System :: OS Independent',
    ],
    keywords='docker-compose diff docker yml',
    include_package_data=True,
    scripts=['bin/compose_diff'])
