# Build context is the directory with all the repos (documentation, core, nova, enterprise, masterfiles, nt-docs)

# Pre-processing
FROM ubuntu:22.04 AS tools

# We need sudo before all
RUN apt-get -qy update && \
    apt-get -qy install sudo

# Add jenkins user
RUN useradd -s /bin/bash jenkins
RUN echo "jenkins    ALL=(ALL)       NOPASSWD: ALL">> /etc/sudoers
RUN mkdir -p /home/jenkins /nt
RUN chown -R jenkins:jenkins /home/jenkins /nt

# Run rest of setup as jenkins user
COPY documentation/generator/build/install.sh /
USER jenkins
WORKDIR /home/jenkins
RUN sudo apt-get update -qy && bash -x /install.sh

WORKDIR /nt
COPY --chown=jenkins:jenkins . /nt

ARG BRANCH
ARG PACKAGE_JOB
ARG PACKAGE_UPLOAD_DIRECTORY
ARG PACKAGE_BUILD
ARG LTS_VERSION
RUN bash -x documentation/generator/build/main.sh "$BRANCH" "$PACKAGE_JOB" "$PACKAGE_UPLOAD_DIRECTORY" "$PACKAGE_BUILD" "$LTS_VERSION"

# Hugo build
FROM ghcr.io/gohugoio/hugo:v0.169.0@sha256:a146e0639230bbc73358e6563240f0a6103466f0390b80a457c775068ec802a9 AS hugo
COPY --from=tools --chown=hugo:hugo /nt/documentation /nt/documentation
WORKDIR /nt/documentation/hugo
RUN npm ci && npm run build:all

# Post-processing and packing into /nt/output
FROM tools AS postprocess
COPY --from=hugo --chown=jenkins:jenkins /nt/documentation /nt/documentation
ARG BRANCH
RUN bash -x documentation/generator/_scripts/_postprocess.sh "$BRANCH" && \
    bash -x documentation/generator/_scripts/_publish.sh "$BRANCH"

# Just the tarballs, exported with --output type=local
FROM scratch AS output
COPY --from=postprocess /nt/output /
