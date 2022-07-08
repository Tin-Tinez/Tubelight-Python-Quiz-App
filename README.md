# Tubelight-Python-Quiz-App
How to Run Python Code Interactively
A widely used way to run Python code is through an interactive session. To start a Python interactive session, just open a command-line or terminal and then type in python, or python3 depending on your Python installation, and then hit Enter.

Here’s an example of how to do this on Linux:

$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
The standard prompt for the interactive mode is >>>, so as soon as you see these characters, you’ll know you are in.

Now, you can write and run Python code as you wish, with the only drawback being that when you close the session, your code will be gone.

When you work interactively, every expression and statement you type in is evaluated and executed immediately:

>>> print('Hello World!')
Hello World!
>>> 2 + 5
7
>>> print('Welcome to Real Python!')
Welcome to Real Python!
An interactive session will allow you to test every piece of code you write, which makes it an awesome development tool and an excellent place to experiment with the language and test Python code on the fly.

To exit interactive mode, you can use one of the following options:

quit() or exit(), which are built-in functions
The Ctrl+Z and Enter key combination on Windows, or just Ctrl+D on Unix-like systems
Note: The first rule of thumb to remember when using Python is that if you’re in doubt about what a piece of Python code does, then launch an interactive session and try it out to see what happens.

If you’ve never worked with the command-line or terminal, then you can try this:

On Windows, the command-line is usually known as command prompt or MS-DOS console, and it is a program called cmd.exe. The path to this program can vary significantly from one system version to another.

A quick way to get access to it is by pressing the Win+R key combination, which will take you to the Run dialog. Once you’re there, type in cmd and press Enter.

On GNU/Linux (and other Unixes), there are several applications that give you access to the system command-line. Some of the most popular are xterm, Gnome Terminal, and Konsole. These are tools that run a shell or terminal like Bash, ksh, csh, and so on.

In this case, the path to these applications is much more varied and depends on the distribution and even on the desktop environment you use. So, you’ll need to read your system documentation.

On Mac OS X, you can access the system terminal from Applications → Utilities → Terminal.
