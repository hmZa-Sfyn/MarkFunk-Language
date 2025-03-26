import re
from html import escape
import argparse
import os
import webbrowser
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

class MarkFunkCompiler:
    def __init__(self):
         self.patterns = [
            # Standard Markdown
            (r'^# (.*?)$', r'<h1>\1</h1>'),
            (r'^## (.*?)$', r'<h2>\1</h2>'),
            (r'^### (.*?)$', r'<h3>\1</h3>'),
            (r'^#### (.*?)$', r'<h4>\1</h4>'),  # Added H4
            (r'^##### (.*?)$', r'<h5>\1</h5>'),  # Added H5
            (r'^###### (.*?)$', r'<h6>\1</h6>'),  # Added H6
            (r'\*\*(.*?)\*\*', r'<strong>\1</strong>'),  # Changed to <strong> for semantic HTML
            (r'\*(.*?)\*', r'<em>\1</em>'),  # Changed to <em> for semantic HTML
            (r'~~(.*?)~~', r'<del>\1</del>'),  # Changed to <del> for semantic HTML
            (r'`(.*?)`', r'<code>\1</code>'),  # Inline code
            (r'^- (.*?)$', r'<li>\1</li>'),  # Unordered list
            (r'^\d+\. (.*?)$', r'<li>\1</li>'),  # Ordered list
            (r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>'),  # Links
            (r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1">'),  # Images
            (r'^\s*>\s*(.*?)$', r'<blockquote>\1</blockquote>'),  # Blockquote
            (r'^\|(.+?)\|$', r'<tr><td>\1</td></tr>'),  # Simple table row
            (r'^---$', r'<hr>'),  # Horizontal rule

            # Text Effects
            (r'@rainbow{(.*?)}', r'<span class="rainbow">\1</span>'),
            (r'@blink{(.*?)}', r'<span class="blink">\1</span>'),
            (r'@shout{(.*?)}', r'<span class="shout">\1</span>'),
            (r'@whisper{(.*?)}', r'<span class="whisper">\1</span>'),
            (r'@glow{(.*?)}', r'<span class="glow">\1</span>'),
            (r'@spin{(.*?)}', r'<span class="spin">\1</span>'),
            (r'@dance{(.*?)}', r'<span class="dance">\1</span>'),
            (r'@bubble{(.*?)}', r'<span class="bubble">\1</span>'),
            (r'@retro{(.*?)}', r'<span class="retro">\1</span>'),
            (r'@neon{(.*?)}', r'<span class="neon">\1</span>'),
            (r'@big{(.*?)}', r'<span class="big">\1</span>'),
            (r'@tiny{(.*?)}', r'<span class="tiny">\1</span>'),
            (r'@shadow{(.*?)}', r'<span class="shadow">\1</span>'),
            (r'@flip{(.*?)}', r'<span class="flip">\1</span>'),
            (r'@wave{(.*?)}', r'<span class="wave">\1</span>'),
            (r'@magic{(.*?)}', r'<span class="magic">\1</span>'),
            (r'@ghost{(.*?)}', r'<span class="ghost">\1</span>'),
            (r'@bounce{(.*?)}', r'<span class="bounce">\1</span>'),
            (r'@fire{(.*?)}', r'<span class="fire">\1</span>'),
            (r'@ice{(.*?)}', r'<span class="ice">\1</span>'),
            (r'@star{(.*?)}', r'<span class="star">\1</span>'),
            (r'@pulse{(.*?)}', r'<span class="pulse">\1</span>'),
            (r'@fade{(.*?)}', r'<span class="fade">\1</span>'),
            (r'@zoom{(.*?)}', r'<span class="zoom">\1</span>'),
            (r'@shake{(.*?)}', r'<span class="shake">\1</span>'),
            (r'@glitch{(.*?)}', r'<span class="glitch">\1</span>'),
            (r'@vaporwave{(.*?)}', r'<span class="vaporwave">\1</span>'),
            (r'@cyber{(.*?)}', r'<span class="cyber">\1</span>'),
            (r'@holo{(.*?)}', r'<span class="holo">\1</span>'),
            (r'@metal{(.*?)}', r'<span class="metal">\1</span>'),
            (r'@crystal{(.*?)}', r'<span class="crystal">\1</span>'),
            (r'@float{(.*?)}', r'<span class="float">\1</span>'),
            (r'@orbit{(.*?)}', r'<span class="orbit">\1</span>'),
            (r'@twist{(.*?)}', r'<span class="twist">\1</span>'),
            (r'@blur{(.*?)}', r'<span class="blur">\1</span>'),
            (r'@invert{(.*?)}', r'<span class="invert">\1</span>'),
            (r'@sepia{(.*?)}', r'<span class="sepia">\1</span>'),
            (r'@grayscale{(.*?)}', r'<span class="grayscale">\1</span>'),
            (r'@rain{(.*?)}', r'<span class="rain">\1</span>'),
            (r'@thunder{(.*?)}', r'<span class="thunder">\1</span>'),
            (r'@sparkle{(.*?)}', r'<span class="sparkle">\1</span>'),
            (r'@warp{(.*?)}', r'<span class="warp">\1</span>'),
            (r'@pixel{(.*?)}', r'<span class="pixel">\1</span>'),
            (r'@matrix{(.*?)}', r'<span class="matrix">\1</span>'),
            (r'@cosmic{(.*?)}', r'<span class="cosmic">\1</span>'),
            (r'@galaxy{(.*?)}', r'<span class="galaxy">\1</span>'),
            (r'@nova{(.*?)}', r'<span class="nova">\1</span>'),
            (r'@eclipse{(.*?)}', r'<span class="eclipse">\1</span>'),
            (r'@aurora{(.*?)}', r'<span class="aurora">\1</span>'),
            (r'@prism{(.*?)}', r'<span class="prism">\1</span>'),
            (r'@fractal{(.*?)}', r'<span class="fractal">\1</span>'),
            (r'@vortex{(.*?)}', r'<span class="vortex">\1</span>'),
            (r'@plasma{(.*?)}', r'<span class="plasma">\1</span>'),
            (r'@flux{(.*?)}', r'<span class="flux">\1</span>'),
            (r'@radiate{(.*?)}', r'<span class="radiate">\1</span>'),
            (r'@echo{(.*?)}', r'<span class="echo">\1</span>'),
            (r'@ripple{(.*?)}', r'<span class="ripple">\1</span>'),
            (r'@splash{(.*?)}', r'<span class="splash">\1</span>'),
            (r'@drift{(.*?)}', r'<span class="drift">\1</span>'),
            (r'@surge{(.*?)}', r'<span class="surge">\1</span>'),
            (r'@tide{(.*?)}', r'<span class="tide">\1</span>'),
            (r'@mist{(.*?)}', r'<span class="mist">\1</span>'),
            (r'@flame{(.*?)}', r'<span class="flame">\1</span>'),
            (r'@smoke{(.*?)}', r'<span class="smoke">\1</span>'),
            (r'@dust{(.*?)}', r'<span class="dust">\1</span>'),
            (r'@sand{(.*?)}', r'<span class="sand">\1</span>'),
            (r'@wind{(.*?)}', r'<span class="wind">\1</span>'),
            (r'@storm{(.*?)}', r'<span class="storm">\1</span>'),
            (r'@shadowdance{(.*?)}', r'<span class="shadowdance">\1</span>'),
            (r'@lightning{(.*?)}', r'<span class="lightning">\1</span>'),

            # Structural Elements
            (r'@quote{(.*?)}', r'<blockquote>\1</blockquote>'),
            (r'@alert{(.*?)}', r'<div class="alert">\1</div>'),
            (r'@note{(.*?)}', r'<div class="note">\1</div>'),
            (r'@code{(.*?)}', r'<pre><code>\1</code></pre>'),

            # Colors
            (r'@red{(.*?)}', r'<span class="red">\1</span>'),
            (r'@blue{(.*?)}', r'<span class="blue">\1</span>'),
            (r'@green{(.*?)}', r'<span class="green">\1</span>'),
            (r'@purple{(.*?)}', r'<span class="purple">\1</span>'),

            # Interactive
            (r'@button{(.*?)}', r'<button>\1</button>'),
            (r'@spoiler{(.*?)}', r'<span class="spoiler">\1</span>'),

            # Alignment
            (r'@center{(.*?)}', r'<div class="center">\1</div>'),
            (r'@right{(.*?)}', r'<div class="right">\1</div>'),

            # Additional Formatting
            (r'@emoji{(.*?)}', r'<span class="emoji">\1</span>'),
            (r'@highlight{(.*?)}', r'<mark>\1</mark>'),
            (r'@var{(.*?)=(.*?)}', r'<span class="var" data-name="\1" data-value="\2"></span>'),
        ]

    def process_code_block(self, code_content):
        lines = code_content.split('\n')
        html_lines = []
        variables = {}
        
        for line in lines:
            line = escape(line.strip())
            if line.startswith('@var{'):
                var_match = re.search(r'@var{(.*?)=(.*?)}', line)
                if var_match:
                    name, value = var_match.groups()
                    variables[name] = value
                    continue
            
            if line.startswith('@foreach{'):
                items = re.search(r'@foreach{(.*?)}:(.*)', line)
                if items:
                    list_items, content = items.groups()
                    html_lines.append(self.process_foreach(list_items, content, variables))
                else:
                    html_lines.append(f'<div class="code-line error">⚠️ Invalid @foreach syntax: {line}</div>')
            
            elif line.startswith('@for{'):
                range_match = re.search(r'@for{(\d+)-(\d+)}:(.*)', line)
                if range_match:
                    start, end, content = range_match.groups()
                    html_lines.append(self.process_for(int(start), int(end), content, variables))
                else:
                    html_lines.append(f'<div class="code-line error">⚠️ Invalid @for syntax: {line}</div>')
            
            elif line.startswith('@while{'):
                count_match = re.search(r'@while{(\d+)}:(.*)', line)
                if count_match:
                    count, content = count_match.groups()
                    html_lines.append(self.process_while(int(count), content, variables))
                else:
                    html_lines.append(f'<div class="code-line error">⚠️ Invalid @while syntax: {line}</div>')
            
            elif line.startswith('@repeat{'):
                repeat_match = re.search(r'@repeat{(\d+)}:(.*)', line)
                if repeat_match:
                    times, content = repeat_match.groups()
                    html_lines.append(self.process_repeat(int(times), content, variables))
                else:
                    html_lines.append(f'<div class="code-line error">⚠️ Invalid @repeat syntax: {line}</div>')
            
            else:
                processed_line = self.replace_vars(line, variables)
                for pattern, replacement in self.patterns:
                    processed_line = re.sub(pattern, replacement, processed_line)
                html_lines.append(f'<div class="code-line">{processed_line}</div>')
        
        return '\n'.join(html_lines)

    def replace_vars(self, content, variables):
        for name, value in variables.items():
            content = content.replace(f'{{{name}}}', value)
        return content

    def process_foreach(self, items, content, variables):
        item_list = [item.strip() for item in items.split(',')]
        result = ['<ul class="foreach-loop">']
        for item in item_list:
            processed = content.replace('{item}', item)
            processed = self.replace_vars(processed, variables)
            for pattern, replacement in self.patterns:
                processed = re.sub(pattern, replacement, processed)
            result.append(f'<li>{processed}</li>')
        result.append('</ul>')
        return '\n'.join(result)

    def process_for(self, start, end, content, variables):
        result = ['<ul class="for-loop">']
        for i in range(start, end + 1):
            processed = content.replace('{i}', str(i))
            processed = self.replace_vars(processed, variables)
            for pattern, replacement in self.patterns:
                processed = re.sub(pattern, replacement, processed)
            result.append(f'<li>{processed}</li>')
        result.append('</ul>')
        return '\n'.join(result)

    def process_while(self, count, content, variables):
        result = ['<ul class="while-loop">']
        i = 0
        while i < count:
            processed = content.replace('{i}', str(i))
            processed = self.replace_vars(processed, variables)
            for pattern, replacement in self.patterns:
                processed = re.sub(pattern, replacement, processed)
            result.append(f'<li>{processed}</li>')
            i += 1
        result.append('</ul>')
        return '\n'.join(result)

    def process_repeat(self, times, content, variables):
        result = ['<ul class="repeat-loop">']
        for _ in range(times):
            processed = self.replace_vars(content, variables)
            for pattern, replacement in self.patterns:
                processed = re.sub(pattern, replacement, processed)
            result.append(f'<li>{processed}</li>')
        result.append('</ul>')
        return '\n'.join(result)

    def compile(self, markfunk_text):
        html = ['<!DOCTYPE html>',
'<html>',
'<head>',
'<meta charset="UTF-8">',
'<title>MarkFunk Document</title>',
'<style>',
'/* General Styles */',
'body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }',
'h1, h2, h3, h4, h5, h6 { margin: 10px 0; }',
'ul, ol { margin: 10px 0 10px 20px; padding: 0; }',
'li { margin: 5px 0; }',
'blockquote { margin: 10px 0 10px 20px; padding: 10px; border-left: 4px solid #ccc; }',
'hr { border: 0; border-top: 1px solid #ccc; margin: 20px 0; }',
'img { max-width: 100%; height: auto; }',
'a { color: #0066cc; text-decoration: none; }',
'a:hover { text-decoration: underline; }',
'pre { background: #f0f0f0; padding: 10px; border-radius: 5px; overflow-x: auto; }',
'code { background: #f0f0f0; padding: 2px 5px; border-radius: 3px; }',
'',
'/* Code Block Styles */',
'.code-block { background: #f0f0f0; padding: 15px; border-radius: 5px; }',
'.code-line { margin: 5px 0; }',
'.code-line.error { color: red; font-weight: bold; }',
'.foreach-loop { list-style-type: circle; }',
'.for-loop { list-style-type: square; }',
'.while-loop { list-style-type: decimal; }',
'.repeat-loop { list-style-type: disc; }',
'',
'/* Funky Effects */',
'.rainbow { animation: rainbow 3s infinite; }',
'@keyframes rainbow { 0% { color: red; } 50% { color: blue; } 100% { color: red; } }',
'.blink { animation: blink 1s infinite; }',
'@keyframes blink { 50% { opacity: 0; } }',
'.shout { text-transform: uppercase; font-weight: bold; }',
'.whisper { font-size: 0.8em; color: #666; }',
'.glow { text-shadow: 0 0 5px yellow; }',
'.spin { animation: spin 2s infinite linear; display: inline-block; }',
'@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }',
'.dance { animation: dance 1s infinite; display: inline-block; }',
'@keyframes dance { 0% { transform: translateX(0); } 50% { transform: translateX(10px); } }',
'.bubble { border-radius: 50%; padding: 10px; background: #f0f0f0; display: inline-block; }',
'.retro { font-family: monospace; background: #000; color: #0f0; padding: 2px 5px; }',
'.neon { text-shadow: 0 0 10px #fff, 0 0 20px #ff00ff; }',
'.big { font-size: 1.5em; }',
'.tiny { font-size: 0.75em; }',
'.shadow { text-shadow: 2px 2px 4px #000; }',
'.flip { transform: rotate(180deg); display: inline-block; }',
'.wave { text-decoration: wavy underline; }',
'.magic { animation: magic 2s infinite; }',
'@keyframes magic { 0% { color: purple; } 50% { color: gold; } }',
'.ghost { opacity: 0.5; }',
'.bounce { animation: bounce 1s infinite; display: inline-block; }',
'@keyframes bounce { 0% { transform: translateY(0); } 50% { transform: translateY(-10px); } }',
'.fire { background: linear-gradient(to top, red, orange); color: white; padding: 2px 5px; }',
'.ice { color: lightblue; text-shadow: 0 0 5px #aaf; }',
'.star { animation: star 1s infinite; }',
'@keyframes star { 0% { text-shadow: 0 0 5px yellow; } 50% { text-shadow: 0 0 15px gold; } }',
'.pulse { animation: pulse 1s infinite; }',
'@keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.1); } }',
'.fade { animation: fade 2s infinite; }',
'@keyframes fade { 0% { opacity: 1; } 50% { opacity: 0.5; } }',
'.zoom { animation: zoom 1s infinite; }',
'@keyframes zoom { 0% { transform: scale(1); } 50% { transform: scale(1.2); } }',
'.shake { animation: shake 0.5s infinite; display: inline-block; }',
'@keyframes shake { 0% { transform: translateX(0); } 25% { transform: translateX(5px); } 75% { transform: translateX(-5px); } }',
'.glitch { animation: glitch 0.3s infinite; }',
'@keyframes glitch { 0% { transform: skew(0deg); } 50% { transform: skew(2deg); } }',
'.vaporwave { color: #ff66cc; text-shadow: 2px 2px #33ccff; }',
'.cyber { font-family: monospace; color: #00ff00; background: #000; padding: 2px 5px; }',
'.holo { color: rgba(255,255,255,0.7); text-shadow: 0 0 10px cyan; }',
'.metal { background: linear-gradient(45deg, #666, #999); color: #fff; padding: 2px 5px; }',
'.crystal { background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.5); padding: 2px 5px; }',
'.float { animation: float 3s infinite; display: inline-block; }',
'@keyframes float { 0% { transform: translateY(0); } 50% { transform: translateY(-10px); } }',
'.orbit { animation: orbit 4s infinite; display: inline-block; }',
'@keyframes orbit { 0% { transform: rotate(0deg) translateX(10px); } 100% { transform: rotate(360deg) translateX(10px); } }',
'.twist { animation: twist 2s infinite; display: inline-block; }',
'@keyframes twist { 0% { transform: rotateY(0deg); } 50% { transform: rotateY(180deg); } }',
'.blur { filter: blur(2px); }',
'.invert { filter: invert(100%); }',
'.sepia { filter: sepia(100%); }',
'.grayscale { filter: grayscale(100%); }',
'.rain { background: linear-gradient(to bottom, #87CEEB, #4682B4); color: white; padding: 2px 5px; }',
'.thunder { animation: thunder 1s infinite; }',
'@keyframes thunder { 0% { opacity: 1; } 10% { opacity: 0.5; } 20% { opacity: 1; } }',
'.sparkle { animation: sparkle 1s infinite; }',
'@keyframes sparkle { 0% { text-shadow: 0 0 5px white; } 50% { text-shadow: 0 0 15px yellow; } }',
'.warp { animation: warp 2s infinite; }',
'@keyframes warp { 0% { transform: scaleX(1); } 50% { transform: scaleX(1.2); } }',
'.pixel { font-family: monospace; image-rendering: pixelated; }',
'.matrix { color: #00ff00; background: #000; animation: matrix 5s infinite; }',
'@keyframes matrix { 0% { transform: translateY(0); } 100% { transform: translateY(20px); } }',
'.cosmic { background: radial-gradient(circle, #000033, #000066); color: white; padding: 2px 5px; }',
'.galaxy { background: linear-gradient(to right, #0f0c29, #302b63, #24243e); color: white; padding: 2px 5px; }',
'.nova { animation: nova 2s infinite; }',
'@keyframes nova { 0% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.5); opacity: 0.5; } }',
'.eclipse { background: radial-gradient(circle, #333, #000); color: white; padding: 2px 5px; }',
'.aurora { background: linear-gradient(45deg, #00ffcc, #ff00ff); animation: aurora 5s infinite; }',
'@keyframes aurora { 0% { opacity: 0.8; } 50% { opacity: 1; } }',
'.prism { background: linear-gradient(45deg, red, blue, green); color: white; padding: 2px 5px; }',
'.fractal { animation: fractal 3s infinite; }',
'@keyframes fractal { 0% { transform: rotate(0deg) scale(1); } 50% { transform: rotate(90deg) scale(1.1); } }',
'.vortex { animation: vortex 3s infinite; display: inline-block; }',
'@keyframes vortex { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }',
'.plasma { background: radial-gradient(circle, purple, blue); animation: plasma 4s infinite; }',
'@keyframes plasma { 0% { opacity: 0.7; } 50% { opacity: 1; } }',
'.flux { animation: flux 2s infinite; }',
'@keyframes flux { 0% { transform: skew(0deg); } 50% { transform: skew(5deg); } }',
'.radiate { animation: radiate 2s infinite; }',
'@keyframes radiate { 0% { text-shadow: 0 0 5px white; } 50% { text-shadow: 0 0 15px white; } }',
'.echo { animation: echo 2s infinite; }',
'@keyframes echo { 0% { opacity: 1; } 50% { opacity: 0.3; } }',
'.ripple { animation: ripple 2s infinite; }',
'@keyframes ripple { 0% { transform: scale(1); } 50% { transform: scale(1.1); } }',
'.splash { animation: splash 1s infinite; display: inline-block; }',
'@keyframes splash { 0% { transform: translateY(0); } 50% { transform: translateY(-5px); } }',
'.drift { animation: drift 3s infinite; display: inline-block; }',
'@keyframes drift { 0% { transform: translateX(0); } 50% { transform: translateX(10px); } }',
'.surge { animation: surge 2s infinite; }',
'@keyframes surge { 0% { transform: scale(1); } 50% { transform: scale(1.05); } }',
'.tide { animation: tide 4s infinite; display: inline-block; }',
'@keyframes tide { 0% { transform: translateY(0); } 50% { transform: translateY(5px); } }',
'.mist { background: rgba(200,200,200,0.5); animation: mist 3s infinite; }',
'@keyframes mist { 0% { opacity: 0.5; } 50% { opacity: 0.8; } }',
'.flame { background: linear-gradient(to top, red, orange); color: white; padding: 2px 5px; }',
'.smoke { color: #666; animation: smoke 3s infinite; }',
'@keyframes smoke { 0% { transform: translateY(0); opacity: 1; } 100% { transform: translateY(-10px); opacity: 0.5; } }',
'.dust { color: #cc9966; animation: dust 2s infinite; }',
'@keyframes dust { 0% { opacity: 1; } 50% { opacity: 0.7; } }',
'.sand { background: #f4a460; color: white; padding: 2px 5px; }',
'.wind { animation: wind 2s infinite; display: inline-block; }',
'@keyframes wind { 0% { transform: translateX(0); } 50% { transform: translateX(5px); } }',
'.storm { background: #333; color: white; animation: storm 1s infinite; }',
'@keyframes storm { 0% { opacity: 1; } 10% { opacity: 0.8; } 20% { opacity: 1; } }',
'.shadowdance { animation: shadowdance 2s infinite; }',
'@keyframes shadowdance { 0% { text-shadow: 2px 2px 5px black; } 50% { text-shadow: -2px -2px 5px black; } }',
'.lightning { animation: lightning 0.5s infinite; }',
'@keyframes lightning { 0% { opacity: 1; } 10% { opacity: 0; } 20% { opacity: 1; } }',
'',
'/* Structural Elements */',
'.alert { border: 2px solid red; padding: 10px; }',
'.note { background: #f0f0f0; padding: 10px; }',
'.center { text-align: center; }',
'.right { text-align: right; }',
'.spoiler { background: #000; color: #000; }',
'.spoiler:hover { color: #fff; }',
'',
'/* Colors */',
'.red { color: red; }',
'.blue { color: blue; }',
'.green { color: green; }',
'.purple { color: purple; }',
'</style>',
'</head>',
'<body>']


        lines = markfunk_text.split('\n')
        in_code_block = False
        code_content = []

        for line in lines:
            if line.strip() == '```':
                if not in_code_block:
                    in_code_block = True
                    code_content = []
                else:
                    in_code_block = False
                    html.append('<div class="code-block">')
                    html.append(self.process_code_block('\n'.join(code_content)))
                    html.append('</div>')
            elif in_code_block:
                code_content.append(line)
            else:
                processed_line = escape(line.strip())
                for pattern, replacement in self.patterns:
                    processed_line = re.sub(pattern, replacement, processed_line)
                if processed_line:
                    html.append(processed_line)

        html.extend(['</body>', '</html>'])
        return '\n'.join(html)

def main():
    parser = argparse.ArgumentParser(description="Compile MarkFunk files to HTML with funky flair!")
    parser.add_argument("filepath", help="Path to the MarkFunk file (e.g., EXAMPLE.md)")
    parser.add_argument("--open-web", action="store_true", help="Open the compiled HTML in your default web browser")
    args = parser.parse_args()

    # Check if file exists
    if not os.path.isfile(args.filepath):
        print(f"{Fore.RED}✘ Oops!{Style.RESET_ALL} The file '{args.filepath}' doesn't exist. Did you mistype the name or path?")
        print(f"{Fore.YELLOW}Tip:{Style.RESET_ALL} Make sure the file is in the right directory and try again!")
        return

    # Read the MarkFunk file
    try:
        with open(args.filepath, 'r', encoding='utf-8') as f:
            markfunk_text = f.read()
    except FileNotFoundError:  # This shouldn't happen due to prior check, but included for completeness
        print(f"{Fore.RED}✘ Yikes!{Style.RESET_ALL} Couldn't find '{args.filepath}'. It vanished!")
        return
    except PermissionError:
        print(f"{Fore.RED}✘ Uh-oh!{Style.RESET_ALL} No permission to read '{args.filepath}'. Check your file permissions.")
        return
    except Exception as e:
        print(f"{Fore.RED}✘ Something went wrong!{Style.RESET_ALL} Error reading '{args.filepath}': {str(e)}")
        print(f"{Fore.YELLOW}Tip:{Style.RESET_ALL} Ensure the file is readable and not corrupted.")
        return

    # Compile the MarkFunk
    compiler = MarkFunkCompiler()
    html_output = compiler.compile(markfunk_text)

    # Write to output file
    output_file = 'output.html'
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"{Fore.GREEN}✔ Success!{Style.RESET_ALL} Your MarkFunk file has been compiled to '{output_file}'.")
    except PermissionError:
        print(f"{Fore.RED}✘ Oh no!{Style.RESET_ALL} Can't write to '{output_file}'. Check your write permissions!")
        return
    except Exception as e:
        print(f"{Fore.RED}✘ Bummer!{Style.RESET_ALL} Failed to write '{output_file}': {str(e)}")
        print(f"{Fore.YELLOW}Tip:{Style.RESET_ALL} Ensure you have space and write access in this directory.")
        return

    # Open in web browser if --open-web is specified
    if args.open_web:
        try:
            webbrowser.open(f'file://{os.path.abspath(output_file)}')
            print(f"{Fore.GREEN}✔ Cool!{Style.RESET_ALL} Opened '{output_file}' in your default web browser.")
        except Exception as e:
            print(f"{Fore.RED}✘ Darn!{Style.RESET_ALL} Couldn't open the browser: {str(e)}")
            print(f"{Fore.YELLOW}Tip:{Style.RESET_ALL} You can manually open '{output_file}' in your browser.")

if __name__ == "__main__":
    main()