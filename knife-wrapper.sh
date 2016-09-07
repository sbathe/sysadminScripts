#!/bin/bash
ENV=$1; shift
case $ENV in
  dev)
    cf="/home/sbathe/.chef-dev/knife.rb"
    ;;
  stage)
    cf="/home/sbathe/.chef-stage/knife.rb"
    ;;
  pune)
    cf="/home/sbathe/.chef-pune/knife.rb"
    ;;
    *)
    echo "env can be DEV or STAGE only"
    ;;
esac
knife "$@" -c $cf
