#! /usr/bin/env python3
import ftplib

from server_cli_setup import setup_cli
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

args = setup_cli()
# set up authorizer and handler
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", "./data", perm="elradfmwMT")
handler = FTPHandler
handler.authorizer = authorizer

# set up server
server = FTPServer(("0.0.0.0", args.port), handler)

# start the server
server.serve_forever()
