from setuptools import setup, find_packages

with open('README.md') as fileobj:
        description = fileobj.read()

setup(
    name='nse_live_stocks',
    version='0.6',
    author="Akhil Kodati",
    author_email="akhilkodati@yahoo.com",
    packages=find_packages(),
    install_requires=[
        'requests>=2.23.0'
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)