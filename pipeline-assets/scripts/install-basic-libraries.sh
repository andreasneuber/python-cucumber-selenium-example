#!/usr/bin/env bash
  
pip install -r requirements.txt
apt-get update
apt-get install -y default-jre
apt-get install -y zip
apt-get install -y wget
apt-get install -y ca-certificates
apt-get install -y libnss3-dev libasound2 libxss1 libappindicator3-1 gconf-service
apt-get install -y libgconf-2-4 libpango1.0-0 xdg-utils fonts-liberation libgbm1 libu2f-udev