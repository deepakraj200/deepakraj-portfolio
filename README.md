# R. Deepakraj — Cinematic Portfolio

A black-and-red cinematic portfolio. Plain HTML, CSS and JavaScript (WebGL + canvas). **No build step, no frameworks.**

## Run locally
```bash
python -m http.server 5173
# open http://localhost:5173
```
(Opening index.html directly may block the video — use a local server.)

## Edit your content
Open `index.html` and find the `ME` object near the top of the script. Name, e-mail, skills, projects, timeline cards and tool list all live there.

## Files
```
index.html        page, styles and scripts
assets/man.mp4    walking-man video: colour on the left half, alpha matte on the right half
assets/fig.png    front-facing cut-out (time-machine silhouette)
assets/fig2.webp  back-view cut-out (tech universe)
assets/ferrari.jpg footer photo
assets/icons.js   AWS service icons + brand logos (embedded SVG)
tools/matte.py    removes a white backdrop from a video (offline helper)
```

## Deploy
Any static host works. On Vercel: import the repo, Framework Preset = **Other**, leave Build Command and Output Directory empty, Deploy.
