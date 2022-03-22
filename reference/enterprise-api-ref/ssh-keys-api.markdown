---
layout: default title: SSH keys API published: true tags: [reference, enterprise, API, build, SSH]
---

The SSH keys API enables you to generate a key pair that can be used for authorization.

# SSH keys API

## Generate SSH key

Generates a key with 4096 bits, sha2-512 digest and in rfc4716 (default openssh) format.

**URI:** https://hub.cfengine.com/api/ssh-key

**Method:** POST

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/ssh-key 
```

**Successful response example:**

```
HTTP 200 Ok
{
    "id": 2,
    "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8M3W9juaAvGVqL7j37iukojCAAqwL2KkArlOMJhmEc5xrEs3/v8pz4/tu2sTdCyVjML3PUZUeUZq8dorSUDn1b7co1LpQsAt5z3AF1yLPGtfivEUsBD96G6fCHTsayHZM8yojjHN2gydDDmlvoTntdH3BcOLA2Pw5iUCQrPpXX23DdqOJENDLn67w6H8dqxbObZlt0niJbGwmNNz16lCii0Lf9SYS8SPPsbPprU1zmNKxEzd32PFl1k0544RMdXGWOpt79batVDGrQVooH5ESm08ODFgdSOD6wPMTQ5+VUC7SCLstODEia9f9/ZajFn14rDzC5ICZT/GNrtqWiHjr5TCwsr+V/EfwlEGYl6eRJ5K3MWIZqFXPpLCllZZYw90dA0VW74O7gL6uWWXQQDeRdBvwuJkBSvH+S4UB+VF+f+c55pH37tGf+WLHUc+m26qOrPJUnxTvHWcH09EUh1nELiHs1OZPwc7CF3ijRKIo3Xm3R45YFXREbfOJFb2XYuxBp0OSRAcqy2aVdST1hlt+NZuhtMKLKT30YkwYgkpl52Y0LpReUaG7ENQxvA5/6Js8vTQPjiTLbOw4L8/nDANCtAavytX3BvTJGbJU0VsErJ50I13xIake/owJzKbfxxLJhBNpllZY8IhSquIyl9S851eB743Bbiufpngk8fEPzw== generated-by-cfengine-ssh-api"
}
```

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 200 OK | SSH key successfully created |
| 500 Internal server error | Internal server error |

## Get SSH keys list

**URI:** https://hub.cfengine.com/api/ssh-key

**Method:** GET

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/ssh-key
```

**Successful response example:**

```
HTTP 200 OK
[
    {
        "id": 2,
        "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8M3W9juaAvGVqL7j37iukojCAAqwL2KkArlOMJhmEc5xrEs3/v8pz4/tu2sTdCyVjML3PUZUeUZq8dorSUDn1b7co1LpQsAt5z3AF1yLPGtfivEUsBD96G6fCHTsayHZM8yojjHN2gydDDmlvoTntdH3BcOLA2Pw5iUCQrPpXX23DdqOJENDLn67w6H8dqxbObZlt0niJbGwmNNz16lCii0Lf9SYS8SPPsbPprU1zmNKxEzd32PFl1k0544RMdXGWOpt79batVDGrQVooH5ESm08ODFgdSOD6wPMTQ5+VUC7SCLstODEia9f9/ZajFn14rDzC5ICZT/GNrtqWiHjr5TCwsr+V/EfwlEGYl6eRJ5K3MWIZqFXPpLCllZZYw90dA0VW74O7gL6uWWXQQDeRdBvwuJkBSvH+S4UB+VF+f+c55pH37tGf+WLHUc+m26qOrPJUnxTvHWcH09EUh1nELiHs1OZPwc7CF3ijRKIo3Xm3R45YFXREbfOJFb2XYuxBp0OSRAcqy2aVdST1hlt+NZuhtMKLKT30YkwYgkpl52Y0LpReUaG7ENQxvA5/6Js8vTQPjiTLbOw4L8/nDANCtAavytX3BvTJGbJU0VsErJ50I13xIake/owJzKbfxxLJhBNpllZY8IhSquIyl9S851eB743Bbiufpngk8fEPzw== generated-by-cfengine-ssh-api",
        "generated_by": "admin",
        "generated_at": "2022-07-06 09:03:31.559311+00"
    },
    {
        "id": 3,
        "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCkm7yAi4Np5TBl4GGmZ3FDUW3QT/1/1EMimBfzNl8wHggLnImeENwvd/tBmtrt3fbz8IVVnpytspbMlqrejQdhiCORMvNNVmV3q7pdWDgeHccVDiugl16+OS7VvNnU7YzbWcSjcS1KXqGS3p/PWEDgejLRre8Jju9v43DD76A2A6InYuCdQt4cpRoqPhsZiro65UIrUb5VzaKfQlS7vD7wBtrsXmDO0L3YFw4lQMCqISnDNLhG57qtT8kjFXsuKnCTsMnt1QtTqUSuYPFiTdPTjVuAGVNtiRoM7BU3jmxcOs0Y+pwIb3TyO3cK+gbY3+gSsHVLsEfgY9fljtV3iWu+EJMEASCTHgrh4OU3homeT+msS7zpE19covoC8+Qg0Z5dGlWEfgoQ2Y87PqjZZ9j+3KmHJcXvdYfdpXD3UHbwyM1Gfzl6IMK7QqQoyS0QXNM/3GLdiZf5Orf4ZbHRdkBEY/tZlEZSMLA6NVtU2eck6FEOime6/+2lS1Ai9ofgGglq0P5eT5k/eFrhFWy05yvKc1pVe9jjk4wdhHzJ28ffdkgNumDMlrbTKgPaxwIKWTOgMunnHWJZJqm1oJPeLT7OgQN3B1eabxfT/XRo0TA2QCRLR1fNYEzkK/RFQifoWK7tc+k5mshPs6I7ZIAQ7KXS/otccj+5mWjspJoHHAbYgw== generated-by-cfengine-ssh-api",
        "generated_by": "admin",
        "generated_at": "2022-07-06 09:04:53.476701+00"
    }
]
```

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 200 Ok | Successful response  |
| 500 Internal server error | Internal server error |

