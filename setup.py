from setuptools import setup, find_packages

with open("README.md", "r") as f: 
    page_description = f.read()

with open("requirements.txt") as f: 
    requirements = f.read().splitlines()


setup(
    name="stat_package",
    version="0.0.1",
    author="fyobara",
    author_email="fernando.y.obara@gmail.com",
    description="O pacote disponibiliza funções para cálculo de medidas de tendência central", long_description=page_description,
    long_description_content_type="text/markdown", url="https://github.com/fyobara/statistic-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    )
    