FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):    # here we are sying that this argument is a default one, so when calling the function, 
                                        # we don't have every time to write the argument
    with open(filepath,"r") as file_local:  # here we hardcoded our function
        todos_local =  file_local.readlines() # creating the list
    return todos_local           # returning the list

def write_todos(todos_arg, filepath=FILEPATH):   # the non-default parameters should be always before the default ones
    with open(filepath, "w") as file:
        file.writelines(todos_arg) 
        # we did not return anything here because this function is more like a procedure, it modifies components in the path file


print("I am outside!")
print(__name__)                  # it's a string, and the result is __main__
# and calling it from outside will give the result functions
# so here if the __name__ is called from the inside file, it will get __main__, then the if loop can run
# but calling it from the outside will give __name__ == functions (the name of our file), so we will not see the result 
# of runing our code from the our principal file (for me it's Day1)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())


# Example functions:


from zipfile import ZipFile
from pathlib import Path

def extract_archive(archivepath, dest_dir):
   with ZipFile(archivepath,'r') as archive:
       archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("005 compressed.zip", "files")

"""
if __name__ == "__main__":
    extract_archive("005 compressed.zip", "files")
This is a very common Python pattern, and it’s used to control what code gets executed when a Python file is run directly versus
 when it is imported as a module.

🔍 Explanation
🔹 __name__
__name__ is a special built-in variable in Python.

When you run a script directly, like:


python myscript.py
then Python sets __name__ to the string "__main__" inside that file.

But if you import that same file as a module:


import myscript
then __name__ will be "myscript" (i.e. the filename, not "__main__").

🔹 if __name__ == "__main__":
This checks:

❓ “Am I running this file directly, or is it being imported?”

If you are running the file directly (like a script), it executes the indented code under it.
If the file is just being imported, it skips that part.

✅ Why It’s Useful
It lets your file do both:

Act like a script (for testing or running functionality)

Be imported as a module (to reuse the function extract_archive() somewhere else)

🔁 In Your Case
You're saying:


if __name__ == "__main__":
    extract_archive("005 compressed.zip", "files")
🟰 "Only extract this zip file if I run this file directly."

But if someone else writes:


from my_zip_module import extract_archive
They can now call extract_archive(...) without triggering the extraction immediately.

📦 Summary
| Case                 | What Happens                                                           |
| -------------------- | ---------------------------------------------------------------------- |
| `python myscript.py` | ✅ Runs the `extract_archive(...)` call                                 |
| `import myscript`    | ❌ Skips the `extract_archive(...)` call (but function still available) |

"""