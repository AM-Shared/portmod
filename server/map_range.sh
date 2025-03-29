#!/bin/bash

public_ip=$1
internal_port=$2
external_port=$3

iptables -t nat -A OUTPUT -p tcp -d $public_ip \
    --dport $internal_port -j DNAT \
    --to-destination $public_ip:$external_port
