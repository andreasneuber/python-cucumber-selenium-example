#!/usr/bin/env bash
  
version=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
wget -N https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
cp chromedriver /usr/local/bin
rm chromedriver_linux64.zip
rm chromedriver