[![Build Status](https://travis-ci.org/funkwerk/compose_diff.svg)](https://travis-ci.org/funkwerk/compose_diff)
[![](https://badge.imagelayers.io/funkwerk/compose_diff.svg)](https://imagelayers.io/?images=funkwerk/compose_diff:latest 'funkwerk/compose_diff')
[![PyPi downloads](https://img.shields.io/pypi/dm/compose_diff.svg)](https://pypi.python.org/pypi/compose_diff/)
[![PyPi version](https://img.shields.io/pypi/v/compose_diff.svg)](https://pypi.python.org/pypi/compose_diff/)
[![Docker pulls](https://img.shields.io/docker/pulls/funkwerk/compose_diff.svg)](https://hub.docker.com/r/funkwerk/compose_diff/)
# compose_diff

Diff docker-compose files.

## Usage

### Via Python

Install it via:
`pip3 install compose_diff`

After that use it like

`compose_diff --images old.yml new.yml`
this will print the the differences in the used images between the two versions.

## Features
 - Support for Version 2 and Version 1.
 - Diffs Images
