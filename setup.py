from distutils.core import setup

requires = [
    'python-gnupg',
]

setup(
    name='pysnippets',
    version='0.1',
    packages=['pysnippets'],
    install_requires=requires,
    # py_modules=['django'],
    url='',
    license='The MIT License (MIT)',
    author='aleksey.osadchuk',
    author_email='aleksey.osadchuk@redsolution.ru',
    description='Helper functions in different python projects',
)
