# imgda-uploader

Upload a DocumentArray from all PNG/JPG images in certain folder, and return the token.   

## Python CLI

Upload every png/jpg in `/Users/hanxiao/Documents/docarray` to cloud:

```bash
pip install -r requirements.txt

python app.py /Users/hanxiao/Documents/docarray
```

```text
Your token will be: DPGae9lTCUg
Preprocessing ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Serializing ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
🎉 Success! Here is how you can use it:
  1
  2 from docarray import DocumentArray
  3
  4 da = DocumentArray.pull('DPGae9lTCUg')
  5
```

### Full args

```text
usage: app.py [-h] [--shape N] [--normalize] [--channel-first]
              [--glob-pattern GLOB_PATTERN [GLOB_PATTERN ...]] [--token TOKEN]
              folder

Image Uploader

positional arguments:
  folder                all images from that folder will be uploaded

optional arguments:
  -h, --help            show this help message and exit
  --shape N             reshape all images to N x N
  --normalize           normalize the image in preprocessing
  --channel-first       bring channel axis from last to first
  --glob-pattern GLOB_PATTERN [GLOB_PATTERN ...]
                        the pattern for image files
  --token TOKEN         token for later DocumentArray access, when not given
                        will auto generate a 8-length one
```

## Docker CLI

A prebuilt version is available at `jinaai/imgup`.

### Run
```bash
docker run -v /Users/hanxiao/Documents/docarray:/j jinaai/imgup /j
```

Caveats with Docker:
- Docker volume can be slow
- Rich console does not rendered correctly in Docker container.

