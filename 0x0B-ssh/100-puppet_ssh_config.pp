# connect to a server without typing a password.

file {'~/.ssh/config':
  ensure    => 'present',
  mode      => '0664'
  content   => '57022-web-01
    HostName 	3.85.175.19
    User ubuntu
    IdentityFile ~/.ssh/school
    IdentitiesOnly yes'
}
