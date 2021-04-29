---
layout: default
title: Dashboard Alerts
sorting: 15
published: true
tags: [Examples, Tutorials, Dashboard, Alerts, Enterprise]
---

At 5 minutes intervals, the CFEngine hub gathers information from all of its connected agents about the current state of the system, including the outcome of its runs. All of this information is available to you. In this tutorial we will show how to use the Dashboard to create compliance overview at a glance

**Note:** This tutorial builds upon [another tutorial that manages local users][Manage local users].

We will create 3 alerts, one that shows when CFEngine repairs the system (promise repaired), one that shows when CFEngine does not need to make a change (promise kept), and one that shows CFEngine failing to repair the system (promise not kept).

<iframe width="560" height="315" src="https://www.youtube.com/embed/Wq-NC2Avxmg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Create a new alert

1. Log into Mission Portal, the web interface for CFEngine Enterprise.

2. In an empty space, Click Add.

![Add new alert widget](create_dashboard_alert2.png)

3. Name the alert 'Users compliance' and leave Severity-level at 'medium'.

4. Click create new condition and leave Name 'Users compliance'.

5. Select Type to 'Policy'.

6. Select Filter to 'Bundle', and type 'ensure_users'.

7. Type Promise handle to 'ensure_user_setup'.

8. Type Promise Status to 'Not kept'.

![New Alert widget](create_dashboard_alert2.png)

9. Press 'Save button' and give the Widget an descriptive name.

![New widget name](create_dashboard_alert3.png)

Done!

You have created a Dashboard Alert for our user management policy. Whenever the policy is out of compliance (not kept), we will be notified.

On the first screen below, we see that the alert has been triggered on zeor of our three hosts (0 / 3). This is exactly what we want. There is no promise not kept anywhere, which means we are in compliance.

![Details of alerts in widget](create_dashboard_alert4.png)

If you click on the Dashboard tab and go to the front page, you will see that our User Policy has a green check-mark. This means that the ‘not kept’ condition have not occured on any host.

![Alert cleared](create_dashboard_alert5.png)

2. Conclusions

In this tutorial, we have shown how easy it is to prove compliance of any of your policies by using the Dashboard alert functionality.

If you would like to get an overview of whenever CFEngine is making a change to your system, simply create another alert, but this time set the Promise Status to ‘Repaired’. This time you will see an alert whenever CFEngine is repairing a drift, for instance if a user is accidentially deleted.

