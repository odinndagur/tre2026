#! /usr/bin/python3

import os
import time

def main():
	tm = time.localtime()
	fname = f'{tm.tm_year}-{tm.tm_mon}-{tm.tm_mday}_{tm.tm_hour}:{tm.tm_min}:{tm.tm_sec}'
	print(fname)

	os.system(f'ffmpeg -i /dev/video0 -vframes 1 pics/{fname}.png')
	os.system('git add --all')
	os.system(f'git commit -am {fname}')
	os.system('git push')


if __name__ == '__main__':
	main()
