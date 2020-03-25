#!/usr/bin/env bash
# Install Nginx web server (w/ Puppet).
# This task is not complete, just nginx is installed
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

