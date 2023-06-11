#!/bin/bash

## Generate random password of given length
function genpass() {
  tr -dc A-Za-z0-9_ < /dev/urandom | head -c ${1:-32}
}

## Different way to generate random  password of given lenght using $RANDOM
function genpass2()
{
  openssl rand -hex 4100 | cut -c1-$1
}

