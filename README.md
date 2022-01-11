# Convert Video to Images

The tool is to convert the videos to images in the folder.

## How to use it ?

```bash
git clone https://github.com/willy541222/Convert-Video-to-Images.git
```

```bash
cd Convert-Video-to-Images
```

Type command below and change the path.
The `-p` param is requirement.

```bash
python video_to_images.py -p {Path/to/the/video/folder}
```

Other parameters are optional.

| Params | Description| Default|
|------|------|-----|
| - i | The initial index of saving image name.|0|
| - s | Interval of saving frames.|30|
| - o | The file path to save images.|./|
