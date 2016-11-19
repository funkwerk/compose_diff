[![Build Status](https://travis-ci.org/funkwerk/compose_diff.svg)](https://travis-ci.org/funkwerk/compose_diff)
[![Docker Build](https://img.shields.io/docker/automated/funkwerk/compose_diff.svg)](https://hub.docker.com/r/funkwerk/compose_diff/)
[![PyPi downloads](https://img.shields.io/pypi/dm/compose_diff.svg)](https://pypi.python.org/pypi/compose_diff/)
[![PyPi version](https://img.shields.io/pypi/v/compose_diff.svg)](https://pypi.python.org/pypi/compose_diff/)
[![Docker pulls](https://img.shields.io/docker/pulls/funkwerk/compose_diff.svg)](https://hub.docker.com/r/funkwerk/compose_diff/)
# compose_diff

Diff docker-compose files.
When deploying using docker-compose, these files could be used to generate Release Notes.
Especially interesting is to diff two docker-compose Releases by each other, then customers know the changed components and testers know which part to especially test.

## Usage

### Via Python

Install it via:
`pip3 install compose_diff`

After that use it like

`compose_diff --versions old.yml new.yml`
this will print the differences in the used versions/tags between the two compose files.

`compose_diff --instances old.yml new.yml`
this will print the amount of instances of this image between the two compose files.

## Features

 - Support for Version 2 and Version 1.
 - Diffs Image Versions
 - Diffs Image Instances
 - Output in Markdown and CSV format
