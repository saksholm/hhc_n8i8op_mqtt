#!/usr/bin/python3
import shutil
shutil.copy2('./default_config.yaml', './config.yaml')
print("Copied 'default_config.yaml' to 'config.yaml'");
shutil.copy2('./default_inventory.yaml', './inventory.yaml')
print("Copied 'default_inventory.yaml' to 'inventory.yaml'");
