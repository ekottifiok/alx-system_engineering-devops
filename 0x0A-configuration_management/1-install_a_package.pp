# install flask from pip3.

exec {'pip3 install flask==2.1.0':
    command => 'pip3 install flask==2.1.0'
    onlyif => 'pip3 show flask'
}
