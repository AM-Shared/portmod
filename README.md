# portmod

Expose internal port ranges on Vast boxes to the same range on calling host via local iptables mapping

The following MUST be added to the sudoers file for the user running the server script:

```
<user> ALL=(ALL) NOPASSWD: /bin/bash /full/path/to/add_mapping.sh
```
