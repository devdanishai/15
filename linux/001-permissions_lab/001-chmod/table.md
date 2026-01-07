| Numeric | Symbolic          | Meaning (Owner / Group / Others)            |
| ------- | ----------------- | ------------------------------------------- |
| 700     | u=rwx,g=,o=       | Owner: rwx, Group: none, Others: none       |
| 755     | u=rwx,g=rx,o=rx   | Owner: rwx, Group: r-x, Others: r-x         |
| 775     | u=rwx,g=rwx,o=rx  | Owner: rwx, Group: rwx, Others: r-x         |
| 644     | u=rw,g=r,o=r      | Owner: rw-, Group: r--, Others: r--         |
| 666     | u=rw,g=rw,o=rw    | Everyone can read/write (no execute)        |
| 600     | u=rw,g=,o=        | Owner read/write, Group/others none         |
| 400     | u=r,g=,o=         | Owner read only, Group/others none          |
| 777     | u=rwx,g=rwx,o=rwx | Everyone can read/write/execute (dangerous) |



### Important codes:

- Scripts → 755

- Config/private → 600/700

- Shared code → 775

- Normal files → 644