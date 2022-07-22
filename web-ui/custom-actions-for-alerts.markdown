---
layout: default
title: Custom actions for Alerts
sorting: 50
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

Once you have become familiar with the [Alerts widgets][Web UI#Alert widgets], you might see the need to integrate the alerts with an existing system like Nagios, instead of relying on emails for getting notified.

This is where the Custom actions come in. A Custom action is a way to execute a script on the hub whenever an alert is triggered or cleared, as well as when a reminder happens (if set). The script will receive a set of parameters containing the state of the alert, and can do practically anything with this information. Typically, it is used to integrate with other alerting or monitoring systems like PagerDuty or Nagios.

Any scripting language may be used, as long as the hub has an interpreter for it.


## Alert parameters ##

The Custom action script gets called with one parameter: the path to a file with a set of KEY=VALUE lines.
Most of the keys are common for all alerts, but some additional keys are defined based on the alert type, as shown below.


### Common keys ###

These keys are present for all alert types.

| Key                         | Description                                                                                           |
|-----------------------------|-------------------------------------------------------------------------------------------------------|
| ALERT_ID                    | Unique ID (number).                                                                          |
| ALERT_NAME                  | Name, as defined in when creating the alert (string).                                                    |
| ALERT_SEVERITY              | Severity, as selected when creating the alert (string).                                                |
| ALERT_LAST_CHECK            | Last time alert state was checked (Unix epoch timestamp).                                              |
| ALERT_LAST_EVENT_TIME       | Last time the alert created an event log entry (Unix epoch timestamp).                                 |
| ALERT_LAST_STATUS_CHANGE    | Last time alert changed from triggered to cleared or the other way around (Unix epoch timestamp).      |
| ALERT_STATUS                | Current status, either 'fail' (triggered) or 'success' (cleared).                                      |
| ALERT_FAILED_HOST           | Number of hosts currently triggered on (number).                                                       |
| ALERT_TOTAL_HOST            | Number of hosts defined for (number).                                                                  |
| ALERT_CONDITION_NAME        | Condition name, as defined when creating the alert (string).                                             |
| ALERT_CONDITION_DESCRIPTION | Condition description, as defined when creating the alert (string).                                      |
| ALERT_CONDITION_TYPE        | Type, as selected when creating the alert. Can be 'policy', 'inventory', or 'softwareupdate'. |



### Policy keys ###

In addition to the common keys, the following keys are present when ALERT_CONDITION_TYPE='policy'.

| Key                                   | Description                                                                                                      |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------|
| ALERT_POLICY_CONDITION_FILTERBY       | Policy object to filter by, as selected when creating the alert. Can be 'bundlename', 'promiser' or 'promisees'.  |
| ALERT_POLICY_CONDITION_FILTERITEMNAME | Name of the policy object to filter by, as defined when creating the alert (string).                              |
| ALERT_POLICY_CONDITION_PROMISEHANDLE  | Promise handle to filter by, as defined when creating the alert (string).                                         |
| ALERT_POLICY_CONDITION_PROMISEOUTCOME | Promise outcome to filter by, as selected when creating the alert. Can be either 'KEPT', 'REPAIRED' or 'NOTKEPT'. |


### Inventory keys ###

In addition to the common keys, the following keys are present when ALERT_CONDITION_TYPE='inventory'.

| Key                                                          | Description                                                                                                                                                                                                                                    |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALERT_INVENTORY_CONDITION_FILTER_$(ATTRIBUTE_NAME)           | The name of the attribute as selected when creating the alert is part of the key (expanded), while the value set when creating is the value (e.g. ALERT_INVENTORY_CONDITION_FILTER_ARCHITECTURE='x86_64').                                      |
| ALERT_INVENTORY_CONDITION_FILTER_$(ATTRIBUTE_NAME)_CONDITION | The name of the attribute as selected when creating the alert is part of the key (expanded), while the value is the comparison operator selected. Can be 'ILIKE' (matches), 'NOT ILIKE' (doesn't match), '=' (is), '!=' (is not), '<', '>'. |
| ...                                                          | There will be pairs of key=value for each attribute name defined in the alert.                                                                                                                                                                |

### Software updates keys ###

In addition to the common keys, the following keys are present when ALERT_CONDITION_TYPE='softwareupdate'.

| Key                                               | Description                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------|
| ALERT_SOFTWARE_UPDATE_CONDITION_PATCHNAME         | The name of the package, as defined when creating the alert, or empty if undefined (string).         |
| ALERT_SOFTWARE_UPDATE_CONDITION_PATCHARCHITECTURE | The architecture of the package, as defined when creating the alert, or empty if undefined (string). |


## Example parameters: policy bundle alert not kept ##

Given an alert that triggers on a policy bundle being not kept (failed), the following is example content of the file being provided as an argument to a Custom action script.

    ALERT_ID='6'
    ALERT_NAME='Web service'
    ALERT_SEVERITY='high'
    ALERT_LAST_CHECK='0'
    ALERT_LAST_EVENT_TIME='0'
    ALERT_LAST_STATUS_CHANGE='0'
    ALERT_STATUS='fail'
    ALERT_FAILED_HOST='49'
    ALERT_TOTAL_HOST='275'
    ALERT_CONDITION_NAME='Web service'
    ALERT_CONDITION_DESCRIPTION='Ensure web service is running and configured correctly.'
    ALERT_CONDITION_TYPE='policy'
    ALERT_POLICY_CONDITION_FILTERBY='bundlename'
    ALERT_POLICY_CONDITION_FILTERITEMNAME='web_service'
    ALERT_POLICY_CONDITION_PROMISEOUTCOME='NOTKEPT'

Saving this as a file, e.g. 'alert_parameters_test', can be useful while writing and testing your Custom action script.
You could then simply test your Custom action script, e.g. 'cfengine_custom_action_ticketing.py', by running

    ./cfengine_custom_action_ticketing alert_parameters_test

When you get this to work as expected on the commmand line, you are ready to upload the script to the Mission Portal, as outlined below.


## Example script: logging policy alert to syslog ##

The following Custom action script will log the status and definition of a policy alert to syslog.

    #!/bin/bash

    source $1

    if [ "$ALERT_CONDITION_TYPE" != "policy" ]; then
       logger -i "error: CFEngine Custom action script $0 triggered by non-policy alert type"
       exit 1
    fi

    logger -i "Policy alert '$ALERT_NAME' $ALERT_STATUS. Now triggered on $ALERT_FAILED_HOST hosts. Defined with $ALERT_POLICY_CONDITION_FILTERBY='$ALERT_POLICY_CONDITION_FILTERITEMNAME', promise handle '$ALERT_POLICY_CONDITION_PROMISEHANDLE' and outcome $ALERT_POLICY_CONDITION_PROMISEOUTCOME"

    exit $?

What gets logged to syslog depends on which alert is associated with the script, but an example log-line is as follows:

    Sep 26 02:00:53 localhost user[18823]: Policy alert 'Web service' fail. Now triggered on 11 hosts. Defined with bundlename='web_service', promise handle '' and outcome NOTKEPT



## Uploading the script to the Mission Portal ##

Members of the admin role can manage Custom action scripts in the Mission Portal settings.

<img src="mp-settings-custom-notification.png" alt="Custom action scripts overview" width="700px">

A new script can be uploaded, together with a name and description, which will be shown when creating the alerts.

<img src="mp-settings-custom-notification-add.png" alt="Adding Custom action syslog script" width="700px">


## Associating a Custom action with an alert ##

Alerts can have any number of Custom action scripts as well as an email notification associated with them. This can be configured during alert creation. Note that for security reasons, only members of the admin role may associate alerts with Custom action scripts.

<img src="create-alert-custom-action-syslog.png" alt="Adding Custom action script to alert" width="420px">

Conversely, several alerts may be associated with the same Custom action script.

When the alert changes state from triggered to cleared, or the other way around, the script will run. The script will also run if the alert remains in triggered state and there are reminders set for the alert notifications.
