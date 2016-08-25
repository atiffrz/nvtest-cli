#!/bin/bash
# This file is main daemon file called by daemon extract_to_database.sh in /etc/init.d
# Author : Pratik Sawale <psawale@nvidia.com>

while [ true ];
do
path1="/mnt/local/people-local/pratiks/softwares/NVTEST/"
file="/mnt/local/people-local/pratiks/softwares/NVTEST/filechange"
if [ -f "$file" ]; then
  echo "File is chnaged"
  python extract_data_from_csv_to_database.py
  rm -rf $file
  sleep 1s
fi
done
