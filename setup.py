# -*- coding: utf-8 -*-
import distutils.core
try:
    import setuptools
except ImportError:
    pass

version = "1.0.0"

setup(
  name="kit-iot-wearable",
  version=version,
  install_requires=[
    "PyBluez"
  ],
  packages=['wearable'],
  author="Vitor Leal",
  author_email="vitor@telefonicabeta.com",
  url="https://github.com/telefonicadigital/kit-iot-wearable-python",
  license="http://opensource.org/licenses/MIT",
  description="API Bluetooth para o Kit IoT v.3 Wearable da Telefonica VIVO",
)