## Get SSH key

**URI:** https://hub.cfengine.com/api/ssh-key/:id

**Method:** GET

**Parameters:**

* **id** *(integer)*
  SSH key ID. Required.

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/ssh-key/2
```

**Successful response example:**

```
HTTP 200 OK
{
    "id": 2,
    "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8M3W9juaAvGVqL7j37iukojCAAqwL2KkArlOMJhmEc5xrEs3/v8pz4/tu2sTdCyVjML3PUZUeUZq8dorSUDn1b7co1LpQsAt5z3AF1yLPGtfivEUsBD96G6fCHTsayHZM8yojjHN2gydDDmlvoTntdH3BcOLA2Pw5iUCQrPpXX23DdqOJENDLn67w6H8dqxbObZlt0niJbGwmNNz16lCii0Lf9SYS8SPPsbPprU1zmNKxEzd32PFl1k0544RMdXGWOpt79batVDGrQVooH5ESm08ODFgdSOD6wPMTQ5+VUC7SCLstODEia9f9/ZajFn14rDzC5ICZT/GNrtqWiHjr5TCwsr+V/EfwlEGYl6eRJ5K3MWIZqFXPpLCllZZYw90dA0VW74O7gL6uWWXQQDeRdBvwuJkBSvH+S4UB+VF+f+c55pH37tGf+WLHUc+m26qOrPJUnxTvHWcH09EUh1nELiHs1OZPwc7CF3ijRKIo3Xm3R45YFXREbfOJFb2XYuxBp0OSRAcqy2aVdST1hlt+NZuhtMKLKT30YkwYgkpl52Y0LpReUaG7ENQxvA5/6Js8vTQPjiTLbOw4L8/nDANCtAavytX3BvTJGbJU0VsErJ50I13xIake/owJzKbfxxLJhBNpllZY8IhSquIyl9S851eB743Bbiufpngk8fEPzw== generated-by-cfengine-ssh-api",
    "generated_by": "admin",
    "generated_at": "2022-07-06 09:03:31.559311+00"
}
```

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 200 Ok | Successful response  |
| 404 Not found | SSH key not found |
| 500 Internal server error | Internal server error |

## Delete SSH key

**URI:** https://hub.cfengine.com/api/ssh-key/:id

**Method:** DELETE

**Parameters:**

* **id** *(integer)*
  SSH key ID. Required.

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/ssh-key/2
```

**Successful response example:**

```
HTTP 204 No content
```

**Responses:**

| HTTP response code | Description |
|--------|-------------|
| 204 No content | SSH key successfully deleted |
| 404 Not found | SSH key not found |
| 500 Internal server error | Internal server error |
