# create a manifest that kills a process named killmenow.

exec {'/usr/bin/pkill killmenow':}