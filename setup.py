# This is what your ‘setup.py’ file should look like.

from setuptools import setup, find_packages

setup(
    name="mailman_sender_plugin", #Name
    version="1.0", #Version
    packages = ["mailman_sender_plugin", "mailman_sender_plugin.pipelines", "mailman_sender_plugin.handlers"],
    package_dir = {"mailman_sender_plugin":"."}
)