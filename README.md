Batch User Creation from File
Create a Python script that meets the following requirements
1. Script Name: /usr/local/bin/file_batch_user.py
2. The script must accept the command line option -f which specifies the path to a file that contains a list of usernames to be created
3. The list of usernames can be separated by a comma, a variable amount of whitespace (including newlines), or a semicolon.
4. The script must create a system user for each user listed in the input file, with a password of the username reversed.
5. A sample list is provided at /var/data/aga/users.txt

Example:


alice   Bill,charlie;danny

earl

frank;greg



With the above input file, the script would create a user alice with a password of ecila, a user Bill with the password lliB, etc.
