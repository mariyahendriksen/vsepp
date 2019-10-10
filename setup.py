from setuptools import setup

print('Started!')
with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='vsepp',
    version="0.1",
    description='Setting up dependencies for visual-semantic embedding project',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
    ],
    author='Mariya Hendriksen',
    author_email='m.hendriksen@uva.nl',
    licanse='MIT'
)

print('Finished!')
