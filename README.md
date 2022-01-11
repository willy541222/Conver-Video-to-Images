# Convert Video to Images

The tool is to convert the videos to images in the folder.

## How to use it ?

1. Download the repository.

```bash
git clone https://github.com/willy541222/Convert-Video-to-Images.git
```

2. Change the directory to the project folder.

```bash
cd Convert-Video-to-Images
```

3. Type command below and change the path.
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

* For example

Save the image per 20 frame and the name of image start from 1.jpg save in the C:/images/ folder.

```bash
python video_to_images.py -p {Path/to/the/video/folder} -i 1 -s 20 -o C:/images/
```