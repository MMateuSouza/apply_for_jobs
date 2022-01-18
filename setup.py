from setuptools import find_packages, setup

setup(
    name="password-generator-microservice",
    description="Apply For Jobs - TOTVs",
    version="1.0.0",
    author="Mateus Souza",
    author_email="mota.mateus13@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "blinker",
        "flask",
        "flask-apscheduler",
        "flask-mongoengine",
        "python-dotenv",
        "requests",
    ],
)
