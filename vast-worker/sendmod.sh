#!/bin/bash

json_output="{\"public_ip\": \"$(curl ipinfo.io/ip)\", \"ip_map\": {"

append_range_to_body() {
    start=$1
    end=$2
    for (( internal_port=start; internal_port<=end; internal_port++ ))
    do
        var_name="VAST_TCP_PORT_$internal_port"
        exposed_port="${!var_name}"
        json_output+="\"$internal_port\": \"$exposed_port\","
    done
}

append_range_to_body 40000 41024
append_range_to_body 50000 51024

# remove trailing comma & close
json_output="${json_output%,}}}"

echo $json_output
# curl -X POST $1

