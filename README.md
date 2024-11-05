# Gym Video Cutter

When I train and record a video I don't want to spend endless hours to cut idles times before exercise preparation and after its done.

With this first implementation I can start recording the video and I send verbal input:

- `start`: will mark the start of the exercise
- `stop`: will mark the end of the exercise

The script will cut everything except the interval from [start, stop]. It will also encode the video.


## Getting started


```bash
pip install -U openai-whisper
```

To enable amd gpu encoding:

https://medium.com/@anvesh.jhuboo/rocm-pytorch-on-fedora-51224563e5be

## Usage

```bash
python3 ./main.py -i video.mp4
```
