### 1.10 Testing as a non-privilieged user

One of the practical advantages of CFEngine is that you can test it
without the need for root or administrator privileges. This is
recommended for all new users of CFEngine 3.

CFEngine operates with the notion of a work-directory. The default
work directory for the `root` user is /var/cfengine (except on
Debian Linux and various derivatives which prefer
/var/lib/cfengine). For any other user, the work directory lies in
the user's home directory, named \~/.cfagent. CFEngine prefers you
to keep certain files here. You should not resist this too strongly
or you will make unnecessary trouble for yourself. The decision to
have this \`known directory' was made to simplify a lot of
configuration.

To test CFEngine as an ordinary user, do the following:

-   Compile and make the software.
-   Copy the binaries into the work directory:
                  host$ mkdir -p ~/.cfagent/inputs
                  host$ mkdir -p ~/.cfagent/bin
                  host$ cd src
                  host$ cp cf-* ~/.cfagent/bin
                  host$ cd ../inputs
                  host$ cp *.cf ~/.cfagent/inputs


You can test the software and play with configuration files by
editing the basic get-started files directly in the
\~/.cfagent/inputs directory. For example, try the following:

         host$ ~/.cfagent/bin/cf-promises
         host$ ~/.cfagent/bin/cf-promises --verbose

This is always the way to start checking a configuration in
CFEngine 3. If a configuration does not pass this check/test, you
will not be allowed to use it, and cf-agent will look for the file
failsafe.cf.

Notice that the CFEngine 3 binaries have slightly different names
than the CFEngine 2 binaries. They all start with the cf- prefix.

         host$ ~/.cfagent/bin/cf-agent

