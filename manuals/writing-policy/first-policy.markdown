---
layout: default
title: Write your first Policy
categories: [Manuals, Writing Policy, Write your first Policy]
published: true
sorting: 10
alias: manuals-writing-policy-first-policy.html
tags: [manuals, style, policy]
---
<!-- Add Before You Begin info: masterfiles and create dirs. ALSO mention that 
EZ TUTORIALS are in another spot-give the location -->

Create a file called a01SayHello.cf.

<!-- Add the location -- where to place this file? -->


**a01SayHello.cf**

```cf3

bundle agent a01_say_hello                                     # <1>
{

methods:                                                       # <2>
    "a01sayhello" usebundle
                        => a01_run ;                           # <3>

}

bundle agent a01_run
{

vars:                                                          # <4>
    "myfile" string     => "/tmp/helloFromCfengine.txt" ;

files:                                                         # <5>
    "$(myfile)"                                                # <6>
    edit_line           => a01_edit,                           # <7>
    edit_defaults       => empty,                              # <8>
    perms               => mog("644","root","root"),           # <9>
    create              => "true",                             # <10>
    classes             => if_repaired("make_some_noise") ;    # <11>

reports:                                                       # <12>
    make_some_noise::                                          # <13>
    "Heads up - the $(this.promise_filename) promise ran." ;   # <14>

}


bundle edit_line a01_edit                                      # <15>
{

vars:
    "hello" string           =>                                # <16>
"If you are reading this, your promise worked on $(sys.fqhost)
Nice going!"

insert_lines:                                                  # <17>
    "$(hello)" ;

}
```

**Point by Point:**

<1> The **a01_say_hello** bundle is called by **promises.cf**, by way of 
the **z01PromiseSetup.cf** file we created. Recall that we specified **a01_say_hello** 
within the **z01_promise_setup** bundle.

<2> CFEngine bundles can have a **methods** section. It is used to call other bundles.

<3> Here we call the **a01_run** bundle, which is defined a few lines below.

<4> CFEngine bundles can have a **vars** section. It defines variables of type **string** 
or **slist** (roughly, string type and array type, respectively).

<5> CFEngine bundles can have a **files** section for specifying files and describing how 
they must be changed.

<6> The expanded value of **$(myfile)** is **/tmp/helloFromCfengine.txt**. This is the file 
we will be editing.

<7> The `edit_line` attribute says to call bundle **a01_edit**.

<8> This attribute says to empty the file before editing it.

<9> The **perms** directive sets the file (m)ode to 644, the file (o)wner to root, and the 
file (g)roup owner to root.

<10> This attribute says to create the file if it does not already exist.

<11> This directive says to set a **class** called **make_some_noise** to the value 
true, _if_ CFEngine discovers that the file is not in the state it expected and therefore 
needs to edit it (either its content or its permissions). We will get to more examples 
of **classes** later, and they are further enumerated by URL references at the end of this primer.

<12> Remember when we set up a mailto address in the **controls/cf_execd.cf** server 
configuration? The **reports** section utilizes that address to send an email on anything 
we report about here. (It also logs a message, via syslog.)

<13> We are checking the **make_some_noise** class. If it's set to **true**, we 
generate the report (which gets emailed and logged). If it's set to **false**, we don't.

<14> This value is the message we report. The **$(this.promise_filename)** is a special 
CFEngine variable. The **$(this)** variables are enumerated by a URL at the end of this primer.

<15> Another bundle, this time of type **edit_line a01_edit**.

<16> We define a variable, and assign it some text, including a special CFEngine variable 
called **$(sys.fqhost)**, which contains the system's fully-qualified hostname. The **$(sys)** 
variables are enumerated by a URL at the end of this primer.

<17> The **edit&#95;line** bundles can have an **insert&#95;lines** section. As you can 
probably guess, they insert into the file the text we specify.

[Back to top of page.][Up and Running#Overview] 

