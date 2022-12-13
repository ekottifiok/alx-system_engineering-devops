# connect to a server without typing a password.

exec {'/usr/bin/echo "    PasswordAuthentication no" >> /etc/ssh/sshd_config':}

exec {'/usr/bin/echo "    ChallengeResponseAuthentication no" >> /etc/ssh/sshd_config':}

exec {'/usr/bin/echo "    UsePAM no" >> /etc/ssh/sshd_config':}
