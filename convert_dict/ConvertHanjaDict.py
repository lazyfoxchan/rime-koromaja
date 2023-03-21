# Convert libhangul hanja dict 2 rime-koromaja hanja dict
# License: GNU Lesser General Public License v2.1
# Author: lazy fox chan

import urllib.request
import convrules

HANJA_DICT_URL = "https://github.com/libhangul/libhangul/raw/main/data/hanja/hanja.txt"
FREQ_HANJA_DICT_URL = "https://github.com/libhangul/libhangul/raw/main/data/hanja/freq-hanja.txt"
FREQ_HANJAEO_DICT_URL = "https://github.com/libhangul/libhangul/raw/main/data/hanja/freq-hanjaeo.txt"

OUTPUT_FILE_NAME = "koromaja.hanja.dict.yaml"
OUTPUT_FILE_HEADER = \
"""# Rime dictionary
# encoding: utf-8
#
# This file was converted from libhangul project
# https://github.com/libhangul/libhangul
#
# --------------------------------------------------------------------------------
# Copyright (c) 2005,2006 Choe Hwanjin
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the author nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# --------------------------------------------------------------------------------

---
name: koromaja.hanja
version: "1.0"
sort: by_weight
use_preset_vocabulary: false
...

"""


def main():
    hanja_dict_file_name = HANJA_DICT_URL.split("/")[-1]
    freq_hanja_dict_file_name = FREQ_HANJA_DICT_URL.split("/")[-1]
    freq_hanjaeo_dict_file_name = FREQ_HANJAEO_DICT_URL.split("/")[-1]

    # Download libhangul dict
    print("Start download: " + HANJA_DICT_URL)
    urllib.request.urlretrieve(HANJA_DICT_URL, hanja_dict_file_name)
    print("Download complete: " + hanja_dict_file_name)

    print("Start download: " + FREQ_HANJA_DICT_URL)
    urllib.request.urlretrieve(FREQ_HANJA_DICT_URL, freq_hanja_dict_file_name)
    print("Download complete: " + freq_hanja_dict_file_name)

    print("Start download: " + FREQ_HANJAEO_DICT_URL)
    urllib.request.urlretrieve(FREQ_HANJAEO_DICT_URL, freq_hanjaeo_dict_file_name)
    print("Download complete: " + freq_hanjaeo_dict_file_name)

    # Get hanja and romaja
    hanja_list = []
    hanja_file = open(hanja_dict_file_name, "r", encoding="utf-8")
    for line_str in hanja_file:
        if line_str[0] == "#":
            continue
        if not ":" in line_str:
            continue
        line_list = line_str.split(":")
        try:
            hanja_list.append([line_list[1], hangul2romaja(line_list[0])])
        except KeyError:
            continue
    hanja_file.close()

    # Get hanja freq
    freq_hanja_dict = {}
    freq_hanja_file = open(freq_hanja_dict_file_name, "r", encoding="utf-8")
    for line_str in freq_hanja_file:
        if not ":" in line_str:
            continue
        line_list = line_str.replace("\n", "").split(":")
        freq_hanja_dict[line_list[0]] = int(line_list[1])
    freq_hanja_file.close()

    # Get hanjaeo freq
    freq_hanjaeo_dict = {}
    freq_hanjaeo_file = open(freq_hanjaeo_dict_file_name, "r", encoding="utf-8")
    for line_str in freq_hanjaeo_file:
        if not ":" in line_str:
            continue
        line_list = line_str.replace("\n", "").split(":")
        freq_hanjaeo_dict[line_list[0]] = int(line_list[1])
    freq_hanjaeo_file.close()

    # Marge freq
    final_list = []
    for hanja_romaja in hanja_list:
        try:
            final_list.append([hanja_romaja[0], hanja_romaja[1], str(freq_hanja_dict[hanja_romaja[0]] + 1)])
            continue
        except KeyError:
            pass
        try:
            final_list.append([hanja_romaja[0], hanja_romaja[1], str(freq_hanjaeo_dict[hanja_romaja[0]] + 1)])
            continue
        except KeyError:
            pass
        final_list.append([hanja_romaja[0], hanja_romaja[1], "1"])

    # Write dict file
    output_file = open(OUTPUT_FILE_NAME, "w", encoding="utf-8")
    output_file.write(OUTPUT_FILE_HEADER)
    for word in final_list:
        output_file.write(word[0] + "\t" + word[1] + "\t" + word[2] + "\n")  # word, hangul, freq
    output_file.close()
    print("CONVERT DONE!: " + OUTPUT_FILE_NAME)


def hangul2romaja(arg_str):
    return_str = ""
    hangul_list = list(arg_str)
    for hangul_str in hangul_list:
        return_str = return_str + convrules.CONVERT_RULES[hangul_str] + " "
    return return_str[:-1]


if __name__ == "__main__":
    main()
