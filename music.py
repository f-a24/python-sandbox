# -*- coding: utf-8 -*-

# pygame(Pythonのゲーム用ライブラリ)を使用する
# pipが入っていればコマンドでインストール可能「pip install pygame」
import pygame.mixer
import time
import os
import random
import sys

# 同階層の"music"ディレクトリから再生リストを取得し、シャッフル
folder = os.getcwd() + "/music/"
songList = os.listdir(folder)
random.shuffle(songList)

pygame.mixer.init()

# 再生リストを最後まで再生
for song in songList:
    pygame.mixer.music.load(folder + song)
    pygame.mixer.music.play(1) # ループ回数（-1だと無限ループ）
    while True:
        if not pygame.mixer.music.get_busy():
            break
