import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
# from scipy.signal import convolve2d

# the copy in the first lines of the function is so that you don't ruin
# the original image. it will create a new one. 

def add_SP_noise(im, p):
    sp_noise_im = im.copy()
    n,m =sp_noise_im.shape
    size = n * m
    # print("size = ", size)
    length = len(sp_noise_im)
    # print("length =", length)
    
    sp_noise_im = np.reshape(sp_noise_im, size, order='F')
    # print("sp noise  =",sp_noise_im)
    # print("sp length =",len(sp_noise_im))

    noise_pixels = int(size * p)
    # print("noise pixels = ", noise_pixels)
    noise_values = [0, 255]

    arr = random.sample( range(size) , noise_pixels)
    # print("arr =", arr)
    # print("sp noise shape =", sp_noise_im.shape)
    # print(sp_noise_im)

    for i in arr:
        # print("i type of = ", type(i))
        sp_noise_im[i] = random.choice(noise_values)

    sp_noise_im = np.reshape(sp_noise_im, (n, m) , order='F')
    # print("return image = ")
    # print(sp_noise_im)
    return sp_noise_im


def clean_SP_noise_single(im, radius):              # median
    noise_im = im.copy()
    # print("clean_SP_noise_single -> orig:\n", noise_im)

    noise_im= np.pad(noise_im, pad_width = radius, mode = 'constant')
    # print("clean_SP_noise_single -> added padding:\n", noise_im)
    clean_im = noise_im
    median_arr_size = radius * 2 + 1
    # print("median_arr_size = ", median_arr_size)

    for row in range(radius, len(noise_im)-radius):
        for culomn in range(radius, len(noise_im[row])-radius):
            if noise_im[row][culomn] == 0 or noise_im[row][culomn] == 255:
                median_arr = (noise_im[(row - radius):(row - radius + median_arr_size), (culomn - radius):(culomn - radius + median_arr_size)])
                # print("median arr: \n", median_arr)
                median_val = np.median(median_arr)
                # print("median val: \n", median_val)
                clean_im[row][culomn] = median_val
            

    clean_im = delete_padding(clean_im, radius)
    # print("clean_SP_noise_single -> cleaned:\n", clean_im)

    return clean_im

def delete_padding(image, padding):
    for i in range(padding):
        n,m = image.shape
        image = np.delete(image, [0,m-1], axis = 1)       #column
        image = np.delete(image, [0,n-1], axis = 0)       #row

    # print("clean_SP_noise_single -> delete_padding:\n", image)    
    return image

def clean_SP_noise_multiple(images):
    # clean_images = images
    # for image in clean_images:
    #     clean_images = clean_SP_noise_single(image)
    return #clean_images


def add_Gaussian_Noise(im, s):
    gaussian_noise_im = im.copy()
    # TODO: add implementation

    return gaussian_noise_im


def clean_Gaussian_noise(im, radius, maskSTD):
    # TODO: add implementation
    return cleaned_im.astype(np.uint8)


def clean_Gaussian_noise_bilateral(im, radius, stdSpatial, stdIntensity):
    bilateral_im = im.copy()
    # TODO: add implementation

    return bilateral_im.astype(np.uint8)


