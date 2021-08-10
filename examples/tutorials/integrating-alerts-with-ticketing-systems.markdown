---
layout: default
title: Integrating alerts with ticketing systems
sorting: 15
published: true
tags: [Examples, Tutorials, Alerts, Enterprise, Custom Actions]
---

Custom actions can be used to integrate with external 3rd party systems. This tutorial shows how to use a custom action script to open a ticket in Jira when a condition is observed.

<iframe width="560" height="315" src="https://www.youtube.com/embed/X5zXn1LdqP0" frameborder="0" allowfullscreen></iframe>

## How it works

We assume that there is already a CFEngine policy bundle in place called `web_service` that ensures an important service is working.

As we are already using the JIRA ticketing system to get notified about issues with the infrastructure, we want CFEngine to open a ticket if our `web_service` bundle fails (is not kept). This is done centrally on our hub, because it knows the outcome of the policy on all the nodes. We will only open a ticket once the alert changes state to triggered, not while it remains in triggered, to avoid an unnecessary amount of tickets being automatically created.

Note however that it is possible to expand on this by adjusting the Custom action script. For example, we could create reminder tickets, or even automatically close tickets when the alert clears.

## Create a Custom action script that creates a new ticket

1.  Log in to the console of your CFEngine hub, and make sure you have python and the jira python package installed (normally by running `pip install jira`).

2.  On your workstation, unpack [cfengine\_custom\_action\_jira.py](integrating-alerts-with-ticketing-systems_cfengine_custom_action_jira.py.zip) to a working directory.

3.  Inside the script, fill in `MYJIRASERVER`, `MYUSERNAME` and `MYPASSWORD` with your information.

4.  Test the script by unpacking [alert\_parameters\_test](integrating-alerts-with-ticketing-systems_alert_parameters_test.zip) into the same directory and running `./cfengine_custom_action_jira.py alert_parameters`.

5.  Verify the previous step created a ticket in JIRA. If not, recheck the information to typed in, connectivity and any output generated when running the script.

## Upload the Custom action script to the Mission Portal

1. Log in to the Mission Portal of CFEngine, go to Settings (top right) followed by Custom notification scripts.

2. Click on the button to Add a script, upload the script and fill in the information as shown in the screenshot.

    ![Upload custom action script](integrating-alerts-with-ticketing-systems_custom-action-script-upload-jira.png)

3.  Click save to allow the script to be used when creating alerts.

## Create a new alert and associate the Custom action script

1. Log into the Mission Portal of CFEngine, click the Dashboard tab.

2. Click on the existing Policy compliance widget, followed by Add alert.
   
    ![Add alert to Policy Compliance widget](integrating-alerts-with-ticketing-systems_policy-compliance-add-alert.png)

3. Name the alert "`Web service`" and set `Severity-level` at "`high`".

4. Click create new condition and leave Name "`Web service`".

5. Select Type to "`Policy`".

6. Select Filter to "`Bundle`", and type "`web_service`".

7. Type Promise Status to "`Not kept`".

    ![Set Type Promise Status to Not kept](integrating-alerts-with-ticketing-systems_web-service-condition.png)

8. Associate the Custom action script we uploaded with the alert.

    ![Associate custom action script with alert](integrating-alerts-with-ticketing-systems_custom-action-alert-association-jira.png)

## Conclusions

In this tutorial, we have shown how easy it is to integrate with a ticketing system, with JIRA as an example, using CFEngine Custom actions scripts.

Using this Custom action, you can choose to open JIRA tickets when some or all of your alerts are triggered. But this is just the beginning; using Custom actions, you can integrate with virtually *any* external system for notifying about- or handling triggered alerts.

Read more in the [Custom action documentation][Custom actions for Alerts].

