#!/bin/bash

grep $@ /var/log/nginx/access.log | tail -n 1 |cut -d"\"" -f6
