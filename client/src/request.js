const BASE_URL = "http://raspberrypi.local:8000";

async function request(endpoint, body) {
  await fetch(`${BASE_URL}/${endpoint}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
}

async function setPattern(colors) {
  await request("pattern", { colors });
}

async function setBrightness(brightness) {
  await request("brightness", { brightness });
}

async function setGradient(colors) {
  await request("gradient", { colors });
}

async function setAll(color) {
  await request("fill", { color });
}

export { setPattern, setBrightness, setGradient, setAll };
