---
layout: default
title: Quick-Start Guide to Using vi
published: true
sorting: 1
tags: [how-to-guides, quick-start guides, vi]
---


This guide is designed for the novice user of CFEngine tutorials—and will introduce the basic
use of a powerful tool that is referenced in the CFEngine learning documentation: the vi visual editor.

What is a visual editor? It lets you see multiple lines of the document you are editing—rather than
simply issuing commands in the shell prompt. This means you can insert a very large piece of text
and navigate anywhere in that text, and make changes.

The vi editor was developed for unix—but can run from any shell prompt, like PuTTY on the Windows platform,
and also the Mac. So whatever the user's platform may be, learning to use vi will be very useful in working
through the CFEngine tutorials.

When working in the CFEngine tutorials, vi will be used to do things like open files, insert text,
save files, and many other functions.

vi will also be used when the CFEngine user starts to actually use the CFEngine software—for things
like writing and deploying promises, the core of the CFEngine technology.

Learning the basics of vi is quite simple. The best way is by walking through an example.

Step 1. Inside the shell prompt, simply type “vi”. This will allow the user to insert text and create a new file.

Step 2. type “i” then press the “Enter” key. This takes the user to the insert mode, and allow typing in text or copying and pasting.

Step 3. Type some text—for example, the  obligatory “Hello World” (which will be the subject of a later tutorial).
Now press "Enter" to go to the next line and type “My name is Gary, and it's nice to meet you.”

The output will look like this:

```
Hello World
My name is Gary, and it's nice to meet you
```

Step 4. Now exit the insert mode and go back to command mode by pressing the “esc” key.

Step 5. Save the file by typing “:w (filename)”

Step 6. exit vi by typing “:q”

You can also save and exit with one command, “:wq”

It is important to remember that there are two basic operation modes in vi: the _command mode_, with which the user opens, saves and
exits from files, and the _insert_ mode with which the user inserts text—either by typing it in, or by copying and pasting—and can
then edit any part of the text in the file.

open file using `vi filename`


