#json_operators.py 
import json
from datetime import date

def write_json(data, filename): 
  with open(filename,'w') as f: 
    json.dump(data, f, indent=2)

def read_json(filename):
  with open(filename,'r') as f:
    return json.load(f)