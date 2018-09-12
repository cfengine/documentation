---
layout: default
title: Mission Portal authenticated access to extra content
published: true
sorting: 90
tags: [FAQ, Mission Portal, enterprise]
---

Mission portal has tool to render static text files (html, sql, txt, etc) for users which are logged in.

##How to use

Upload your files into `/path/to/cfengine/httpd/htdocs/application/modules/files/static_files` directory 
then you will have access to them by URL https://hub/files/view/file_name.html, when file_name.html is name of uploaded file.
Please note, uploaded files should have read permission for `cfapache` user.
