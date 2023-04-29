# FTP Server and Client

## Introduction

This project contains an FTP server and client implementation in Python. The FTP server can be used to transfer files between a client and a server over the FTP protocol.

## Prerequisites

Before you can use the FTP server and client, you must have the following software installed on your system:

- Python 3.10 or later
- `pip` package installer for Python

## Installation

1. Navigate to the project root directory

2. Create a Python virtual environment for the project:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

5. Install the required packages using `pip` and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

### FTP Server

To start the FTP server, run the following command:

```bash
cd server
./server.py
```

This will start the FTP server on the default port `21`.

You can also specify a custom port using the `-p` or `--port` flag:

```bash
./server.py --port 2121
```

This will start the FTP server on port `2121`.

### FTP Client

To use the FTP client, run the following command:

```bash
#make sure you are in the client directory
cd client
./client
```

This will start the FTP server on the default port `21` and a default domain of `0.0.0.0`.

You can also specify a custom port using the `-p` or `--port` flag
You can also specify a custom domain using the `-d` or `--domain` flag

This will start the FTP client in interactive mode. You can then enter FTP commands to connect to a remote server and transfer files.

## Commands

| Command | Description                                        | Usage          |
| ------- | -------------------------------------------------- | -------------- |
| GET     | Downloads file from server given file name         | GET [filename] |
| PUT     | Uploads file from client to server given file name | PUT [filename] |
| LS      | Lists all files in directory                       | LS             |
| QUIT    | Disconnects from server and ends program           | QUIT           |

## Conclusion

This project provides a simple implementation of an FTP server and client in Python. By following the installation and usage instructions in this README, you should be able to set up and use the FTP server and client on your system.
