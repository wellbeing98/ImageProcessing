import cv2


# 영상 소스 열기

src = cv2.imread("images/picture01.jpg")

## 영상 처리 알고리즘 구현
dst1 = cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
dst2 = src.copy()
_, dst2  = cv2.threshold(dst2, 127, 255, cv2.THRESH_BINARY)

# 영상 디스플레이
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)

# 마무리


cv2.waitKey(0)
cv2.destroyAllWindows()
