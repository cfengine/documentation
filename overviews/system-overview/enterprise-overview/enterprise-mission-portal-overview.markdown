---
layout: default
title: Mission Portal Overview
sorting: 1
published: true
tags: [overviews, mission portal]
---

* [Infrastructure Engineering with the CFEngine Mission Portal](#infrastructure-engineering-with-the-cfengine-mission-portal)
* [Categorization of Hosts](#categorization-of-hosts)
* [Mission Portal Topics](#mission-portal-topics)
* [See Also](#see-also)

## Infrastructure Engineering with the CFEngine Mission Portal

When engineering IT infrastructure, and especially once the scale of a system grows to become quite large, it is much more of a challenge to recognize what the system consists of, what is happening at any given moment in time (or over time), and recognizing changes in state.

To meet this challenge, the CFEngine Mission Portal provides tools to collect, organize, store, and deliver data from every host to a primary server and then make that data available for high level reports or alerts and notifications.

Mission Portal's GUI environment also allows infrastructure engineers to make quick and easy modification of any machine or group of machines within their domain using classifications of hosts and a template mechanism called sketches.

### Categorization of Hosts ###

CFEngine allows for arbitrary categorization of hosts based on specified criteria. If you are writing your own policy, you are able to set classes on hosts which can be used in the Mission Portal. If you are not, you can still use pre-defined groups that CFEngine discovers automatically in your environment.

CFEngine's Mission Portal comes with a pre-defined host categorization based on operating systems used in your environment. The same categorization is used for the menu on the left of the [Hosts App][Viewing Hosts in Mission Portal], the data-filtering inside the [Reports App][Mission Portal Reports], and for the activation of sketches in the [Design Center App][Using Sketches in Mission Portal's Design Center App].

You can also define your own categories and sub-categories. As part of the menu inside the [Hosts App][Viewing Hosts in Mission Portal], you will find the option to add a new categorization. Here you can group your hosts in whichever way you need by combining different classes. You can then share your custom categorization within your team and organization (this needs special access rights).

### Mission Portal Topics ###

* [Alerts and Notifications in the Mission Portal Dashboard][Alerts and Notifications in the Mission Portal Dashboard]
* [Viewing Hosts in Mission Portal][Viewing Hosts in Mission Portal]
* [Using Sketches in Mission Portal's Design Center App][Using Sketches in Mission Portal's Design Center App]
* [Mission Portal Reports][Mission Portal Reports]
* [Host Monitoring in Mission Portal][Host Monitoring in Mission Portal]

### See Also ###
* [Sketches Available in the Mission Portal][Sketches Available in the Mission Portal]
* [Sketch Flow in CFEngine Enterprise][Sketch Flow in CFEngine Enterprise]
* [Integrating Mission Portal with git][Integrating Mission Portal with git]
* [Controlling Access to the Design Center UI][Controlling Access to the Design Center UI]



