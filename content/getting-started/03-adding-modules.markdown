---
layout: default
title: Adding modules
sorting: 30
aliases:
  - "/getting-started-modules-from-cfengine-build.html"
  - "/getting-started/modules-from-cfengine-build"
  - "/getting-started/adding-modules"
---

Now that you've installed CFEngine, and used the Web UI a bit, let's take a look at extending it with modules.
CFEngine Build enables users to find useful modules on the website, [build.cfengine.com](https://build.cfengine.com), and easily add them to their policy.

The workflow will look like this:

{{< wideimg "workflow.png" "Infographic showing 4 steps of the CFEngine Build workflow, adding modules, building, deploying, observing." >}}

You can work on CFEngine Build projects both from inside Mission Portal, and using our command line tools.
In this tutorial, we will do it from inside Mission Portal.

## Step 0: Creating a new project

When you are logged in to Mission Portal, click the **Build** application in the left menu.

{{< wideimg "click-build.png" "Screenshot of Mission Portal showing the Build application you should click highlighted." >}}

If you do not have any pre-existing Build projects, you will be automatically prompted to create a new one:

{{< wideimg "add-new-project.png" "Screenshot of the form to add a new project with git repository information and the set up later button highlighted." >}}

On this screen, you can enter details to make your project be synced with a git repository (for example on github.com).
At this point, since we are just testing things, feel free to just click **Set up later**.

You will be prompted to select a version of the masterfiles policy framework (the CFEngine policy files that come with CFEngine).
In general, the default is the best option, it will choose a version matching the version of CFEngine you are running.
Click **Confirm**.

{{< img "masterfiles-selection.png" "Small popup which allows you to choose between masterfiles version 3.27.1 (default) and master" >}}

## Step 1: Explore and add modules

You will see a welcome screen which gives you an introduction to CFEngine Build:

{{< wideimg "cfengine-build-welcome.png" "Screenshot of Mission Portal Build welcome screen with instructions of how to get started and search field for finding modules." >}}

The search bar here searches for modules from [build.cfengine.com](https://build.cfengine.com).
Let's add some modules;

Search for `compliance-report-lynis` and click on the search result;

{{< wideimg "search-compliance-report-lynis.png" "Search results for compliance-report-lynis, there is one result that module." >}}

Click **Add module** to add it to your project:

{{< wideimg "add-compliance-report-lynis.png" "Module description screen after clicking the module, with the add module button highlighted." >}}

Feel free to add more modules, for example search for `inventory` and add `inventory-etc-hosts`, or any other module which seems useful.
Generally, `inventory-` modules add useful information to the reporting inventory and don't require any configuration or input to work.

On the left side of the application we can see the modules we've added:

{{< wideimg "added-modules.png" "Screenshot of Build in Mission Portal, with the added modules section highlighted showing the modules we've added." >}}

## Step 2 & 3: Build & deploy

In order to get these modules actually running, a few things need to happen:

1. **Building:** Downloading all the modules and combining them into one policy set.
2. **Deploying:** Transferring that policy set to the right folder on the hub.
3. **Updating / enforcing:** This happens automatically - once the policy is there, all the hosts will start fetching and running it.

In Mission Portal, we achieve this by simply clicking the **Deploy locally** button in the top right corner:

{{< wideimg "deploy-locally.png" "Screenshot of Build in Mission Portal UI with the Deploy locally button highlighted." >}}

## Step 4: Observe

Now, our modules are running on the hub and any other hosts in the infrastructure, and new reporting data will start arriving.
Let's open the **Reports** application:

{{< wideimg "navigate-reports.png" "Screenshot of Mission Portal with the left navigation button for reports highlighted." >}}

Go to the **CFEngine Build** tab to find reports added by CFEngine Build modules:

{{< wideimg "reports-cfengine-build-tab.png" "Screenshot of the Reports application with the CFEngine Build tab highlighted." >}}

And click on the new Lynis report:

{{< wideimg "reports-click-lynis.png" "Screenshot of the report application after clicking the CFEngine Build tab. There is only one report shown and highlighted, the lynis report." >}}

You will now see the new report and its results:

{{< wideimg "lynis-compliance-report.png" "Overview of the results from the Lynis compliance report, showing percentages in different categories and individual lynis security hardening check results." >}}

In this case, you can scroll through the report, look at the failing checks and find potential security hardening improvements highlighted by Lynis.
The other module we added, `inventory-etc-hosts`, does not add a _report_, but instead adds _reporting data_ / inventory.
To find this, go back to the **Reports** application:

{{< wideimg "back-to-reports.png" "Screenshot of Mission Portal highlighting the button to go back to the Reports screen." >}}

Then, click on **Inventory** to open up a new inventory report:

{{< wideimg "click-inventory.png" "The inventory button highlighted within the reports application." >}}

Click on **Columns** so we can add the new data as a new column:

{{< wideimg "click-columns.png" "Inventory report with information about each host, with the columns button highlighted." >}}

Use the search bar or scroll to find the new data:

{{< wideimg "etc-column.png" "Popup for editing columns and search bar for finding modules to add, highlighting a search for etc columns " >}}

After finding the inventory attribute, clicking **Add** and then **Done** we see it as a new column in the report:

{{< wideimg "inventory-with-etc-hosts.png" "New inventory report where the /etc/hosts columns is added." >}}

## What's next

This marks the end of the getting started tutorial.
You now have a good foundation to start using CFEngine, finding modules, exploring the Mission Portal web UI, and so on.
If you want to follow some more advanced tutorials, here are some that might be interesting to you:

- [Learn how to use the CFEngine Build command line tools to work with Build projects locally](/examples/tutorials/cfbs/)
- [Introduction to policy writing](/examples/tutorials/policy-writing/)
