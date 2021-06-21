from setuptools import find_packages, setup

setup(
    name='demo',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask-restful-swagger-3==0.4.6',
    ],
)