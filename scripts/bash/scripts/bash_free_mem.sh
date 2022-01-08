#!/bin/bash

used=$(free | sed '1d; $d' | tr -s ' ' | cut -d' ' -f3)
avail=$(free | sed '1d; $d' | tr -s ' ' | cut -d' ' -f2)

echo "Used mem (bytes): $used"
echo "Avail mem (bytes): $avail"
