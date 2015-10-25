#!/bin/bash
sdcv -n -2 ~/Documents/stardict-21shijishuangxiangcidian-big5-2.4.2/ $1 | ./txt2html $1 > $2
