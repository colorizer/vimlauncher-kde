import os
import tempfile
import subprocess

def copy(string):
    return subprocess.run(
        ['xclip', '-selection', 'c'],
        universal_newlines=True,
        input=string
    )
def get():
    result = subprocess.run(
        ['xdotool', 'getactivewindow', 'key', 'ctrl+v'],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    # returncode = result.returncode
    stdout = result.stdout.strip()
    return stdout
def open_editor(filename):
    subprocess.run([
        "konsole", '-e', "vim", "+star",
        f"{filename}",
    ])

def open_vim():
    f = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.tex')
    f.close()
    open_editor(f.name)
    
    latex = ""
    with open(f.name, 'r') as g:
        latex = g.read().strip()
    os.remove(f.name)
    copy(latex)
    
open_vim()
get()
