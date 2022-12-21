#install and configure an Nginx server using Puppet manifest
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure => installed,
  require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\n\trewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec {'HTTP header':
	command => 'sed -i "25i\n\tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
