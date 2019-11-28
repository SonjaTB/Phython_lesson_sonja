#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:58:09 2019

@author: sonja
"""

authors = ["Darwin", "Lovelace", "Hawkin", "Noether"]

output_fh = open("list.html", "w")

scaffold_start = """<!DOCTYPE html>
<html>
<head>
<title>Titel dieser wunderbaren Seite</title>
</head>
<body>

<h1>Eine grandiose und geniale Überschrift</h1>

<p>Ein nicht weniger toller Abschnitt.</p>

<li></li>


<ul>
"""

output_fh.write(scaffold_start)

scaffold_middle = ""
for author in authors:
    scaffold_middle = scaffold_middle + "<li>" + author + "</li>\n"
    #print(scaffold_middle)
    #print("------------------")
    
output_fh.write(scaffold_middle)

scaffold_end = """
</ul>

</body>

</html>""" 
output_fh.write(scaffold_end)

output_fh.close()

output_fh = open("list.html", "w")
output_fh.write(scaffold)
output_fh.close()