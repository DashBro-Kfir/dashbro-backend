from setuptools import find_packages, setup

setup(
    name="dashbro",
    version="1.0.0",
    description="Dashbro - A simple way to manage Grafana dashboards.",
    author="Dashbros",
    author_email="dashbro@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["sqlmodel==0.0.24", "pydantic>=2.0.0,<=2.11.7", "uvicorn==0.35.0", "fastapi==0.115.14"],
    tests_require=["ruff==0.12.3"],
    python_requires=">=3.8",
)
