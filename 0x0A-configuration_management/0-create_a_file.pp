# create a file in a folder with some requirements

file {'/tmp/school'
    ensure => 'file',
    owner => 'www-data',
    group => 'www-data',
    mode => '0744',
    content => 'I love Puppet',
}
