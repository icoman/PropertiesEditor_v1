import os, sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
                     "include_msvcr": True,
                     "silent": True,
                     "build_exe":os.getenv("DIR","App"),
                     "zip_include_packages": "*",
                     "zip_exclude_packages": "",
                     "excludes": ["tkinter","scipy","cv2","PySide","numpy","PyQt4"],
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Console"
if 1:
    if sys.platform == "win32":
        base = "Win32GUI"

target = Executable(
    script="main.py", base=base #, icon="is.ico"
    )
setup(  name = "Python application",
        version = "0.1",
        description = "(C) 2019 Ioan Coman",
        options = {"build_exe": build_exe_options},
        executables = [target])