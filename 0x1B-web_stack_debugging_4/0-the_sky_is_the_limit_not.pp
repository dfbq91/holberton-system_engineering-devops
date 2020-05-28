# Increase ULIMIT for nginx

exec { 'Increase Ulimit for nginx':
     command => 'sed -i "s/15/2000/g" /etc/default/nginx',
     path    => '/bin/',
}

exec { 'restart nginx':
     command => 'service nginx restart',
     path    => ['/usr/bin']