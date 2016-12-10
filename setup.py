from setuptools import setup, find_packages


setup(
    name='valhalla',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['logbook', 'tornado', 'flask', 'click'],
    entry_points={
        'console_scripts': [
            'valhallad = valhalla.run_server:main'
        ]
    }
)