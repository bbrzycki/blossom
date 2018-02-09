"""
Load simulation parameters from world config file.
"""

import configparser
import os, glob

# Set environmental filename
env_file = glob.glob('/*.env')
if length(env_file) != 1:
	print("There are multiple environment configuration files in the current directory. "
		  "There should only be one environment configuration file. Taking one at random.")
env_file = env_file[0]

config_world = configparser.ConfigParser()
config_world.read(env_file)

# dimensionality: int
dimensionality = int(config_world['Overall Parameters']['dimensionality'])

# world_size: int, or 'inf'
world_size = config_world['Overall Parameters']['world_size']
if world_size != 'inf':
	world_size = [int(L) for L in (config_world['Overall Parameters']['world_size']).split()]
	
# environment_filename: str, or 'none'
environment_filename = config_world['Overall Parameters']['environment_filename']