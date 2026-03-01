from machine import Pin

# Mapeamento de Pinos para ESP32-C3 Super Mini
PINS = {
    "sda": 8, "scl": 9,      # I2C para OLED
    "sck": 4, "miso": 5,     # SPI para CC1101
    "mosi": 6, "cs": 7,      # SPI para CC1101
    "gdo0": 10,              # Interrupção Rádio
    "up": 0, "down": 1,      # Botões
    "ok": 2, "back": 3       # Botões
}

def setup_button(gpio):
    return Pin(gpio, Pin.IN, Pin.PULL_UP)

# Inicializa os botões
btn_up = setup_button(PINS["up"])
btn_down = setup_button(PINS["down"])
btn_ok = setup_button(PINS["ok"])
btn_back = setup_button(PINS["back"])
