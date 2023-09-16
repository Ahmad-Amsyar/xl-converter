# Multiplatform makefile replacement
# I got fed up with trying to get `make` to work on Windows

import platform, os, shutil, glob, subprocess, PyInstaller.__main__
from VARIABLES import VERSION

PROGRAM_NAME = "xl-converter"
PROGRAM_FOLDER = os.path.dirname(os.path.realpath(__file__))

def replaceLine(path, pattern, new_line):
    """Replace the first line containing a pattern."""
    if not os.path.isfile(path):
        return

    content = ""
    with open(path, "r") as file:
        content = file.readlines()
    
    for n, line in enumerate(content):
        if pattern in line:
            if line != new_line:    # If the file wouldn't be the same
                content[n] = new_line
                break   # Only one line needs to be replaced
            else:
                return
    
    with open(path, "w") as file:
        file.writelines(content)

if __name__ == '__main__':
    # Clean
    if os.path.isdir("dist"):
        shutil.rmtree("dist")

    # Important - cleans up the build folder If moved to a different platform
    if os.path.isdir("build"):  
        if os.path.isfile("build/last_built_on"):
            last_built_on = open("build/last_built_on","r")
            last_platform = last_built_on.read()
            last_built_on.close()
            
            if last_platform == f"{platform.system()}_{platform.architecture()}":
                print("[Building] Platform matches with previously compiled cache")
                pass
            else:
                print("[Building] Platform mismatch - deleting the cache")
                shutil.rmtree("build") 
                shutil.rmtree("__pycache__")
        else:
            print("[Building] \"last_built_on\" not found - deleting the cache")
            shutil.rmtree("build")
            shutil.rmtree("__pycache__")

    # Preapre Directory and Build Binaries
    print("[Building] Generating binaries")
    os.makedirs("dist")
    PyInstaller.__main__.run([
        'main.spec'
    ])

    # Copy Dependencies
    print("[Building] Copying dependencies")
    if platform.system() == "Windows":
        os.makedirs(f"dist/{PROGRAM_NAME}/bin/win/")
        for i in glob.glob("bin/win/*"):
            shutil.copy(i, f"dist/{PROGRAM_NAME}/bin/win/")
    elif platform.system() == "Linux":
        os.makedirs(f"dist/{PROGRAM_NAME}/bin/linux/")
        for i in glob.glob("bin/linux/*"):
            shutil.copy(i, f"dist/{PROGRAM_NAME}/bin/linux/")

    # Append an Installer
    print("[Building] Appending an installer")
    if platform.system() == "Linux":
        shutil.copy("misc/install.sh","dist")
        shutil.copy("misc/xl-converter.desktop","dist")
    elif platform.system() == "Windows":
        shutil.copy("misc/install.iss","dist")

    # Embed the Version Number
    print("[Building] Embedding the version number")
    if platform.system() == "Linux":
        replaceLine(os.path.join(PROGRAM_FOLDER, "dist/install.sh"), "VERSION=", f"VERSION=\"{VERSION}\"\n")
    elif platform.system() == "Windows":
        replaceLine(os.path.join(PROGRAM_FOLDER, "dist/install.iss"), "#define MyAppVersion", f"#define MyAppVersion \"{VERSION}\"\n")

    # Log Last Build Platform
    with open("build/last_built_on","w") as last_built_on:
        last_built_on.write(f"{platform.system()}_{platform.architecture()}")

    print(f"[Building] Finished (built to {os.path.join(PROGRAM_FOLDER,'dist','xl-converter')})")