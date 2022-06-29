import os
from cralwer import preprocessing

def createFolder(results):
  print('폴더 제작')

  directory = 'data'
  try:
    if not os.path.exists(directory):
      os.makedirs(directory)
  except OSError:
    print ('Error: Creating directory. ' +  directory)

  directory += '/' + results['node_category']
  try:
    if not os.path.exists(directory):
      os.makedirs(directory)
  except OSError:
    print ('Error: Creating directory. ' +  directory)

  directory += '/' + results['node_name']
  try:
    if not os.path.exists(directory):
      os.makedirs(directory)
  except OSError:
    print ('Error: Creating directory. ' +  directory)

def add_readme(results):
  print('목차 만들기')

  steps = results['steps']
  directory = results['node_category'] + '/' + results['node_name']
  
  md = '# 목차\n\n'
  md += results['node_blurb'] + '\n\n'
  for step in list(steps.keys()):
    md += f'1. [{step}](./{step}.md)\n'

  with open(f"{directory}/README.md", 'w', encoding='utf-8') as f:
    f.write(md)

def add_step_content(results):
  steps = results['steps']
  directory = results['node_category'] + '/' + results['node_name']

  for step in list(steps.keys()):
    md = f'# {step}\n\n'
    md += str(steps[step])

    step = preprocessing(step)
    with open(f"{directory}/{step}.md", 'w', encoding='utf-8') as f:
      f.write(md) 
