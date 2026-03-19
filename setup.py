from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='netbox-plugin-dhcp',
    version='0.1.3',
    description='NetBox plugin for managing Kea DHCP configuration per ConnectServer VM',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ConnectedCare GmbH',
    author_email='',
    url='https://github.com/TDL-Bewatec/netbox-plugin-dhcp',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    zip_safe=False,
)