---
layout: default
title: Extending Mission Portal
published: true
sorting: 90
tags: [faq, mission portal, hub administration]
---

## Custom pages requiring authenticated users

Mission Portal can render static text files (html, sql, txt, etc ...) for users
which are logged in.

### How to use

Upload files to
`$(sys.workdir)/httpd/htdocs/application/modules/files/static_files` on your
hub. Access the content using the url https://hub/files/view/file_name.html,
where `file_name.html` is the name of a file. Please note, uploaded files should
have read permission for `cfapache` user.

## Custom help menu entries

The help menu Mission portal help menu. It can be useful if you would like to
make extra content like documentation easily avilable to users.

### How to use

Upload html files into
`$(sys.workdir)/httpd/htdocs/application/views/extraDocs/` on your hub. Menu
items will appear named for each html file where underscores are replaced with
spaces. Files must be readable by the `cfapache` user.


### Example

File `test_documentation.html` was uploaded to the directory specified above.
![Extended menu](extended-menu.png)

### Mission Portal Style

Use the following structure in your HTML to style the page the same as the rest
of Mission Portal.

```html
<div class="contentWrapper help">
    <div class="pageTitle">
        <h1>PAGE TITLE</h1>
    </div>

     <!-- CONTENT --->
</div>
```

