---
layout: default
title: User Interface
sorting: 20
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

When engineering IT infrastructure, and especially once the scale of a system grows to become quite large, it is much more of a challenge to recognize what the system consists of, what is happening at any given moment in time (or over time), and recognizing changes in state.

To meet this challenge, the CFEngine Enterprise's User Interface (also known as Mission Portal) provides tools to collect, organize, store, and deliver data from every host to a primary server and then make that data available for high level reports or alerts and notifications.

CFEngine Enterprise's User Interface also allows infrastructure engineers to make quick and easy modification of any machine or group of machines within their domain using classifications of hosts and a template mechanism called sketches.

* [Hosts, Health and Settings][CFEngine Enterprise User Interface#Hosts, Health and Settings]
* [Alerts and Notifications][CFEngine Enterprise User Interface#Alerts and Notifications]
* [Reporting][CFEngine Enterprise User Interface#Reporting]
* [Monitoring][CFEngine Enterprise User Interface#Monitoring]
* [Design Center][CFEngine Enterprise User Interface#Design Center]

## Hosts, Health and Settings ##

Find out more: [Hosts, Health and Settings][]

## Alerts and Notifications ##

The dashboard contains informative widgets that you can customize to create alerts that are important to you. All alert state changes, e.g. from OK to triggered, are logged to the Event log.

![Enterprise UI Alerts](welcome_2nd_screen.png)


Alerts can have three different severities: low, medium and high. These are represented by rings in yellow, orange and red respectively, along with the percentage of hosts alerts have triggered on. Hovering over the widget will show all information in a convenient list.

![Enterprise UI Alerts](widget_1.gif)


You are able to pause alerts during maintenance windows or while working on resolving an underlying issue to avoid unnecessary triggering and notifications.

![Enterprise UI Alerts](pause_alerts.gif)

Alerts can have three different states: OK, triggered, and paused. It is easy to filter by state on each widget's alert overview.

Find out more: [Alerts and Notifications][]

## Reporting ##

Inventory reports allow for quick reporting on out-of-the-box attributes. The attributes are also extensible, by tagging any CFEngine variable or class, such as the role of the host, inside your CFEngine policy. These custom attributes will be automatically added to the Mission Portal.

![Enterprise UI Reporting](inventory-hover.png)

You can reduce the amount of data or find specific information by filtering on attributes and host groups. Filtering is independent from the data presented in the results table: you can filter on attributes without them being presented in the table of results.

![Enterprise UI Reporting](inventory_filter.gif)

Add and remove columns from the results table in real time, and once you're happy with your report, save it, export it, or schedule it to be sent by email regularly.

![Enterprise API Overview](add_columns.gif)

Find out more: [Reporting][]

## Monitoring ##		

Find out more: [Monitoring][]

## Design Center ##

Find out more: [Design Center][]










