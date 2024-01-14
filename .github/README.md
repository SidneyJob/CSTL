# Client-Side Testing Lab

Self-hosted app to testing your Client-Side PoCs.

## Authors
- [SidneyJob](https://t.me/SidneyJobChannel)
- [tokiakasu](https://t.me/hackthishit)

## Setup:
```bash
git clone https://github.com/SidneyJob/CSTL.git
cd CSTL
sudo docker build . -t cstl
sudo docker run -d --name cstl -p 8081:8081 --restart always cstl
```

## Uninstall:
```bash
sudo docker stop cstl # stop container
sudo docker rm cstl # delete container
sudo docker rmi cstl # delete image
```