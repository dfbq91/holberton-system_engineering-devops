# Increase ULIMIT for nginx

exec { 'Increase_Ulimit':
     command => 'sed -i "s/15/2000/g" /etc/default/nginx',
     path    => ['/bin/'],
}

exec { 'restart_nginx':
     command => 'service nginx restart',
     path    => ['/usr/bin'],
     require => Exec['ulimit'],
}