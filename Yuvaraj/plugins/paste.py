import requests 
import config, os
import datetime

from Yuvaraj import yuvaraj, MODULE
from pyrogram import filters



__mod_name__ = "PASTE"  
    
__help__ = """  
- paste: paste txt to nekobin
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
