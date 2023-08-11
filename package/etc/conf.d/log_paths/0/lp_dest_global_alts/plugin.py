#! /usr/bin/env python3
import os
import jinja2
import pprint

pp = pprint.PrettyPrinter(indent=4)

plugin_path = os.path.dirname(os.path.abspath(__file__))

templateLoader = jinja2.FileSystemLoader(searchpath=plugin_path)
templateEnv = jinja2.Environment(loader=templateLoader)
tm = templateEnv.get_template("plugin.jinja")


global_alt = os.getenv(f"SC4S_DEST_GLOBAL_ALTERNATES", "")
if global_alt != "":
    dest_key_dests = global_alt.split(",")
    msg = tm.render(destination=dest_key_dests)
    print(msg)    
else:
    pass
