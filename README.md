# Quick Dialog Bar

File::: codV001.txt

![Screenshot](https://i.ibb.co/mVQGCV27/barra-de-dialogos-rapidos.jpg)

## Overview

This project creates a **quick dialog bar** for customer service agents.
It provides predefined responses (short phrases or long texts) that can be copied with a single click, helping reduce response time and maintaining consistency in customer interactions.

The bar is built with **JavaScript + HTML**, dynamically generating buttons, inputs, and text areas from arrays of templates.

---

## Features

* **Quick Copy Buttons**: Each phrase or dialog has a dedicated button to copy its content into the clipboard.
* **Dynamic Greeting**: The bar generates greetings based on the current time of day (morning, afternoon, evening).
* **Predefined Templates**:

  * **Line Mode**: Simple one-line responses with a button.
  * **Matrix Mode**: Multi-button rows for grouped answers (e.g., FAQs, procedures).
  * **Plain Text Section**: Extra references (keywords or short phrases).
* **Agent Customization**: Agent’s name can be changed dynamically (`nombreAsesor`).


## Usage

1. Embed the `script.js` in your HTML page.
2. Update the `nombreAsesor` variable with your agent’s name.
3. Add or modify phrases inside the arrays (`arrayPlantillaEnLineas`, `arrayPlantillaMatriz`, etc.).
4. Reload your browser — the bar will be generated dynamically.

---

## Benefits

* Faster responses to customers.
* Consistency in messages (formal tone, required legal info).
* Easy to extend: just add a new object in the arrays.
* Adaptable for **chat, email, or CRM platforms**.

---

## Next Improvements (Ideas)

* Add **search** for phrases.
* Support for **multilingual responses**.
* Store frequently used phrases in **localStorage** or a **database**.
* Option to **edit phrases directly in the UI**.

---

## Author

Developed by **Álvaro Ruiz** – as a personal productivity tool for BPO/Call Center support.
