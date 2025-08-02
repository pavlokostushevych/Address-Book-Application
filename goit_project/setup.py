from setuptools import setup, find_namespace_packages


setup(
    name='goit_project',
    version='1.0',
    packages=find_namespace_packages(),
    install_requires=[
        'customtkinter', 'prompt_toolkit', 'rich'
    ],
    entry_points={
        'console_scripts': ['start_project = goit_project.gui:main',
                            'start_project_console = goit_project.main:main'],
    },
)