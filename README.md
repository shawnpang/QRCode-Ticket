# QRCode-Ticket项目介绍
This repository is built with python to enable anyone to use QR code as a way to send out and check in tickets

## Team Members | 团队成员 

## User Manual | 使用使用
通过启动`app.py`进行运作。

## Code Structure | 代码架构
```
├── app.py
├── config.py
├── qrcode_reader.py
├── requirements.txt
├── ticket_checker.py
└── ticket_generator.py

```

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
