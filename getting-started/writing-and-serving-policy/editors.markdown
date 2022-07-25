---
layout: default
title: Editors
published: true
sorting: 10
tags: [tools, editor, vim, emacs, vscode, kate, sublime text, atom, eclipse ]
---

Using an editor that provides syntax highlighting and other features can significantly enhance prodcutivity and quality of life.

## Emacs

For Emacs users, editing CFEngine policies is easy with the built-in CFEngine 3 mode in the [cfengine.el library](https://github.com/cfengine/core/blob/master/contrib/cfengine.el). For an overview of the capabilities, see the [webinar by Ted Zlatanov](https://www.youtube.com/watch?v=-PPVhwSKNdE) and Appendix A of Diego Zamboni’s [Learning CFEngine](https://leanpub.com/learning-cfengine/) book.
	
![Emacs](guide-writing-and-serving-policy-editors-emacs.png)

## Spacemacs

Spacemacs has a [CFEngine layer](https://github.com/syl20bnr/spacemacs/blob/develop/layers/%2Btools/cfengine/README.org) that configures many of the features shown in the Emacs webinar above out of the box as well as integration for executing `cfengine3` `src` blocks in `org-mode`. It’s a great way for `vi/vim` lovers to leverage the power of Emacs.

![Spacemacs](guide-writing-and-serving-policy-editors-spacemacs.png)

## Vi/Vim

Vi/Vim users can edit CFEngine policies with Neil Watson’s CFEngine 3 scripts, available as GPL-software [on GitHub](https://github.com/neilhwatson/vim_cf3). Neil’s vi mode is also described in Appendix B of Diego Zamboni’s “Learning CFEngine” book.
	
![Vim](guide-writing-and-serving-policy-editors-vim.png)

## Visual Studio Code

Microsoft VS Code users have syntax highlighting thanks to AZaugg. Install the syntax highlighting and snippets directly from within Visual Studio Code by running ext install vscode-cfengine.

![Visual Studio Code](guide-writing-and-serving-policy-editors-visual-studio-code.png)

## Sublime Text

Sublime Text 2 and 3 users have syntax highlighting and snippets thanks to Valery Astraverkhau. Get the syntax highlighting and snippets from his github repository. Aki Vanhatalo has contributed a beautifier to automatically re-indent policy in Sublime Text.
	 Sublime Screenshot

![Sublime Text](guide-writing-and-serving-policy-editors-sublime-text.jpg)

## Atom

Using Githubs hackable editor? You can get syntax highlighting with the language-cfengine3 package.

![Atom](guide-writing-and-serving-policy-editors-atom.png)

## Eclipse

Interested in syntax highlighting for your CFEngine policy in Eclipse? Try this  contributed syntax definition.

Want more out of your Eclipse & CFEngine experience? Itemis Xtext expert Boris Holzer developed a CFEngine workbench for Eclipse. They even published a brief screen-cast highlighting many of its features. For more information about their workbench please contact them using this form.
	
![Eclipse](guide-writing-and-serving-policy-editors-eclipse-0.png)
![Eclipse](guide-writing-and-serving-policy-editors-eclipse-1.png)
![Eclipse](guide-writing-and-serving-policy-editors-eclipse-2.png)
![Eclipse](guide-writing-and-serving-policy-editors-eclipse-3.png)

## Kate

Users of the editor of the KDE desktop, Kate, have syntax highlighting available thanks to Jessica Greer, John Coleman, and Panos Christeas. The syntax highlighting definition can be found with the CFEngine source in contrib.
	
![Kate](guide-writing-and-serving-policy-editors-kate.jpg)
