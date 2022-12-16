# make changes to config file using puppet
file_line {'Turn off password authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}

file_line {'Declare identity file path':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => 'IdentityFile ~/.ssh/id_rsa'
  match_for_absence => true,
}
