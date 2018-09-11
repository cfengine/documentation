---
layout: default
title: Extend Mission portal help menu
published: true
sorting: 90
tags: [faq, mission portal, menu]
---

Mission portal has the possibility to extend the help menu. It can be useful if you would like to share extra content with your users.

##How to use

Upload your html file into `/path/to/cfengine/httpd/htdocs/application/views/extraDocs/` directory 
then your menu will be extended by this file. Name of menu item will be parsed from file name. Underscores will be replaced by whitespace. 
Please note, uploaded files should have read permission for `cfapache` user.

##Example

File `test_documentation.html` was uploaded to the directory specified above.
![Extended menu](extended-menu.png)

##Html structure

You can follow HTML structure below to make your page styled as Mission portal ones. 

```
<div class="contentWrapper help">
    <div class="pageTitle">
        <h1>PAGE TITLE</h1>
    </div>

     <!-- CONTENT --->
</div>
```

*It's not required, you can use own structure.