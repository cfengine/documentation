---
layout: default
title: Promise Types and Attributes
published: true
sorting: 20
tags: [reference, bundles, common, promises]
---

Within a bundle, the promise types are executed in a round-robin fashion in the
following [normal ordering][Normal Ordering]. Which promise types are available
depends on the [bundle][bundles] type:

| Promise Type   | common | agent | server | monitor |
|----------------|:------:|:-----:|:------:|:--------|
| [defaults][defaults] - a default value for bundle parameters | x      | x     | x      | x       |
| [classes][classes] - a class, representing a state of the system | x      | x     | x      | x       |
| [meta][meta] - information about promise bundles | x      | x     | x      | x       |
| [reports][reports] - report a message | x      | x     | x      | x       |
| [vars][vars] - a variable, representing a value | x      | x     | x      | x       |
| [commands][commands] - execute a command |        | x     |        |         |
| [databases][databases] - configure a database |        | x     |        |         |
| [files][files] - configure a file |        | x     |        |         |
| [packages][packages] - install a package |        | x     |        |         |
| [guest_environments][guest_environments] |        | x     |        |         |
| [methods][methods] - take on a whole bundle of other promises |        | x     |        |         |
| [processes][processes] - start or terminate processes |        | x     |        |         |
| [services][services] - manage services or define new abstractions |        | x     |        |         |
| [storage][storage] - verify attached storage |        | x     |        |         |
| [users][users] - add or remove users |        | x     |        |         |
| [access][access] - grant or deny access to file objects |        |       | x      |         |
| [roles][roles] - allow certain users to activate certain classes |        |       | x      |         |
| [measurements][measurements] - measure or sample data from the system |        |       |        | x       |

See each promise type's reference documentation for detailed lists of available
attributes.

## Common Body Attributes

The following attributes are available to all body types.

### inherit_from

**Description:** Inherits all attributes from another body of the same
type as a function call. For a detailed description, see
[**Bodies**][bodies].

**Type:** `fncall`

**Allowed input range:** (arbitrary body invocation)

**Example:**

A simple example first, which has no parameters:

```cf3
    body TYPE parent
    {
      atribute1 => 100;
      atribute2 => { "a" };
      atribute3 => 75;
    }

    body TYPE child
    {
      inherit_from => parent; # same as parent()
      atribute3 => 300; # overwrites parent's attribute3
      # has atribute1 => 100;
      # has atribute2 => { "a" };
    }
```

Now with parameters. The child calls the parent as a function call.
Note that the child's parameters can be passed up to the parent.

```cf3
    body TYPE parent(a1, a2)
    {
      atribute1 => $(a1);
      atribute2 => { $(a2) };
      atribute3 => 75;
    }

    body TYPE child(aaa)
    {
      inherit_from => parent(5, $(aaa));
      atribute3 => 300; # overwrites parent's attribute3
      # has atribute1 => 5;
      # has atribute2 => { $(aaa) };
    }
```

**History:** Was introduced in 3.8.0.

### meta

**Description:** A list of meta attributes.

**Type:** `slist`

**Allowed input range:** (arbitrary string list)

**Example:**

```cf3
    body ANYTYPE mybody
    {
      meta => { "deprecated" };
    }
```

**Note:** When a variable is re-defined the associated meta attributes are also
re-defined.

**History:** Was introduced in 3.7.0.

