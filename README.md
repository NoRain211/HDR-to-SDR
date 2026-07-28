# HDR to SDR Converter

![Tests](https://github.com/NoRain211/HDR-to-SDR/actions/workflows/python-tests.yml/badge.svg)
![Coverage floor](https://img.shields.io/badge/coverage-90%25%20floor-brightgreen)
![License](https://img.shields.io/github/license/NoRain211/HDR-to-SDR)

This is a desktop GUI application to convert HDR videos to SDR using FFmpeg. The application lets you select an input video (or drag and drop one), live-preview the tonemapped result frame by frame, fine-tune the conversion, and convert single files or a whole queue while monitoring progress.

## Feature Access

This fork starts with every feature enabled. It has no paid feature tier.

You do not need to buy, enter, or activate a product key. The app does not contact a license server at startup.

## Under the Hood

- **GPU/CPU dual pipeline**: tonemapping runs on the GPU via libplacebo (Vulkan) when available, falling back to a pure-CPU ffmpeg filter chain — GPU tonemapping roughly halves conversion time on capable hardware.
- **Real color science**: gamut conversion runs through a generated BT.2020→BT.709 3D LUT (tetrahedral interpolation) instead of approximate gamma math, on both the CPU and GPU paths.
- **Dolby Vision (profile 5) RPU handling** and automatic hardware encoder detection (NVENC / AMF / QSV) with CPU fallback.
- **Tested and typed**: 13 test modules run against Python 3.10–3.13 (headless, via Xvfb, to exercise the real Tkinter GUI) on every push, gated by a 90% coverage floor and a zero-error `pyright` pass on `src/`.
- **Signed, installable releases**: PyInstaller build + Inno Setup installer, code-signed via Azure Trusted Signing, with an in-app auto-updater.

## Features

- **Select Input Video Files**: Browse for video files (`.mp4`, `.mkv`, `.mov`, `.avi`, `.webm`, `.m4v`), or use the "All files" filter for anything else FFmpeg can read.
- **Drag and Drop**: Drop one or more files to load and preview them.
- **Live Frame Preview**: See the original (HDR) frame next to the converted (SDR) result side by side. Five evenly-spaced frame buttons let you scrub through the video, and the previews scale smoothly as you resize the window.
- **Adjust Gamma Value**: Drag a slider (or type a value) to fine-tune the gamma of the output; the preview updates instantly.
- **Conversion Methods**: Choose between a **Static** or **Dynamic** method. Static applies the same conversion regardless of the file; Dynamic analyzes the original's brightness (MAXFALL) for a more faithful result.
- **Tonemappers**: Pick between Reinhard, Mobius, Hable, BT.2390, and Spline. BT.2390 and Spline are GPU-only (libplacebo) and shown greyed out until GPU tonemapping is active.
- **Video Info Strip**: After a file loads, a one-line summary shows resolution, frame rate, codec, HDR/SDR, audio codec, and the probed source bitrate (estimated from the container total when a source, e.g. MKV, doesn't expose a per-stream bitrate). Dolby Vision sources are detected automatically and flagged in this strip.
- **Monitor & Cancel**: A progress bar tracks the active conversion, and a Cancel button stops it cleanly.
- **Open Output File**: Optionally open the output automatically when the conversion completes.
- **Dark Theme**: A flat, color-based dark UI that stays smooth during window resizing.
- **GPU Acceleration**: Runs HDR→SDR tonemapping on the GPU via libplacebo (Vulkan) and encodes with the detected hardware encoder (`h264_nvenc` / `h264_amf` / `h264_qsv`). Because tonemapping (not encoding) is the real bottleneck, moving it to the GPU can roughly halve conversion time on capable hardware. Falls back automatically to CPU tonemapping when Vulkan/libplacebo isn't available, and to CPU encoding if the GPU encoder fails.
- **H.265/HEVC Preservation**: An HEVC source is re-encoded back to HEVC instead of being converted to H.264.
- **10-Bit Output**: Encode the SDR output at 10-bit color depth to avoid banding on gradients.
- **Dolby Vision Support**: Dolby Vision (profile 5) RPU metadata is routed through the libplacebo tonemapper for an accurate conversion. The source audio track is preserved when the output container supports it.
- **Persistent Settings**: Gamma, conversion method, tonemapper, quality, container, GPU toggle, preview toggle, and "open after conversion" are saved between sessions.
- **Quality Control**: A Quality Mode dropdown switches between **Constant Quality** (a CRF 17–28 on CPU / CQ 15–30 on GPU slider that lets the encoder auto-vary bitrate per scene) and **Target Bitrate** (you set the average output bitrate directly, up to the source's own bitrate).
- **Output Container**: Explicitly choose the output container (MP4 / MKV / MOV); it defaults to match the input. Audio and subtitles are stream-copied when the container allows, and transcoded or dropped only when it can't hold them (e.g. TrueHD audio or PGS subtitles into MP4).
- **Custom Frame Seek**: Jump the preview to any exact timestamp (`HH:MM:SS`, `MM:SS`, or plain seconds) in addition to the five frame buttons.
- **Batch Conversion Queue**: Add multiple files (via "Add Files" or by dropping several at once) and convert them sequentially. The queue shows a per-file status (pending / converting / done / failed), lets you click an entry to preview it, remove or clear entries, and reports a summary when it finishes. Each item remembers its own settings (quality mode, quality/bitrate value, bit depth) and restores them when you reselect it, and the list marks any item whose settings you've customized away from the shared defaults.
- **Apply to All**: Copy the currently displayed settings onto every item in the batch queue in one click.
- **12-Bit Output**: Encode the SDR output at 12-bit color depth (CPU only) for the widest gradient headroom.

## Requirements

- Python 3.10 or newer (tested on 3.10–3.13)
- FFmpeg (`ffmpeg` and `ffprobe` on your PATH, or bundled alongside the app)
- GPU acceleration is optional. GPU tonemapping needs an ffmpeg build with libplacebo (Vulkan); GPU encoding is supported on NVIDIA (`h264_nvenc`), AMD (`h264_amf`), and Intel (`h264_qsv`) hardware. The app degrades gracefully to CPU when either is unavailable.

## Installation

1. Install Python 3.10 or newer and FFmpeg.
2. Clone this repository and create a virtual environment: `python -m venv .venv`.
3. Install the application dependencies: `.venv\Scripts\python -m pip install -r requirements.txt`.
4. Start the application: `.venv\Scripts\python src\main.pyw`.

## Software License

The MIT License applies to this source code. This legal license does not limit access to app features. See [LICENSE](LICENSE) for the full terms.
