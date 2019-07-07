import numpy as np 
from PIL import Image 
import glob
import os
import argparse
import config

parser = argparse.ArgumentParser()
parser.add_argument("--input", default=None, help="path to folder containing input images")
parser.add_argument("--background", default=None, help="path to folder containing background images")
parser.add_argument("--target", default=None, help="path to folder containing target images")
parser.add_argument("--output_dir", default=None, help="path to folder to which output images saved'")

args = parser.parse_args()

if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

inputs = glob.glob(args.input + '/*-inputs*')
background = glob.glob(args.background + '/*-background*')
target = glob.glob(args.target + '/*-targets*')

flag = 1
for inp,back,tar in zip(inputs,background,target):
	inp,back,tar = Image.open(inp) , Image.open(back), Image.open(tar) 

	inp = inp.resize((256,256) , Image.BICUBIC)
	back = back.resize((256,256) , Image.BICUBIC)
	tar = tar.resize((256,256) , Image.BICUBIC)

	new_im = Image.new('RGB', (256*3, 256))

	x_offset = 0
	for im in [tar,back,inp]:
	  new_im.paste(im, (x_offset,0))
	  x_offset += im.size[0]

	new_im.save(args.output_dir + '/{}.jpg'.format(flag))
	flag+=1