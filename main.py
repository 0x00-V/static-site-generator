import shutil, os


def copytodst(static, public):
    shutil.rmtree(public)
    os.mkdir(public)
    shutil.copy(static, public)
"""
The shutil.copy() function will only copy a single file—not an entire directory. 
To copy all the files and subdirectories within static, you'll need to traverse 
through its contents, identifying whether each item is a file or subdirectory. 
This is where recursion becomes important.
"""
"""
How will you distinguish between files and subdirectories in static? 
What function might help you differentiate and handle those cases? 
"""