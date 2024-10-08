from setuptools import setup, find_packages

setup(
    name='ophrase',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tenacity',
        'rich',
        'loguru',
        'pydantic',
        'jinja2',
        'ollama',
        'flake8',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'ophrase=ophrase.main:Main.run'
        ],
    },
)
