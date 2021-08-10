---
layout: default
title: Integrating alerts with PagerDuty
sorting: 15
published: true
tags: [Examples, Tutorials, Alerts, Enterprise, Custom Actions, PagerDuty]
---

In this How To tutorial we will show you can integrate with [PagerDuty](http://www.pagerduty.com/) using the CFEngine notification dashboard.

We will create a policy that ensures file integrity, and have CFEngine notify PagerDuty whenever there is a change in the file we manage.

**System requirements:**

* CFEngine Mission Portal
* Active PagerDuty Account

<iframe width="560" height="315" src="https://www.youtube.com/embed/50ia1ZPfbT8" frameborder="0" allowfullscreen></iframe>

## Create the file we want to manage

Run the following command on your policy server to create the file we want to manage.

```console
# touch /tmp/file-integrity
```

## Create a new policy to manage the file

Insert the following policy into `/tmp/file_example.cf`

```cf3
bundle agent file_integrity
{
  files:
    any::
      "/tmp/test-integrity" -> {"PCI-DSS-2", "SOX-nightmare"}
        handle => "ensure-test-file-integrity",
        changes => change_detection;
}

body changes change_detection
{
 hash => "md5";
 update_hashes => "true";
 report_changes => "all";
 report_diffs => "true";
}
```

## Ensure the policy always runs

Normally, to ensure your policy file is put into action, you would need to follow these three steps:

1. Move the policy file to your masterfiles directory (`/var/cfengine/masterfiles`):

    Normally, to ensure your policy file is put into action, you would need to follow these three steps:

    ```console
    # mv /tmp/file_example.cf /var/cfengine/masterfiles/
    ```

2. Modify `promises.cf` to include your policy

   Unless you use version control system, or has a non-standard CFEngine setup, modify your `promises.cf` file by adding the new bundlename and policy-file so it will be picked up by CFEngine to be included in all future runs.

   ```console
   # vi /var/cfengine/masterfiles/promises.cf
   ```

   a) Under the body common control, add `file_integrity` to your *bundlesequence*

      ![integrating-alerts-with-pagerduty_bundlesequence-800x357.png](integrating-alerts-with-pagerduty_bundlesequence-800x357.png)

   b) Under `body common control`, add `file_example.cf` to your inputs section.

      ![integrating-alerts-with-pagerduty_inputs-800x179.png](integrating-alerts-with-pagerduty_inputs-800x179.png)

   Now, any change you manually make to the `/tmp/file_integrity` file will be picked up by CFEngine!

   Next we need to a new service in PagerDuty which we will notify whenever a change is detected by CFEngine.

## Create a new Service in PagerDuty

1. Go to PagerDuty.com. In your account, under Services tab, click `Add New Service`

   ![integrating-alerts-with-pagerduty_Services_-_PagerDuty.png](integrating-alerts-with-pagerduty_Services_-_PagerDuty.png)

2. Enter a name for the service and select an escalation policy. Select `Integrate via email.` Copy the integration email provided for use in CFEngine.

   ![integrating-alerts-with-pagerduty_CFEngine-Service-Setup-800x512.png](integrating-alerts-with-pagerduty_CFEngine-Service-Setup-800x512.png)

3. Click `Add Service` button. Copy the integration email which we will use in CFEngine.

## Create a new Alert in CFEngine Mission Portal

1. Go to the the CFEngine Dashboard and click `Add` button to create a new alert.

   ![integrating-alerts-with-pagerduty_new_alert1.png](integrating-alerts-with-pagerduty_new_alert1.png)

2. Fill out a new alert name `File integrity demo`, severity level `High` and name for the condition `File integrity demo`.

   ![integrating-alerts-with-pagerduty_new_alert_details.png](integrating-alerts-with-pagerduty_new_alert_details.png)

3. Select `Policy` under type

   ![integrating-alerts-with-pagerduty_type_policy.png](integrating-alerts-with-pagerduty_type_policy.png)

4. Select `Bundle`, type in the bundle name which is *file_integrity*, and finally select `Repaired` as the promise status. This means that whenever CFEngine needs to repair the bundle, it will create an alert notification.

   ![integrating-alerts-with-pagerduty_new_alert_bundle_repair.png](integrating-alerts-with-pagerduty_new_alert_bundle_repair.png)

5. Type in the integration email defined above in the Notifications section. Press `Save` to active the alert. Choose any name you like for the New widget. In our demo we name the widget `PagerDuty`.

   **Integration complete!**

   ![integrating-alerts-with-pagerduty_notification.png](integrating-alerts-with-pagerduty_notification.png)

## Test it!

Now we have a made a policy to monitor the `/tmp/file-integrity` file. Whenever there is a change to this file, whether it be permissions or content, this will be detected by CFEngine which will send a notification to PagerDuty.

1. Make a change to the `/tmp/file_integrity` file on your policy server:

   ```console
   # echo "Hello World!!" > /tmp/file_integrity
   ```

   The next time CFEngine runs, it will detect the change and send an notification to PagerDuty. Go to PagerDuty and wait for an alert to be triggered.

   ![integrating-alerts-with-pagerduty_pagerduty_new_alert.png](integrating-alerts-with-pagerduty_pagerduty_new_alert.png)
