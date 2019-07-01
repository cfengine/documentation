---
layout: default
title: Federated Reporting
published: true
sorting: 55
---

## Overview ##

Federated Reporting enables the collection of data from multiple Hubs to provide a view in Mission Portal which can scale up beyond the capabilities of a Hub which manages hosts. CFEngine supports a large number of hosts per hub, around 5,000 hosts per hub depending on many factors. With Federated Reporting it is possible to scale up to 100,000 hosts or more for the purposes of analysis and reporting.

Hubs which hosts report to are called Feeder Hubs.

The hub which collects information from Feeder Hubs is called the Superhub.

If all hubs are version 3.14.0 or higher then Mission Portal can be used to configure and connect the Superhub and Feeder hubs. For Feeder hubs with an earlier version than 3.14.0 an API and manual steps must be followed. This documentation will be provided soon.

## Installation ##

The [General Installation][General Installation] instructions should be used to install CFEngine Hub on a Superhub as well as Feeder hubs.

## Setup ##

### Enable Hub management app ###

![Enable Hub Management](fr-hub-management-enabled.png)

On the Superhub and all Feeder enable the Hub management
app by [Opening Settings] then selecting [Manage Apps] and finally
by clicking the `On` radio button for Hub management in the Status column (fr-hub-management-enabled.png)

### Enable Federated Reporting ###

![Enable Federated Reporting](fr-hub-management-default.png)

The Hub management app should now appear in the bottom left corner of mission portal.

Click on the Enable Superhub or Enable Feeder button as appropriate.
This will cause some configuration to be written in the filesystem and on next agent run policy will make the needed changes. You can speed up this process by running the agent manually.

### Connect Feeder Hubs ###

![Connect Feeder Hubs](fr-superhub-enabled-no-feeders.png)

Refresh the Hub management on each hub to see that Federated Reporting is enabled.

After all hubs have Federated Reporting enabled visit Hub management on the Superhub
to connect the Feeder hubs.

Click on the Connect hub button to show the Connect a hub dialog.

![Connect a hub](fr-connect-a-hub.png)

Fill out the form with the base URL of your feeder hub Mission Portal and enter credentials for a user with administrative credentials.
These credentials will only be used to authenticate to the feeder hub and will not be saved otherwise.

The Hub management view will show all connected hubs, the number of bootstrapped hosts and allow you to edit the settings.

![Feeders connected](fr-feeder-added.png)

## Operation ##

Now that everything is configured the Feeder hubs will generate a database
dump every 20 minutes and the Superhub will pull any available dumps from
each Feeder every 20 minutes as well.

You can test import immediately by running the agent on the feeders and then
the superhub.

## Troubleshooting ##

Please refer to `/var/cfengine/output`, `/var/log/postgresql.log` and  `/opt/cfengine/federation/superhub/import/*.log.gz`
when problems occur. Sending these logs to us in bug reports will help significantly as we fine tune the Federated
Reporting feature.
