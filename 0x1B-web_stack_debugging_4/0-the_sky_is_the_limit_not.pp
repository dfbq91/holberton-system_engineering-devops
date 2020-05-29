# Increase ULIMIT for nginx

exec { 'Increase_Ulimit':
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
  provider => shell,
}

exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => shell,
  require  => Exec['Increase_Ulimit'],
}