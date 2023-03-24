#!/usr/bin/env bash
  
curl -o allure-2.21.0.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.21.0/allure-commandline-2.21.0.tgz
tar -zxvf allure-2.21.0.tgz -C /opt/
ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure