#!/bin/bash
for node in $(kubectl get nodes -o name); do
  echo "Draining $node"
  kubectl cordon $node
  kubectl drain $node --ignore-daemonsets --delete-emptydir-data
done