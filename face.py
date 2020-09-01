# -*- coding: utf-8 -*-

import cv2
import numpy as np

def main():
    img = cv2.imread("hoge.JPG")
    # step1: テスト画像データを読み込む
    keypoint = img

    # step2: 特徴点検出を行う
    gftt = cv2.FastFeatureDetector_create()
    keypoints = gftt.detect(img)

    # step3: 結果を表示する
    keypoint = cv2.drawKeypoints(img, keypoints, keypoint)
    cv2.imshow("keypoints", keypoint)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
