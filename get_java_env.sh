#!/bin/bash
pid="$(ps -ax -o pid,command | grep [o]rg.apache.hadoop.hbase.master.HMaster | awk '{print $1}')"
pr="$(ps -ax -o pid,command | grep [o]rg.apache.hadoop.hbase.master.HMaster)"
echo -e "found hbase process:\n\t$pr\n\n"
echo -e "HBase environment:"
strings -1 /proc/$pid/environ
echo -e "\n\n\n"
echo -e "hbase args are:"
ps -ax -o pid,command | grep [o]rg.apache.hadoop.hbase.master.HMaster | awk '{$1=""; print $0}' | tr ' ' "\n"
