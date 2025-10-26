#!/usr/bin/env python
# coding: utf-8

import os
import sys

roam_graph = os.environ.get("ROAM_GRAPH")
print("ROAM_GRAPH value:", roam_graph)

if ',' in roam_graph:
    graph_array = roam_graph.split(',')
else:
    graph_array = roam_graph.splitlines()

for v in graph_array:
    v = v.strip()
    print("Current value of v is:", v)
    os.makedirs(f"./markdown/{v}/images", exist_ok=True)
    os.system(f"python scripts/roam_image_backup.py json/{v}.json ./markdown/{v}/images")
    os.system(fr"sed -i 's/- #/\n#/g;s/](</](/g;s/.md>)/.md)/g;s/- \([[:digit:]]*\)\./\n\1\./g;s~(https.*%2F\(.*\)\?alt=media.*)~(./images\/\1)~g' ./markdown/{v}/*.md")
