# Derived from RPS Fujiwara's office interleave pjt

import cv2
import numpy as np
import argparse


def main(input_image, output_image):
    frame = cv2.imread(input_image)
    double_frame = cv2.resize(frame, dsize=(0, 0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR_EXACT)

    edges = cv2.Canny(double_frame, 60, 100)
    edges = edges.astype('float')

    x_edges = np.mean(edges, axis=1)
    y_edges = np.mean(edges, axis=0)


    def get_size(line, axis):
        line = line - np.mean(line) # removing DC component
        n = len(line)  # length of the signal
        k = np.arange(n)
        Fs = len(line)
        T = n / Fs
        freq = k / T  # two sides frequency range
        freq = freq[range(int(n / 2))]  # one side frequency range

        Y = np.fft.fft(line) / n  # fft computing and normalization
        Y = Y[range(int(n / 2))]

        index = np.argmax(Y[1:])
        pixel_count = int(round(freq[index]))
        pixel_size = n / pixel_count
        print(axis, pixel_count)

        return pixel_count


    orig_width = get_size(y_edges, 'width')
    orig_height = get_size(x_edges, 'height')
    orig_frame = cv2.resize(frame, dsize=(orig_width, orig_height), interpolation=cv2.INTER_LINEAR_EXACT)

    cv2.imwrite(output_image, orig_frame)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a pixel art image into original size.')
    parser.add_argument('input_image', type=str, help='Input image file name to convert')
    parser.add_argument('output_image', type=str, help='Output image file name')

    args = parser.parse_args()
    main(args.input_image, args.output_image)