# QRCode-Ticket项目介绍
This repository is built with python to enable anyone to use QR code as a way to send out and check in tickets
该产品仅为一个最基本的模型，还需要大量的完善工作。但是当前可以在单机上进行二维码门票的生成和使用。


## Dependencies | 外部依赖
* python3
* virtualenv
* brew

## Installation | 安装
可以通过以下脚本进行安装
```
virtualenv -p python3 runtime
source runtime/bin/activate
cd src
brew install zbar
pip install -r requirements.txt
```
