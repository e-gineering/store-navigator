#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here


app = App()
stack = MyStack(app, "temp")
CloudBackend(stack,
  hostname='app.terraform.io',
  organization='e-gineering',
  workspaces=NamedCloudWorkspace('store-navigator')
)

app.synth()
