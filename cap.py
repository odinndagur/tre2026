#! /usr/bin/python3

import os
import time

def main():
	tm = time.localtime()
	fname = f'{str(tm.tm_year).zfill(2)}-{str(tm.tm_mon).zfill(2)}-{str(tm.tm_mday).zfill(2)}_{str(tm.tm_hour).zfill(2)}:{str(tm.tm_min).zfill(2)}:{str(tm.tm_sec).zfill(2)}'
	print(fname)

	os.system(f'ffmpeg -i /dev/video0 -vframes 1 pics/{fname}.png')
	os.system('git add --all')
	os.system(f'git commit -am {fname}')
	os.system('git push')


if __name__ == '__main__':
	main()
