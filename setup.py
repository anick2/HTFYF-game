from setuptools import setup, find_packages
import subprocess

subprocess.run(["mkdir", "-p", "HTFYF/ru/LC_MESSAGES"])
subprocess.run(["msgfmt", "-o", "HTFYF/ru/LC_MESSAGES/locale.mo",
                "HTFYF/ru.po"])

setup(
    name="HTFYF",
    version="0.0.1",
    author="Anikevich Yuliya, Alieva Elvira, Dugin Andrey",
    author_email="alieva.elwira@mail.ru",
    description="Game",
    url="https://github.com/anick2/HTFYF-game",
    install_requires=["pygame"],
    packages=find_packages(),
    include_package_data=True
)