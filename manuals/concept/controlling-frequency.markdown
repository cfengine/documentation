---
layout: default
title: Controlling Frequency
categories: [Manuals, Concept Guide, Controlling Frequency]
published: true
alias: manuals-concept-controlling-frequency.html
tags: [manuals, concepts, controlling, frequency, performance]
---

### Controlling Frequency

When checking a series of expensive functions and verifying complex promises, you may want to make sure that CFEngine is not checking too frequently. CFEngine incorporates a series of locks which prevent it from checking promises too often, and which prevent it from spending too long trying to check promises it has recently verified. 

This locking mechanism works in such a way that you can start several CFEngine components simultaneously without having to worry about conflicts between these processes. You can control two things about each kind of action in CFEngine:

'‘ifelapsed'::
    The minimum time (in minutes) which should have passed since the last time that promise was verified. It will not be executed again until this amount of  time has elapsed. (Default time is 1 minute.) 

'‘expireafter'::
    The maximum amount (in minutes) of time cf-agent should wait for an old instantiation to finish before killing it and starting again.  You can think about expireafter as a timeout to use when a promise verification may involve an operation that could wait indefinitely. (Default time is 120  minutes.)

You can set these values either globally (for all actions) or for each action separately. If you set global and local values, the local values override the global ones. All times are written in units of minutes. The following global setting is defined in "body agent control".  This setting tells CFEngine not to verify promises until 60 minutes have elapsed.  This would ensure that the global frequency for all promise verification is one hour:

    body agent control
    {
        ifelapsed => "60";	# one hour
    }

This global setting of one hour could be changed for a specific promise body by setting ifelapsed in the promise body.   Here we see a promise which overrides the global 60 minute time period and defines a promise with a frequency of 90 minutes.

    body action example
    {
        ifelapsed => "90";	# 1.5 hours
    }

These locks do not prevent the whole of cf-agent from running, only atomic promise checks. Several different processes (or atoms) can be run concurrently by different cf-agent instnaces. The locks ensure that atoms will never be started by two cf-agents at the same time, or too soon after a verification, causing contention and wasting CPU cycles.       
