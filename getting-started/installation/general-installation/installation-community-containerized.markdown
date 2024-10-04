---
layout: default
title: Installing Community Using Containers
published: true
sorting: 80
---

The instructions in this guide describe how to download and install the latest version of CFEngine Community in a Docker containerized environment using pre-compiled rpm packages and ubi9 images.

This guide describes how to set up a client-server model with CFEngine and, through policy, manage both containers.

Docker containers will be created, one container to be the Policy Server (server), and another container that will be the Host Agent (client).

Both the containers will run **_ubi9-init_** images and communicate on a container network.
Upon completion, you are ready to start working with CFEngine.


## Requirements
* 1G+ disk space
* 1G+ memory
* Working [Docker Engine](https://docs.docker.com/engine/) or [Podman](https://podman.io/) setups on a supported [x86_64](https://en.wikipedia.org/wiki/X86-64) platform.

**Note**: This document considers [Docker Engine](https://docs.docker.com/engine/) for all examples.
Use of [Podman](https://podman.io/) shall be similar with adequate adaptations. (_Ref_: [Emulating Docker CLI with Podman](https://podman-desktop.io/docs/migrating-from-docker/emulating-docker-cli-with-podman)).

## Overview
1. Installing container engine
2. Preparing CFEngine hub in container
3. Preparing CFEngine host in container
4. Using docker compose
    1. Preparing container image for CFEngine
    2. Using docker compose service
5. Glossary
6. References

## Installing container engine
**Ref**: [Install Docker Engine](https://docs.docker.com/engine/install/)

OR

**Ref**: [Podman Installation Instructions](https://podman.io/docs/installation)
(_Optionally_: [Emulating Docker CLI with Podman](https://podman-desktop.io/docs/migrating-from-docker/emulating-docker-cli-with-podman))

## Preparing CFEngine hub in container
Run the container with systemd

```command
docker run --privileged -dit --name=cfengine-hub registry.access.redhat.com/ubi9-init /usr/sbin/init
```

Prepare the container for **cfengine-hub**

```command
docker exec cfengine-hub bash -c "dnf -y update; dnf -y install procps-ng iproute"
```

Install cfengine-community package

```command
docker exec cfengine-hub bash -c "dnf -y install https://cfengine-package-repos.s3.amazonaws.com/community_binaries/Community-3.24.0/agent_rhel9_x86_64/cfengine-community-3.24.0-1.el9.x86_64.rpm"
```

Bootstrap cf-agent

```command
docker exec cfengine-hub bash -c "/usr/local/sbin/cf-agent --bootstrap \$(ip -4 -o addr show eth0 | awk '{print \$4}' | cut -d'/' -f1)"
```

## Preparing CFEngine host in container
The procedure to setup **cfengine-host** is similar to the **cfengine-hub** deployment. The changes are to name of the host container for better identification and bootstrap IP of the **cfengine-hub**.

```command
docker run --privileged -dit --name=cfengine-host registry.access.redhat.com/ubi9-init /usr/sbin/init
```

Prepare the container for **cfengine-host**

```command
docker exec cfengine-host bash -c "dnf -y update; dnf -y install procps-ng iproute"
```

Install cfengine-community package

```command
docker exec cfengine-host bash -c "dnf -y install https://cfengine-package-repos.s3.amazonaws.com/community_binaries/Community-3.24.0/agent_rhel9_x86_64/cfengine-community-3.24.0-1.el9.x86_64.rpm"
```

### Bootstrap cfengine-host to the policy server container.
Find IP address of **cfengine-hub**:

```command
CFENGINE_HUB_IP=$(docker exec cfengine-hub bash -c "ip -4 -o addr show eth0 | awk '{print \$4}' | cut -d'/' -f1")
```

Bootstrap cfengine-host to cfengine-hub:

```command
docker exec cfengine-host bash -c "/usr/local/sbin/cf-agent --bootstrap ${CFENGINE_HUB_IP}"
```

## Using docker compose
### Preparing container image for CFEngine
Create a `Dockerfile` with following contents:

```Dockerfile
FROM registry.access.redhat.com/ubi9-init:latest
LABEL description="This Dockerfile builds container image based on ubi9-init for cfengine-community-3.24.0.1 rpm."

RUN dnf -y update \
&& dnf -y install bind-utils iproute procps-ng \
&& dnf -y install https://cfengine-package-repos.s3.amazonaws.com/community_binaries/Community-3.24.0/agent_rhel9_x86_64/cfengine-community-3.24.0-1.el9.x86_64.rpm

HEALTHCHECK --interval=5s --timeout=15s --retries=3 \
    CMD /usr/local/sbin/cf-agent --self-diagnostics || exit 1

ENTRYPOINT ["/usr/sbin/init"]
```

Validate the Dockerfile

```command
docker build -t cfengine:3.24.0-1 -f Dockerfile . --check
```
```output
[+] Building 0.1s (3/3) FINISHED                                        docker:default
 => [internal] load build definition from Dockerfile                            0.0s
 => => transferring dockerfile: 596B                                            0.0s
 => [internal] load metadata for registry.access.redhat.com/ubi9-init:latest    0.0s
 => [internal] load .dockerignore                                               0.0s
 => => transferring context: 2B                                                 0s
Check complete, no warnings found.
```

**Note**: You can skip to [_Using docker compose service_](#using-docker-compose-service), as the image would be built as per compose.yaml file, if not present.

Build the docker image based on above Dockerfile:

```command
docker build -t cfengine:3.24.0-1 -f Dockerfile .
```

Verify created image:

```command
docker image ls cfengine
```
```output
REPOSITORY   TAG        IMAGE ID       CREATED             SIZE
cfengine     3.24.0-1   <IMAGE_ID>     About an hour ago   302MB
```

### Using docker compose service
Create a `compose.yaml` file with following contents:

```yaml
[file=compose.yml]
name: cfengine-demo

services:
  cfengine-hub:
    container_name: cfengine-hub
    image: cfengine:3.24.0-1
    build:
      context: .
      dockerfile: Dockerfile
    privileged: true
    command:
      - /bin/sh
      - -c
      - |
        "/usr/local/sbin/cf-agent --bootstrap $(ip -4 -o addr show eth0 | awk '{print $4}' | cut -d'/' -f1)"
    networks:
      - control-plane

  cfengine-host:
    image: cfengine:3.24.0-1
    build:
      context: .
      dockerfile: Dockerfile
    privileged: true
    command:
      - /bin/sh
      - -c
      - |
        "/usr/local/sbin/cf-agent --bootstrap $(dig +short cfengine-hub|tr -d [:space:])"
    networks:
      - control-plane
    depends_on:
      cfengine-hub:
        condition: service_healthy
        required: true

networks:
  control-plane:
```

Validate the `compose.yaml` file

```command
docker compose -f compose.yaml config 1>/dev/null
```
**Note**: No output means valid yaml file.

Start service cfengine-demo

```command
docker compose -f compose.yaml up -d
```

Bootstrap hub and hosts

```command
docker exec -it cfengine-hub bash -c "/usr/local/sbin/cf-agent --bootstrap \$(ip -4 -o addr show eth0 | awk '{print \$4}' | cut -d'/' -f1)"
```
```output
R: Bootstrapping from host '192.168.16.2' via built-in policy '/var/cfengine/inputs/failsafe.cf'
R: This host assumes the role of policy server
R: Updated local policy from policy server
R: Triggered an initial run of the policy
R: Restarted systemd unit cfengine3
notice: Bootstrap to '192.168.16.2' completed successfully!
```

```command
docker exec -it cfengine-demo-cfengine-host-1 bash -c "/usr/local/sbin/cf-agent --bootstrap \$(dig +short cfengine-hub|tr -d [:space:])"
```
```output
notice: Bootstrap mode: implicitly trusting server, use --trust-server=no if server trust is already established
notice: Trusting new key: MD5=2f406e11cfd3e08d810d77a186e204e2
R: Bootstrapping from host '192.168.16.2' via built-in policy '/var/cfengine/inputs/failsafe.cf'
R: This autonomous node assumes the role of voluntary client
R: Updated local policy from policy server
R: Triggered an initial run of the policy
R: Restarted systemd unit cfengine3
notice: Bootstrap to '192.168.16.2' completed successfully!
```

Health-check for hub and host

```command
docker exec -it cfengine-hub bash -c "/usr/local/sbin/cf-agent --self-diagnostics"
```
```output
...
[ YES ] Check that agent is bootstrapped: 192.168.16.2
[ YES ] Check if agent is acting as a policy server: Acting as a policy server
[ YES ] Check private key: OK at '/var/cfengine/ppkeys/localhost.priv'
[ YES ] Check public key: OK at '/var/cfengine/ppkeys/localhost.pub'
...
```

```command
docker exec -it cfengine-demo-cfengine-host-1 bash -c "/usr/local/sbin/cf-agent --self-diagnostics"
```
```output
...
[ YES ] Check that agent is bootstrapped: 192.168.16.2
[ NO  ] Check if agent is acting as a policy server: Not acting as a policy server
[ YES ] Check private key: OK at '/var/cfengine/ppkeys/localhost.priv'
[ YES ] Check public key: OK at '/var/cfengine/ppkeys/localhost.pub'
...
```

Stop services and cleanup

```command
docker compose -f compose.yaml down
```

## Glossary
- [Hub](https://docs.cfengine.com/docs/3.24/overview-glossary.html#hub)
- [Host](https://docs.cfengine.com/docs/3.24/overview-glossary.html#host)
- [Client](https://docs.cfengine.com/docs/3.24/overview-glossary.html#client)
- [CFEngine role](https://docs.cfengine.com/docs/3.24/overview-glossary.html#cfengine-role)
- [Policy](https://docs.cfengine.com/docs/3.24/overview-glossary.html#policy)
- [Promise](https://docs.cfengine.com/docs/3.24/overview-glossary.html#promise)
- [Server](https://docs.cfengine.com/docs/3.24/overview-glossary.html#server)
- [Policy server](https://docs.cfengine.com/docs/3.24/overview-glossary.html#policy-server)

## References
- [Dockerfile](https://docs.docker.com/reference/dockerfile/)
- [Docker compose file](https://docs.docker.com/reference/compose-file/)
- [RedHat Universal Base Image (UBI)](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image)
- [Using the UBI init images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/building_running_and_managing_containers/index#using-the-ubi-init-images_assembly_adding-software-to-a-ubi-container)
- [ubi9-init repository](https://catalog.redhat.com/software/containers/ubi9-init/6183297540a2d8e95c82e8bd)
