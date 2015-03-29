import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='kb-aliuacademy-org',
    packages=['project', 'project.management', 'project.management.commands', 'web', 'web.tests', 'web.management', 'web.management.commands', 'settings'],
    package_data={
        'project': [
            'static/*.*',
            'static/css/*.*',
            'static/css/project/*.*',
            'static/img/*.*',
            'static/img/project/*.*',
            'templates/*.*',
            'templates/project/*.*',
        ],

        'web': [
            'templates/*.*',
            'templates/web/*.*',
        ],
    },
    version='0.0.21',
    description='Aliu Academy web site',
    author='Patrick Kimber',
    author_email='code@pkimber.net',
    url='git@bitbucket.org:pkimber/aliuacademy_org.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)