from distutils.core import setup

AUTHOR = "Lissajous Fans"

setup(name="lissapi",
      version="0.1.0",
      author=AUTHOR,
      packages=["lissapi"],
      install_requires=["PyQt5", "pyqtchart", "pandas"],
      package_dir={"lissapi": "src/api/"})

# setup(name="Lissajous",
#       version="0.1.1",
#       author=AUTHOR,
#       packages=["Lissajous"],
#       package_dir={"Lissajous": "src/"},
#       install_requires=["PyQt5", "pyqtchart", "pandas", "pycountry", "lissapi"],
#       scripts=["main.py"])
