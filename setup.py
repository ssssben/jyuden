from setuptools import setup
import os
from glob import glob
from setuptools import setup

package_name = 'jyuden'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ben fang',
    maintainer_email='vlongbf@gmail.com',
    description='充電残量を表示',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'batterytalker = jyuden.batterytalker:main',
            'batterylistener = jyuden.batterylistener:main',
        ],
    },
)
