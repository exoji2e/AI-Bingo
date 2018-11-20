from PIL import Image, ImageDraw, ImageFont
import textwrap
import cv2
import argparse
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help="input-file with bingo text")
    parser.add_argument('-o', '--outputfolder', default='imgs', help="output-folder for images")
    return parser.parse_args()

def create_im(text, sz, cnt):
    MAX_W, MAX_H = (400, 400)
    para = textwrap.wrap(text, width=cnt)
    im = Image.new("RGB", (MAX_W, MAX_H), "white")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('Roboto-Medium.ttf', sz)
    L = len(para)
    _, h = draw.textsize(para[0], font=font)
    pad = 10
    curr_h = int(MAX_H/2 - (h+pad)*(L/2.))
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W-w)/2, curr_h), line, fill="black", font=font)
        curr_h += h + pad
    return im

def add_border(img, bordersize=10):
    return cv2.copyMakeBorder(img, 
        top = bordersize,
        bottom = bordersize,
        left = bordersize,
        right = bordersize,
        borderType = cv2.BORDER_CONSTANT,
        value = (0, 0, 0))


def save_im(text, out_file):
    print(text)
    sz = 50
    cnt = 20
    while True:
        im = create_im(text, sz, cnt)
        im.save("test.png", "PNG")
        im2 = cv2.imread("test.png")
        image = add_border(im2)
        cv2.imshow("test", image)
        k = cv2.waitKey()
        if k == ord('w'):
            sz += 2
        elif k == ord('s'):
            sz -= 2
        if k == ord('d'):
            cnt += 1
        elif k == ord('a'):
            cnt -= 1
        elif k == ord('o'):
            break
        elif k == ord('q'):
            return
    cv2.imwrite(out_file, image)

if __name__ == '__main__':
    args = get_args()
    for i, line in enumerate(open(args.input).read().strip().split('\n')):
        save_im(line, '{}/{}.png'.format(args.outputfolder.rstrip('/'), i))
