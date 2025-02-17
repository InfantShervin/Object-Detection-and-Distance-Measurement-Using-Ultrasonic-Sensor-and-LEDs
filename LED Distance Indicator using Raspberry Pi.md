**LED Distance Indicator using Raspberry Pi** 

**Introduction** 

**Background** 

A distance indicator is commonly used in applications such as parking sensors, obstacle avoidance systems, and proximity alert mechanisms. By measuring distance using an ultrasonic sensor, these systems provide visual and audio feedback based on proximity, improving safety and usability. 

**Objective** 

The goal of this project is to build a **distance measurement and alert system** using a **Raspberry Pi**, **ultrasonic sensor (HC-SR04)**, **LED indicators**, and a **buzzer**. The LEDs will light up in different colors based on the measured distance, and a buzzer will activate when a predefined threshold is crossed. 

**Scope** 

This project includes: 

- Using an **HC-SR04 ultrasonic sensor** to measure distance. 
- Controlling **three LEDs (green, yellow, red)** and a **buzzer** based on distance. 
- Writing a **Python script** to handle sensor readings and activate the appropriate components. 
- Implementing a simple yet effective **proximity alert system**. 
- Testing the system for accuracy and reliability. 

**Components and Materials** 

**Component  Specification  Quantity** Raspberry Pi  Any model with GPIO pins  1 

Ultrasonic Sensor HC-SR04  1 

Green LED  5mm  4 

Yellow LED  5mm  4 

Red LED  5mm  4 

Resistors  220-ohm  12 (1 per LED) Buzzer  5V passive  1 

Breadboard  Standard size  1 

Jumper Wires  Male-to-male, Male-to-female 15-20 

**Design and Circuit Diagram** 

**Circuit Diagram** 

![](Aspose.Words.454510ee-485b-48b7-aede-953e3ec8b60c.001.png)

**Explanation of Circuit** 

- **Ultrasonic Sensor (HC-SR04):** Sends and receives ultrasonic waves to measure distance. 
- **LEDs:** Indicate different distance levels (Green - safe, Yellow - warning, Red - danger). 
- **Buzzer:** Sounds an alert when the distance crosses a predefined threshold. 
- **Resistors:** Limit the current to protect LEDs. 
- **Breadboard and Jumper Wires:** Used for easy connections without soldering. 

**Software and Code Implementation** 

**Programming Language** 

- **Python** (for easy GPIO control on Raspberry Pi) 

**Working Principle** 

**Distance Measurement** 

- The **HC-SR04 ultrasonic sensor** emits a high-frequency sound wave. 
- The wave reflects off an object and returns to the sensor. 
- The time taken for the wave to return is used to calculate distance. 

**LED Indicator Logic** 

- **Distance > 30 cm:** Only the **green LED** is ON. 
- **15 cm < Distance ≤ 30 cm:** Only the **yellow LED** is ON. 
- **5 cm < Distance ≤ 15 cm:** Only the **red LED** is ON. 
- **Distance ≤ 5 cm:** The **buzzer** is activated along with the **red LED**. 

**Testing and Results** 

**Testing Process** 

1. Place objects at different distances. 
1. Observe LED and buzzer behavior. 
1. Adjust code thresholds if necessary. 

**Results** 

- The system successfully detects distance and activates the appropriate LED. 
- The buzzer correctly triggers when an object is within **5 cm**. 
- The system performs accurately under normal conditions. 

**Applications** 

- **Proximity warning systems** (e.g., parking sensors). 
- **Obstacle detection** in robotics. 
- **Assistance for visually impaired individuals**. 

**Limitations and Future Enhancements** 

**Limitations** 

- The **sensor has a limited range (~4 meters)**. 
- Accuracy can be affected by **obstacles and environmental factors**. 

**Future Enhancements** 

- Add **multiple sensors** for **360-degree detection**. 
- Integrate **wireless alerts** (e.g., **Bluetooth or Wi-Fi notifications**). 
- Implement a **display screen** to show exact distance measurements. 

**How to Run the Project** 

1. **Set up the Raspberry Pi** with Raspbian OS. 
1. **Connect components** as per the circuit diagram. 
1. **Install dependencies** by running: 

   pip install RPi.GPIO 

4. **Run the Python script**: 

   python distance\_indicator.py 

5. **Observe the LED and buzzer behavior** based on distance measurements. 
