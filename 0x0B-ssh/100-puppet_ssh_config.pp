# connect to a server without typing a password.

exec {'/usr/bin/echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config':}

exec {'/usr/bin/echo "    ChallengeResponseAuthentication no" >> /etc/ssh/ssh_config':}

exec {'/usr/bin/echo "    UsePAM no" >> /etc/ssh/ssh_config':}

file {'~/.ssh/config':
  ensure    => 'present',
  mode      => '0664'
  content   => '57022-web-01
    HostName 	100.25.45.223
    User ubuntu
    IdentityFile ~/.ssh/school
    IdentitiesOnly yes'
}
