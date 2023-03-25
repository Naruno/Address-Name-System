from setuptools import setup


setup(name='address_name_system',
version='0.1.2',
description="""Mapping Addresses to Dynamic IPs, Simplified""",
long_description_content_type="text/markdown",
include_package_data=True,
long_description="".join(open("README.md", encoding="utf-8").readlines()),
url='https://github.com/Naruno/Address-Name-System',
author="Naruno Developers",
author_email='onur.atakan.ulusoy@naruno.org',
license='MIT',
packages=["address_name_system"],
package_dir={'':'src'},
install_requires=[
    "fire==0.5.0"
],
entry_points = {
    'console_scripts': ['ans=address_name_system.address_name_system:main'],
},
python_requires=">= 3",
zip_safe=False)