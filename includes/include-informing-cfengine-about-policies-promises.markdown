Once bundles of promises have been written, CFEngine needs to know about them. The place where this generally happens is in the file `/var/cfengine/masterfiles/promises.cf`, but there may be cases where the information occurs in another file and referenced within `promises.cf`.

#### Anatomy of promises.cf ####

The default anatomy of file `/var/cfengine/masterfiles/promises.cf` looks something like the following (`#` marks comments, while `...` marks omitted text):

```cf3
body common control

{

      bundlesequence => {
						  # Here is a comment about bundlesequences, which are the bundles where promises can be found
                          name_of_a_bundle,
						  # Sometimes it is more efficient to use lists -- see 'bundle common stuff' below
						  @(stuff.bundles),
                          ...
      };

      inputs => {
                  #Here is a comment about inputs, which are the files that contain the bundles identified within the bundlesequences section
                  "name_of_file_where_the_bundle_exists.cf",
				  
				  # Sometimes it is more efficient to use lists -- see 'bundle common stuff' below
				  @(stuff.inputs),
				  ...

      };

      version => "CFEngine Promises.cf 3.6.0";

}

bundle common stuff
{
  vars:
      "inputs" slist => { "stuff/any.cf", "stuff/hello.cf", "stuff/world.cf" };
      "bundles" slist => { "stuff_control", "stuff_any", "stuff_autorun", "stuff_hello", "stuff_world" };

  reports:
    verbose_mode::
      "$(this.bundle): loading stuff module '$(inputs)'";
}
```


