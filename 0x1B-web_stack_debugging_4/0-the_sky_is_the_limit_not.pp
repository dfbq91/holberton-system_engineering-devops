# Increase ULIMIT for nginx

exec { 'Increase_Ulimit':
  command => 'sed -i "s/15/2000/g" /etc/default/nginx',
  path    => 'shell',
}

exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => 'shell',
  require => Exec['Increase_Ulimit'],
}