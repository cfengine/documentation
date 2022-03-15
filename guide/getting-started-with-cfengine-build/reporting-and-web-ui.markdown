---
layout: default
title: Reporting and Web UI
published: true
sorting: 30
tags: [guide, getting started, mission portal]
---

After setting up your CFEngine Hub, adding modules and deployed your first policy set, it's appropriate to get familiar with the CFEngine Web UI, Mission Portal, and some of it's useful features.
This is by no means an exhaustive list of everything Mission Portal offers, but a good introduction for new users.
If you haven't already, open your web browser and put the IP address (or hostname) of your CFEngine Hub in the address bar.
For example:

https://192.168.56.2/

(Log in with the username and password for your hub, the default is `admin` as both and you will be prompted to change it on the first login).

## The host info page

You can find individual hosts by using the search bar in the top right corner of Mission Portal, or by clicking _Hosts_ in the left navigation bar and looking through the different categories in the tree.
Both ways will lead you to an individual _Host info page_:

![](host-info.png)

In this page you find a lot of useful functionality and information related to an individual host.
There are a few action buttons in the top right corner:

![](action-buttons.png)

These allow you to trigger an agent run, report collection, get a sharable link, or delete the host from Mission Portal and the hub.
Further down there is a section for _Inventory_ (reporting data) which you can customize to show the pieces of information you care about:

![](inventory-section.png)

In the _Host specific data_ section you can assign CFEngine variables and classes to that host, changing the behavior of the policy running there.
If you haven't started writing any policy yet, the _Suggestions_ menu can be used to make some changes to what the default policy is doing, such as making the agent run every minute instead of the 5-minute default:

![](host-specific-data-with-suggestion.png)

**Tip:** Host specific data can be used to make temporary or permanent changes to the data (configuration) of specific hosts.
Using the suggestion from the screenshot above has the same effect as the `every-minute` module we added earlier in the tutorial series.
The advantage of not using that module and instead using host specific data is that we can quickly enable and disable this functionality on a per-host basis, and without rebuilding and deploying a new policy set to all our hosts.

## Inventory reports

Inventory reports allow you to easily get an overview of all your hosts, and what is on them.
Each host in your infrastructure gets a row in the inventory report.
The columns can be customized so the report shows the data you care about:

![](inventory-reports.gif)

Use the _Filter_ menu if you want to only show some of your hosts in the report.

## Compliance reports

Compliance reports allow you to specify your requirements for your infrastructure as checks, and easily see which hosts are compliant and which ones are not.
The checks are grouped into categories and you can specify that some checks only apply to some hosts.
In Mission Portal, there is already an example compliance report which gives you a good idea of the things you can do with them:

![](compliance-report.png)

(To find this, click _Reports_ in the left navigation bar, then _Compliance_).

## Policy analyzer

As you start writing policy or using more modules, you might encounter situations where your deployed policy is not working and causes errors on some hosts.
The best way to investigate these errors is to use the _Policy Analyzer_.
In the left navigation bar, you can click _Policy Analyzer_, and then the blue button to _Enable policy analyzer_.
Once enabled (refresh or wait a bit) the policy analyzer gives you a way to browse through your policy set:

![](policy-analyzer.png)

The _Policy Analyzer_ tab will have a red counter if there are errors happening in your policy.
In CFEngine, we call these _Promises not kept_, meaning the policy failed to do what it was supposed to, it failed to reach the desired state.

You can change the filters to see the outcomes of everything your policy does.
Drill down to individual policy files and lines of policy and see which hosts it's failing on and what the relevant log messages are.

## Next steps

At this point you have a good overview of what CFEngine does, and you can choose to look around in Mission Portal, create your first Compliance Report, or find more modules on [CFEngine Build](https://build.cfengine.com/).
Once you feel comfortable with the CFEngine Hub, modules, and reports, you are ready to move on, and learn CFEngine's expressive policy language and powerful module system.
You're not limited by what modules others have made, you can write the code you need to get things done:

[Writing policy][Writing policy]
