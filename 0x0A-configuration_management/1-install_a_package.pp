#!/usr/bin/pup
# install_flask.pp

package { 'puppet-lint':
  ensure   => '2.1.0',
  provider => 'gem',
}
