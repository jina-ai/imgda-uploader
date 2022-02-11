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


## Docker CLI

### Build
```bash
docker build --platform linux/amd64 . -t imgup
```

### Run
```bash
docker run -v /Users/hanxiao/Documents/docarray:/img --platform linux/amd64 imgup /img
```

Caveats with Docker:
- Docker volume can be slow
- Rich console does not rendered correctly in Docker container.

