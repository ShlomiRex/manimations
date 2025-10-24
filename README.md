# Manimations — Manim animations for MSc summary presentation

This repository contains Manim Community animations used for a Master's thesis summary presentation. The animations are intended to be exported as video files (MP4) and embedded into PowerPoint slides.

Files of interest

- `kl_divergence_animation.py` — Example scene that visualizes the KL divergence between two Gaussian distributions. This is the main scene you edited.
- `main.py` — (if present) helper runner or collection of scenes.
- `pyproject.toml` — project configuration (Manim may read config here).
- `media/` — output directory where Manim writes rendered videos, images, and partial movie files.

Prerequisites

- Windows 10/11 (PowerShell). You are using a virtual environment located at `./.venv`.
- Python (the virtual environment already contains Manim Community). Activate the venv before running Manim.
- Manim Community (example in this repo: v0.19.0).
- ffmpeg (highly recommended) for audio/video muxing and to silence pydub warnings. Add `ffmpeg.exe` to your PATH or set `FFMPEG_BINARY` in Python.

Quick setup (PowerShell)

1. Activate the project's virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

2. (Optional) Install/update dependencies inside the venv (if you need to):

```powershell
# Example, only if you have requirements or want to ensure manim is installed
pip install -U manim
```

Rendering videos

General pattern (PowerShell):

```powershell
# activate venv then run manim
.\.venv\Scripts\Activate.ps1; manim <options> <python_file> <SceneClass>
```

Preview / fast low-quality (use while editing):

```powershell
.\.venv\Scripts\Activate.ps1; manim -pql kl_divergence_animation.py KLDivergence
```

Common quality presets (Manim Community):
- `-pql` : preview, low quality (fast; typically 480p, 15 fps)
- `-pqm` : preview, medium quality (typically 720p, 30 fps)
- `-pqh` : preview, high quality (typically 1080p, 30 fps)

Specify exact resolution (pixel-perfect)

```powershell
# 1080p (1920x1080)
.\.venv\Scripts\Activate.ps1; manim -p -r 1920,1080 kl_divergence_animation.py KLDivergence

# 4K (3840x2160)
.\.venv\Scripts\Activate.ps1; manim -p -r 3840,2160 kl_divergence_animation.py KLDivergence
```

Frame rate (FPS)

Some Manim versions accept `--frame_rate` or `--fps`. If `--frame_rate` isn't recognized, try `--fps` or check `manim --help`.

```powershell
# 60 fps at 1080p
.\.venv\Scripts\Activate.ps1; manim -p -r 1920,1080 --frame_rate 60 kl_divergence_animation.py KLDivergence
```

Output location

Rendered videos are placed under `media/videos/<module_name>/<resolution>/`. Example:

```
media/videos/kl_divergence_animation/1080p30/KLDivergence.mp4
```

Tips and considerations

- Higher resolution dramatically increases render time and file size. Start with `-pql` while iterating, then render the final video at 1080p or 4K.
- If you see this warning from `pydub`:

```
RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
```

install ffmpeg and add it to your PATH. Two quick ways:

- Chocolatey (elevated PowerShell):

```powershell
choco install ffmpeg -y
```

- Download a static build from https://ffmpeg.org/ or https://www.gyan.dev/ffmpeg/builds/ and add the folder containing `ffmpeg.exe` to your user PATH.

Alternatively, point pydub/Manim directly to the ffmpeg binary in Python before importing pydub:

```python
import os
os.environ['FFMPEG_BINARY'] = r'C:\ffmpeg\bin\ffmpeg.exe'
# or for pydub specifically:
from pydub import AudioSegment
AudioSegment.converter = r'C:\ffmpeg\bin\ffmpeg.exe'
```

Embedding into PowerPoint

- Use MP4 files exported by Manim.
- Prefer 1080p for presentations (good balance between quality and size). 4K is overkill for most projectors and can cause playback issues.
- If you need a transparent background (to place animations over slides), Manim supports rendering with transparent background depending on the renderer; you may need to export as an image sequence or use special settings — check Manim docs for your version.

Advanced: pyproject.toml config

You can put common settings in `pyproject.toml`/Manim config to avoid passing `-r`/`--frame_rate` every time. See Manim docs for configuration options for your installed version.

Troubleshooting

- If Manim raises `TypeError: Mobject.__init__() got an unexpected keyword argument 'height'`, replace unsupported kwargs (e.g. `height`) with the appropriate API parameter (e.g. `y_length`) for your Manim version. This repository's `kl_divergence_animation.py` already uses `y_length`.
- If `manim --help` shows slightly different flags (`--fps` vs `--frame_rate`), use the one your installed version expects.

If you want me to:
- Render a 1080p or 4K video for you from the venv now, tell me the target resolution and fps and I will run it (note: long render times). 
- Add a small script to automate rendering all scenes into a specified resolution.

Enjoy building your presentation animations — tell me if you want a script that renders all scenes to 1080p and places output in a `final/` folder ready for embedding in PowerPoint.
