#! /usr/bin/python

import logging
import argparse

parser = argparse.ArgumentParser(description='Face detector')
parser.add_argument('-i', '--input-dir', help='Directory where images are stored')
parser.add_argument('-o', '--output-dir', help='Directory where output images are stored')
parser.add_argument('-v', '--verbose', help='Verbose process output', action='store_true')

args = parser.parse_args()

if args.verbose :
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

if args.input_dir == None:
    logging.error('No input directory specified')
    exit(1)

input_dir = args.input_dir
output_dir = args.output_dir

logging.debug('Found parameters Input Directory = %s, Output Directory = %s', args.input_dir, args.output_dir)

# TODO: Assumption here is that whatever there is in input directory is
# TODO: consider as a image even as text file. Hence we need only images in input_dir

import listdir
import processfile

files = listdir.get_files(args.input_dir)
logging.debug('Got files: %s', files)
for file in files:
    logging.debug('Processing file %s', file)
    processfile.process(file, args.output_dir)

logging.info('Done')
