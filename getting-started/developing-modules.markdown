---
layout: default
title: Developing modules
published: true
sorting: 50
tags: [guide, getting started]
---

Modules, such as the one we've used for git promises, are easy to write.
In this tutorial, we will focus on implementing a new promise type in Python, with the provided CFEngine library, since this is the easiest and recommended way.
If you are interested in how modules are implemented, or how you could do it in another programming language, see the [complete documentation](/reference-promise-types-custom.html).

In short, you need to implement 2 functions: `validate_promise()` and `evaluate_promise()`.
_Validation_ should check that the correct attributes are used, and any other constraints you may want to enforce, to determine whether a promise is valid or invalid.
_Evaluation_ happens after successful _Validation_, and actually performs actions / makes changes to the system.
When implementing a promise type for CFEngine, there are 3 outcomes you need to understand:

* `Result.KEPT` - The module detected that no changes are necessary, the actual state of the system is already consistent with the desired state
* `Result.REPAIRED` - The module detected that changes have to be made, and successfully completed all of them
* `Result.NOT_KEPT` - The module failed to make the necessary changes

## The template

To get started, let's take a look at this template repository:

https://github.com/cfengine/promise-type-template

We can add it to our project with the full URL:

```
$ cfbs add https://github.com/cfengine/promise-type-template
```

From that repo, we have now added a new promise type, it is called `git_example` to avoid confusion with the "real" git promise type used earlier in the tutorial.
Then, we should edit our policy example, `my_policy.cf` to use this module:

```cfengine3
bundle agent hello_world
{
  meta:
    "tags"
      slist => { "autorun" };

  git_example:
    "/tmp/hugo"
      repository => "https://github.com/gohugoio/hugo.git";
}
```

That's it, you can now build and deploy:

```
$ cfbs build && cf-remote deploy
```

And to test it, we can delete the folder and run the agent again:

```
$ cf-remote sudo -H hub "rm -rf /tmp/hugo && cf-agent -KI | grep hugo"
root@137.184.114.168: 'rm -rf /tmp/hugo && cf-agent -KI | grep hugo' -> '    info: Cloning 'https://github.com/gohugoio/hugo.git' -> '/tmp/hugo'...'
root@137.184.114.168:                                                   '    info: Successfully cloned 'https://github.com/gohugoio/hugo.git' -> '/tmp/hugo''
```

## Creating your own repository

To start working on your own module, you can click _Use this template_ in GitHub, to create your own copy (fork):

https://github.com/cfengine/promise-type-template

Take a look at these important files:

* `git_example.py` - The module code itself. This is where you will work the most, changing what the promise type does, implementing functionality, fixing bugs, etc.
* `cfbs.json` - Metadata about the module(s). Most importantly, the `provides` key has the information needed for `cfbs add`, and subsequently `cfbs build` to work.
* `enable.cf` - The snippet of policy that needs to be included to enable your promise type.

Start by editing `cfbs.json`, at least changing the `repo` and `by` URLs.

**Tip:** Remember to update `cfbs.json` and `enable.cf` if you change the filename of the python file, or the name of the promise type.

To test your changes, make sure they are pushed to GitHub, and re-add your module, for example:

```
$ cfbs remove promise-type-git-example && cfbs add https://github.com/cfengine/promise-type-template
```

**Tip:** Replace the URL with your own repository URL when you've create one using the template.

Then, build and deploy the project again:

```
$ cfbs build && cf-remote deploy
```

And just like before, you can run manual agent runs to test:

```
$ cf-remote sudo -H hub "rm -rf /tmp/hugo && cf-agent -KI"
```

## Changing / updating the python file

As you've changed the high level things, like file name, promise type name, URLs, etc. and deployed that, the only thing you need to edit is the contents of the python file.
So, to test your changes to the python file, a full build is not really necessary, you can just copy over that one file:

```
$ cf-remote scp -H hub git_example.py /var/cfengine/masterfiles/modules/promises/git_example.py
```

(Assuming you have the `git_example.py` file in the current directory).

And then you can test it:

```
$ cf-remote sudo -H hub "cf-agent -KIf update.cf && cf-agent -KI"
```

**Note:** Every 5 minutes (by default) CFEngine will copy files from `/var/cfengine/masterfiles` (on the hub) to other locations, such as `/var/cfengine/inputs` and `/var/cfengine/modules`.
This is the responsibility of the update policy, `update.cf`.
By editing the file inside `/var/cfengine/masterfiles`, and then running `cf-agent -KIf update.cf` we can be sure that our modules and policy files are correct and in sync, our changes will not be reverted the next time CFEngine runs in the background.

## Submitting your module to CFEngine Build

Once you have your module working and would like to share it with others, take a look at our contribution guide:

https://github.com/cfengine/build-index/blob/master/CONTRIBUTING.md

## Additional resources

There are several places to look for more information or inspiration when writing modules:

* [The real git promise type code](https://github.com/cfengine/modules/tree/c3b7329b240cf7ad062a0a64ee8b607af2cb912a/promise-types/git/)
* [HTTP promise type module](https://github.com/cfengine/modules/tree/c861789d4b376147d904fccd76963a92e65eaa97/promise-types/http/)
* [CFEngine custom promise type specification](/reference-promise-types-custom.html)
* [Blog post: How to implement CFEngine Custom Promise Types in Python](https://cfengine.com/blog/2020/how-to-implement-cfengine-custom-promise-types-in-python/)
* [Blog post: How to implement CFEngine Custom Promise Types in Bash](https://cfengine.com/blog/2021/how-to-implement-cfengine-custom-promise-types-in-bash/)
