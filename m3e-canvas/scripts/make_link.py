#!/usr/bin/env python3
"""M3E Canvas: 把设计 JSON 压缩成分享链接（官方协议，raw deflate + base64url）。

用法: python make_link.py design.json
输出: https://lnkiai.github.io/m3e-canvas/#docz=<压缩后的设计>
"""
import sys
import zlib
import base64


def make_link(json_path: str) -> str:
    data = open(json_path, "rb").read()
    c = zlib.compressobj(9, zlib.DEFLATED, -15)  # raw deflate, no zlib header
    raw = c.compress(data) + c.flush()
    b64 = base64.urlsafe_b64encode(raw).decode().rstrip("=")
    return "https://lnkiai.github.io/m3e-canvas/#docz=" + b64


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python make_link.py design.json", file=sys.stderr)
        sys.exit(1)
    print(make_link(sys.argv[1]))
