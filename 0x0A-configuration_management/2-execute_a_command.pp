# kills a process named killmenow
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}