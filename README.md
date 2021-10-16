# mo436

to build docker image using dockerfile

```bash
docker build -f Dockerfile -t data_science_container:latest .
```

In order to run 

```bash
docker run -it -p 8888:8888 \
    -p 8889:8889 \
    -p 6006:6006 \
    -d \
    -v $(pwd)/notebooks:/notebooks \
    data_science_container
```