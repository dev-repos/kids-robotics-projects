#!/usr/bin/env python3
"""Scaffold: python3 tools/new_project.py NN slug "Title" -> projects/NN-slug/{README.md,spec.json}"""
import json,os,sys
n,slug,title=int(sys.argv[1]),sys.argv[2],sys.argv[3]; d=f"projects/{n:02d}-{slug}"; os.makedirs(d,exist_ok=True)
spec={"number":n,"slug":f"{n:02d}-{slug}","title":title,"color":"#888888","topic":"","age":"8+","time":"","materials":[],"motor":{},
"mechanism":{"name":"","params_mm":{}},"geometry":{"targets":{},"results":{},"acceptance":[]},"sheets":[],"card_steps":[],"assembly_steps":[],"outputs":{},
"video":{"playlist":"PLeEznjsWgvDM","youtube_id":None},"commit":""}
p=f"{d}/spec.json"
if not os.path.exists(p): json.dump(spec,open(p,"w"),indent=2)
r=f"{d}/README.md"
if not os.path.exists(r): open(r,"w").write(f"# #{n} {title}\n\nSee spec.json. Process: siddick/vercel-sandbox .claude/agents/robotics-pdf.md\n")
print("created",d)
