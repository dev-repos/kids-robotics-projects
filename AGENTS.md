# Agents

The full process for new robotics projects (design, geometry check, true-size templates, build card, one-by-one assembly pages, full PDF, images, README/index, verification, git) lives in **siddick/vercel-sandbox → `.claude/agents/robotics-pdf.md`** (source of truth).

In this repo:
- `spec/project.schema.json` – machine-readable project spec format
- `projects/13-wheelbarrow-walker/spec.json` – worked example
- `tools/new_project.py NN slug "Title"` – scaffold a project folder + spec stub
- Commit with `git -c user.name=Siddick -c user.email=siddick@gmail.com commit`; never change global config; push `gh-pages`.
