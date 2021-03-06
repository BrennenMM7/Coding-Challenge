# Coding Challenge

## Installation and Running Application

### Prerequisites
This project will require python version 3.X to be installed, no other third party packages are required for this project. Ensure your Python version is updated by running: 

```bash
$ python --version 
Python 3.10.4
```

### Clone Project and Setup Terminal

```bash 
#Cloning Repository
git clone https://github.com/BrennenMM7/Coding-Challenge.git

#Ensure Terminal is in cloned directory
cd .\Coding-Challenge\
```

### Running the Application

```bash
#Run application with single file argument
python .\src\CodeChallenge.py -f .\sampleData\moby.txt

#Run application with multiple file arguments
python .\src\CodeChallenge.py -f .\sampleData\moby.txt .\sampleData\testingSample.txt

OR

#Execute app with raw text input from stdin
"testing sample data for text input" | python .\src\CodeChallenge.py

#Execute app with  text file input from stdin
cat "sampleData\moby.txt" | python .\src\CodeChallenge.py
```

Output:
```
cat "sampleData\moby.txt" | python .\src\CodeChallenge.py
----------------Results for "Terminal Input"-------------------
the sperm whale  -  84
the white whale  -  71
of the whale  -  70
one of the  -  64
of the sea  -  56
out of the  -  55
part of the  -  53
a sort of  -  51
of the sperm  -  42
it was a  -  33
for a moment  -  29
in the sea  -  29
it is a  -  28
of the boat  -  28
of the ship  -  27
to the deck  -  27
the sperm whale's  -  27
the sea and  -  26
at the same  -  25
for the time  -  25
by no means  -  25
the right whale  -  25
to be the  -  24
the same time  -  24
so as to  -  24
the bottom of  -  24
in the air  -  23
in order to  -  23
that in the  -  23
must have been  -  23
out of sight  -  22
there is no  -  22
it was that  -  22
at the time  -  22
into the sea  -  22
of the pequod  -  22
there was a  -  21
now and then  -  21
in the fishery  -  21
and in the  -  20
as it were  -  20
the whale and  -  19
up to the  -  19
and all the  -  19
it was the  -  19
it was not  -  19
and at the  -  19
so that the  -  19
i do not  -  18
down into the  -  18
as if it  -  18
of the whale's  -  18
one of those  -  18
on the sea  -  18
as well as  -  18
bottom of the  -  18
into the air  -  18
down to the  -  17
and with a  -  17
it is that  -  17
it is not  -  17
the ship and  -  17
down in the  -  17
the pequod was  -  17
end of the  -  17
over the side  -  17
the old man  -  17
round and round  -  17
of the white  -  17
in his own  -  16
to and fro  -  16
the old man's  -  16
whale and the  -  16
you would have  -  16
of the world  -  15
it is the  -  15
and as for  -  15
the act of  -  15
of the great  -  15
he was a  -  15
to be sure  -  15
but it was  -  15
the head of  -  15
side of the  -  15
he seemed to  -  15
all the time  -  15
more and more  -  15
him in the  -  15
on the other  -  15
of his head  -  15
some of the  -  15
of the leviathan  -  15
that it was  -  14
it was only  -  14
one of them  -  14
he had been  -  14
in the first  -  14
he did not  -  14
the sea the  -  14
the top of  -  14
-------------------------------------
```

## Running Tests
The Python testing module exsists within the same directory as the main module. The testing module is dependent on the "sampleData\testingSample.txt" file to check definition functions. 

```bash
#Run testing python module. 
python .\src\test_CodeChallenge.py
```

## What would you do next, given more time 
- In its current state the application is processing a single file everytime even if multiple arguments are provided on input. Importing a multithreading module and incorporating using a differrent thread for each file input would greatly increase speed.

- Add a different argument to accept file directory paths as a whole instead of manually adding each file argument.  

- Add dyanmicly generated sample text for the testing modules to ensure each function operating for variablity of data. 

## Known Bugs/Issues
- No real known bugs currently found. Only if a word line ends in the middle of the letters on reading the file will it split into two seperate words.
    Example: This is an exa\nmple.  