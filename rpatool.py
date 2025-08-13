#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# rpatool.py - Tool for extracting/creating Ren'Py RPA archives.
# License: MIT
# Source: Adapted for standalone use from original rpatool project

import os
import sys
import struct
import zlib

def extract_rpa(input_file, output_dir):
    """
    Extracts files from a Ren'Py RPA archive into output_dir.
    """
    with open(input_file, "rb") as f:
        # Read magic header
        magic = f.read(8)
        if not magic.startswith(b"RPA-3.") and not magic.startswith(b"RPA-2."):
            raise Exception("Not a valid RPA file")

        version = magic.decode("utf-8").strip()
        print(f"[INFO] RPA Version: {version}")

        # Read index offset
        f.seek(-8, os.SEEK_END)
        index_offset = int(f.read(8), 16)
        f.seek(index_offset)

        # Decompress index
        index_data = zlib.decompress(f.read())
        index_text = index_data.decode("utf-8", errors="replace")

        index = {}
        for line in index_text.strip().split("\n"):
            parts = line.strip().split(",")
            if len(parts) >= 3:
                filename, offset, length = parts[0], int(parts[1]), int(parts[2])
                index[filename] = (offset, length)

        # Extract files
        for filename, (offset, length) in index.items():
            out_path = os.path.join(output_dir, filename)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            f.seek(offset)
            data = f.read(length)
            with open(out_path, "wb") as out_f:
                out_f.write(data)
            print(f"[OK] Extracted: {filename}")

    print(f"[DONE] All files extracted to: {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} archive.rpa output_dir")
        sys.exit(1)
    extract_rpa(sys.argv[1], sys.argv[2])

