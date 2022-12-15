#install and configure an Nginx server using Puppet manifest
package { 'nginx':
ensure => installed,
}

file { '/var/www/html/index.html':
content => 'Hello World!',
}

file { '/etc/nginx/html/index.html':
content => 'Hello World!',
}

file { '/usr/share/nginx/html/index.html':
content => 'Hello World!',
}

file_line { 'Add redirection, 301':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
after  => 'listen 80 default_server', 
line   => 'rewrite ^/redirect_me http://www.staggeringbeauty.com/ permanent;',
}

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
