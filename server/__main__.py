import itertools
import json
import math

import board
import neopixel
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

with open("config.json", "r") as config:
    config = json.loads(config.read())

PIXEL_COUNT = config["pixel_count"]
DEFAULT_BRIGHTNESS = config["default_brightness"]
PORT = config["port"]

COLOR_TYPE = tuple[int, int, int]

pixels = neopixel.NeoPixel(
    board.D18, PIXEL_COUNT, auto_write=False, brightness=DEFAULT_BRIGHTNESS
)


class Color(BaseModel):
    color: int


class Brightness(BaseModel):
    brightness: float


class ColorPattern(BaseModel):
    colors: list[int]


class Gradient(BaseModel):
    colors: list[int]


app = FastAPI()


def hex_to_rgb(color: int) -> tuple[int, int, int]:
    r = (color >> (8 * 2)) & 255
    g = (color >> (8 * 1)) & 255
    b = color & 255
    return r, g, b


@app.post("/fill")
async def fill(color: Color):
    pixels.fill(color.color)
    pixels.show()


@app.post("/brightness")
async def brightness(b: Brightness):
    if 0 > b.brightness or 1 < b.brightness:
        raise HTTPException(
            status_code=400, detail="brightness must be in range form 0 to 1"
        )
    pixels.brightness = b.brightness
    pixels.show()


@app.post("/pattern")
async def pattern(pat: ColorPattern):
    colors = itertools.cycle(pat.colors)
    for i in range(PIXEL_COUNT):
        pixels[i] = next(colors)
    pixels.show()


@app.post("/gradient")
async def gradient(grad: Gradient):
    parts = len(grad.colors) - 1
    part_length = PIXEL_COUNT / parts

    for pixel in range(PIXEL_COUNT):
        part = pixel / part_length
        n = part % 1
        color1 = grad.colors[math.floor(part)]
        color2 = grad.colors[math.floor(part) + 1]
        r1, g1, b1 = hex_to_rgb(color1)
        r2, g2, b2 = hex_to_rgb(color2)
        r = math.floor(r1 * (1 - n) + r2 * n)
        g = math.floor(g1 * (1 - n) + g2 * n)
        b = math.floor(b1 * (1 - n) + b2 * n)
        pixels[pixel] = r, g, b

    pixels.show()


app.mount("", StaticFiles(directory="client/public/", html=True), name="static")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
