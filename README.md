# TPBot AI Lens Line Follower

An intelligent robotic control system for the Elecfreaks TPBot and PlanetX AI Lens. This project enables a robot to wait for a specific visual trigger (object recognition) before initiating an automated line-following sequence.

## 🚀 Overview

The robot operates in two primary states:
1.  **Searching/Idle:** The robot remains stationary with red headlights until the AI Lens identifies a previously "learned" object (ID1).
2.  **Tracking:** Once the object is recognized, the robot switches to line-tracking mode, using its underside sensors to navigate a path.

## 🛠 Features

* **One-Button Learning:** Use Button A to teach the AI Lens a new object on the fly.
* **Visual Feedback:** The micro:bit LED matrix and TPBot RGB headlights change colors and icons to indicate current status (e.g., Happy, Sad, Learning, Searching).
* **Safety Stop:** Use the micro:bit logo (touch sensor) or Button B to immediately stop the motors and reset the system.
* **Robust Line Following:** Logic handling for straight paths, left turns, and right turns.

## 🕹 Controls

| Input | Action | Feedback |
| :--- | :--- | :--- |
| **Button A** | Learn current object as ID1 | LED: "L1" / Lights: Blue |
| **Button B** | Manual stop and status check | LED: Pattern / Lights: Cyan |
| **Logo** | Wipe memory and emergency stop | LED: "NO" / Lights: Off |

## 📋 Hardware Requirements

* [micro:bit V2](https://microbit.org/)
* [Elecfreaks TPBot](https://www.elecfreaks.com/tpbot.html)
* [PlanetX AI Lens](https://www.elecfreaks.com/planetx-ai-lens.html)

## ⚙️ Setup & Installation

1.  Open [MakeCode for micro:bit](https://makecode.microbit.org/).
2.  Click on **Extensions** and search for `TPBot` and `PlanetX-AILens`.
3.  Paste the code and download the `.hex` file to your micro:bit.

---
*Note: This project was designed using the Elecfreaks PlanetX and TPBot extension libraries.*
