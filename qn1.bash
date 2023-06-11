#!/bin/bash

mkdir ../Modified
find . -name '*.txt' -type f | xargs -I % sh -c 'cp % ../Modified'

