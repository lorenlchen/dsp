# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > `pwd` show current working directory path  
> > `mkdir` create a directory  
> > `rmdir` delete a directory  
> > `touch` create an empty file  
> > `rm` delete a file  
> > `mv`  rename (or move) a file  
> > `ls -a` list all files (including hidden)  
> > `cp` copy a file from one path to another (maybe in another directory)  
> > `cd` change working directory  
> > `pushd, popd` `pushd` temporarily change working directory and save current working directory. `popd` returns you to previous working directory.  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` list files in working directory  
> > `ls -a` list all files, including hidden  
> > `ls -l` list files in long format (with information on size, date modified, owner, privileges, etc.)  
> > `ls -lh` list files in long format with suffixes for size (K, M, etc.)  
> > `ls -lah` list all (including hidden) files in long format with size suffixes  
> > `ls -t` list files sorted by when they were last modified  
> > `ls -Glp` list files in long format, color-coded by filetype, and displaying directories with a `/` at the end.  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `-d` lists only the directories in the working directory  
> > `-r` reverses the sort order of the list  
> > `-m` displays as a list separated by commas  
> > `-1` displays each entry on a separate line  
> > `-g` uses long format, but omits the owner name   

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` can take what's given in STDOUT and convert it into arguments or groups of arguments (depending on the options) to be passed to commands. It is especially useful if you are trying to pass a very long list of arguments to a command that has an argument maximum, such as the result of a `find`, `ls`, or other command.   
>> A usage example is `find . -name "*~" -print0 | xargs -0 rm` which should remove all files ending in `~` in the working directory, for example, the temp files created by emacs.  
 

