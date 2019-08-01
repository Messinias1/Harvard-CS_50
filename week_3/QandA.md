# Questions

## What's `stdint.h`?

The <stdint.h> header shall declare sets of integer types having specified widths, and shall define corresponding sets of macros (brief abbreviations for longer constructs). It shall also define macros that specify limits of integer types corresponding to types defined in other standard headers.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

When the programming tasks specify the integer width especially to accommodate some file or communication protocol format. With increasing needs for consistency, char, short, int, long and long long, are not enough (or at least not so easy) and so int8_t, int16_t, int32_t, int64_t are born. New languages tend to require very specific fixed integer size types and 2's complement.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE: 8-bit unsigned int, DWORD: 32-bit unsigned int, LONG: 32-bit signed int, WORD: 16-bit unsigned int

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

In ASCII: BM
In hexadecimal: 0x42 0x4D, same as BM in ASCII.

## What's the difference between `bfSize` and `biSize`?

bfSize: The size, in bytes, of the bitmap file.
biSize: The number of bytes required by the structure.

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top-down DIB (Device Independent Bitmap) and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

The biBitCount member of the BITMAPINFOHEADER structure determines the number of
bits that define each pixel and the maximum number of colors in the bitmap.

## Why might `fopen` return `NULL` in `copy.c`?

TODO

## Why is the third argument to `fread` always `1` in our code?

TODO

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

TODO

## What does `fseek` do?

TODO

## What is `SEEK_CUR`?

TODO
