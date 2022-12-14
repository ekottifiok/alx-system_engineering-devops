# connect to a server without typing a password.

exec {'/usr/bin/echo "    PasswordAuthentication no" >> /etc/ssh/sshd_config':}

exec {'/usr/bin/echo "    ChallengeResponseAuthentication no" >> /etc/ssh/sshd_config':}

exec {'/usr/bin/echo "    UsePAM no" >> /etc/ssh/sshd_config':}

file {'~/.ssh/config':
  ensure    => 'present',
  mode      => '0664'
  content   => '57022-web-01
    HostName 	3.85.175.19
    User ubuntu
    IdentityFile ~/.ssh/school
    IdentitiesOnly yes'
}
