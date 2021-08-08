import os
import platform


if __name__ == '__main__':
    print('\nExecuting Virtual Environment Setup\n')

    if platform.system() == 'Linux':
        print('\nLinux Virtual Environment Setup\n')
        os.system("python3.6 -m venv .venv")
        os.system(".venv/bin/python3 -m pip install -r requirements.txt")

    if platform.system() == 'Windows':
        print('\nWindows Virtual Environment Setup\n')
        os.system("python3.6 -m venv .venv")
        os.system(".\\.venv\\Scripts\\python -m pip install -r requirements.txt")
