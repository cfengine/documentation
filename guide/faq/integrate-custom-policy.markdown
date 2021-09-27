---
layout: default
title: How do I integrate custom policy?
published: true
sorting: 90
tags: [getting started, installation, faq]
---

There are many different ways that custom polices can be organized. CFEngine
does not prescribe any specific organizational layout but generally speaking
keeping custom policy files under as few different paths as possible can ease
policy framework upgrades.

For example, it is common to store custom policy files under `services/SERVICE`
or `ORGINIZATION` from the root of your policy set.

Here we only describe ways to include and execute custom policies.

## Using autorun

The *autorun* feature in the Masterfiles Policy Framework automatically adds
policy files found in `services/autorun` to inputs and executes bundles tagged
with *autorun* as methods type promises in lexical order.

**See also:** [`services_autorun` in the Masterfiles Policy Framework][Masterfiles Policy Framework#services\_autorun]

## Using augments

Augments uses the `inputs` key to define `def.augments_inputs` which is included
in inputs of body common control in promises.cf by default.

```json
{
    "inputs": [ "my_update.cf" ]
}
```

Alternatively you can define `augments_inputs` directly.

```json
{
    "vars": {
        "augments_inputs": [ "my_policy.cf" ]
    }
}
```

To extend inputs in the update policy define `update_inputs`.

```json
{
    "vars": {
        "update_inputs": [ "my_update.cf" ]
    }
}
```

**See also:** [Augments][Augments], [Extend inputs for update policy in the Masterfiles Policy Framework][Masterfiles Policy Framework#Append to inputs used by update policy]

## Using body file control

*inputs* in `body file control` can be used to load additional policy files.
This can be very useful for loading policy files that are relative to each
other.

**NOTES:**

-   `body file control` can **not** be used to specify bundles that should be executed.
-   `this.promise_*` variables can **not** be used directly in `body file control`.
   
   ```cf3
   body file control
   {
     inputs => { "$(this.policy_dirname)/../stdlib.cf" };
   }
   ```
    
    Bundle variables can be used to achieve relative inputs. 
    
   ```cf3
   bundle common example_file_control
   {
      vars:
        "policy[stdlib]"
          string => "$(this.policy_dirname)/../my_other_policy.cf";
   
        "inputs" slist => getvalues( policy );
   }
   
   body file control
   {
     inputs => { "$(example_file_control.inputs)" };
   }
   ```

-   `sys.policy_*` variables **can** be used directly in `body file control`.
    
   ```cf3
   body file control
   {
     inputs => { "$(sys.policy_entry_dirname)/lib/stdlib.cf" };
   }
   ```

**See also:** [`inputs` in `body file control`][file control#inputs]

## Using body common control

`body common control` is the classic way to define the list of policy files that
make up the policy set ( *inputs* ), and the order of the bundles to be executed
( *bundlesequence* ).

**See also:** [`inputs` in `body common control`][Components#inputs], [`bundlesequence` in `body common control`][Components#bundlesequence]

