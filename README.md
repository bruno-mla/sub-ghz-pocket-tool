# 📡 Sub-GHz Pocket Tool

## 🎓 CS50 Final Project
Este é o meu projeto final para o CS50 da Harvard University. É um dispositivo portátil modular capaz de analisar, capturar e replicar sinais de rádio Sub-GHz.

### 🔌 Escolha sua Plataforma
Este projeto foi desenhado para rodar em duas arquiteturas diferentes:
* [**Guia de Montagem: ESP32-C3 Super Mini**](./docs/ESP32-C3-Super-Mini-Setup.md) (Recomendado)
* [**Guia de Montagem: Raspberry Pi Pico**](.//docs/Raspberry-Pi-Pico-Setup.md)

---

## 📂 Estrutura do Projeto
* `/src`: Código fonte em MicroPython.
* `/docs`: Esquemas de pinagem e instruções de hardware.
* `/saves`: Pasta onde os sinais capturados (.json) serão armazenados.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** MicroPython
- **Hardware:** ESP32-C3 / RP2040 + CC1101 + OLED 0.96"

- **Conceitos:** Comunicação SPI/I2C, Gerenciamento de Arquivos, Interrupções de Hardware.



