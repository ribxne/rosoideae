# rosoideae 🌹

ws281x LED strip controller with web-based GUI for Raspberry Pi made using Svelte and FastAPI

## Requirements

- Raspberry Pi
- LED strip connected to [GPIO 18](https://pinout.xyz/)
- Python
- Node.js :(
- Electricity

## Usage

> **Warning**  
> The neopixel library requires root access

- Clone the repository
- Rename `config.example.json` to `config.json` and edit it to suit your needs
- Install `server` dependencies by running
  ```
  sudo poetry install
  ```
- Inside the `client` folder run
  ```
  npm i
  npm run build
  ```
- Start the server
  ```
  sudo poetry run python -m server
  ```

> **Note**  
> To change the base URL edit `client/src/request.js`

## To do

- [ ] Add more effects
- [ ] Config tab
- [ ] Replace current design with MD3
- [ ] Ability to change the language

## Screenshots

![](/images/1.png)

![](/images/2.png)
