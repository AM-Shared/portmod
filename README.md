# portmod

Remap internal port ranges on Vast boxes to the same range on requesting host via iptables mapping

## Server

The following MUST be added to the sudoers file for the user running the server script:

```
<user> ALL=(ALL) NOPASSWD: /bin/bash /full/path/to/add_mapping.sh
```

## Client (Worker)

Should be run on worker startup.

```
curl -fsSL https://raw.githubusercontent.com/AM-Shared/portmod/refs/heads/master/vast-worker/sendmod.sh | bash -s -- <server-url> <write-key>
```
