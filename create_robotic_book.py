import streamlit as st
import textwrap
from datetime import datetime

PAGE_WIDTH = 80
WRAP = textwrap.fill

def wrap(text):
    return WRAP(text, width=PAGE_WIDTH)

def header(title):
    line = "=" * PAGE_WIDTH
    return f"{line}\n{title.center(PAGE_WIDTH)}\n{line}\n"

def chapter_title(num, title):
    return f"\n\nCHAPTER {num}: {title}\n" + ("-" * PAGE_WIDTH) + "\n"

def build_content():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    intro = header("Robotic Humanoid: Complete Step-by-Step Guide")
    intro += wrap(
        f"This book teaches you how to build a humanoid robot in simple English. "
        f"Useful for hackathons and beginners. Generated on: {now}.\n"
    )

    intro += "\nTable of Contents:\n" + "\n".join([
        "1. Planning & Concept",
        "2. Parts, Components & Full Price List (PKR)",
        "3. Mechanical Design & DOF",
        "4. Electronics & Wiring",
        "5. Software & Control System",
        "6. Integration & Testing",
        "7. Advanced Features (Vision, AI, Balance)",
        "8. Hackathon Strategy",
        "9. Troubleshooting Guide",
        "10. Resources & Next Steps"
    ]) + "\n\n"

    # CHAPTER 1
    c1 = chapter_title(1, "Planning & Concept")
    c1 += wrap(
        "Before building a humanoid robot, define a clear purpose. "
        "Begin with small goals for hackathons because time is short. "
        "Decide what the robot must do: walk, wave, talk, detect faces, etc."
    )

    c1 += "\n\n" + wrap("Important decisions:")
    c1 += "\n - Robot size"
    c1 += "\n - Weight limit"
    c1 += "\n - Skill level of team"
    c1 += "\n - Hackathon time"
    c1 += "\n - Budget (PKR based)"

    # CHAPTER 2 — PKR PRICE LIST
    c2 = chapter_title(2, "Parts, Components & Full Price List (PKR)")

    c2 += wrap("Below are parts needed to build a humanoid robot with PKR prices (2025).")

    # Mechanical
    c2 += "\n\nMechanical Structure:"
    c2 += "\n - Aluminum frame: 8,000 – 25,000 PKR"
    c2 += "\n - 3D printed body parts: 5,000 – 20,000 PKR"
    c2 += "\n - Screws, brackets, joints: 1,500 – 6,000 PKR"
    c2 += "\n - Bearings: 500 – 4,000 PKR"

    # Motors
    c2 += "\n\nMotors / Actuators:"
    c2 += "\n - Standard servos: 1,200 – 3,500 PKR each"
    c2 += "\n - High torque servos: 6,000 – 25,000 PKR each"
    c2 += "\n - Brushless motors: 8,000 – 35,000 PKR"
    c2 += "\n - PCA9685 servo driver: 1,000 – 2,500 PKR"

    # Electronics
    c2 += "\n\nElectronics & Sensors:"
    c2 += "\n - Raspberry Pi 4/5: 18,000 – 40,000 PKR"
    c2 += "\n - Arduino / ESP32: 1,000 – 3,500 PKR"
    c2 += "\n - IMU sensor: 1,000 – 7,000 PKR"
    c2 += "\n - Raspberry Pi Camera: 3,000 – 10,000 PKR"
    c2 += "\n - Motor Drivers: 700 – 3,000 PKR"

    # Power System
    c2 += "\n\nPower System:"
    c2 += "\n - LiPo Battery: 4,000 – 12,000 PKR"
    c2 += "\n - Battery Charger: 1,500 – 4,000 PKR"
    c2 += "\n - Voltage Regulators: 500 – 2,000 PKR"

    # Tools
    c2 += "\n\nTools Required:"
    c2 += "\n - Soldering Kit: 2,000 – 4,500 PKR"
    c2 += "\n - Multimeter: 1,200 – 3,000 PKR"
    c2 += "\n - Screwdriver Set: 500 – 1,500 PKR"
    c2 += "\n - Wires, heat shrink: 300 – 1,200 PKR"

    # Total Cost
    c2 += "\n\nApprox Total Cost:"
    c2 += "\n - Small humanoid: 30,000 – 80,000 PKR"
    c2 += "\n - Medium humanoid: 80,000 – 250,000 PKR"
    c2 += "\n - Large humanoid: 250,000 – 2,000,000+ PKR"

    # CHAPTER 3
    c3 = chapter_title(3, "Mechanical Design & DOF")
    c3 += wrap(
        "Mechanical design controls movement. Humanoids use joints called DOF (Degrees of Freedom)."
    )
    c3 += "\n\nRecommended DOF for beginners:"
    c3 += "\n - Head: 1–2 DOF"
    c3 += "\n - Arms: 2 DOF each"
    c3 += "\n - Torso: 1 DOF"

    # CHAPTER 4
    c4 = chapter_title(4, "Electronics & Wiring")
    c4 += wrap("Electronics connect motors, sensors and battery power safely.")

    # CHAPTER 5
    c5 = chapter_title(5, "Software & Control System")
    c5 += wrap("Python + Arduino is the best combination for humanoid robots.")

    # CHAPTER 6
    c6 = chapter_title(6, "Integration & Testing")
    c6 += wrap("Integration means combining mechanical, electronics and software systems.")

    # CHAPTER 7
    c7 = chapter_title(7, "Advanced Features")
    c7 += wrap("Add AI once the robot's basic movement is stable.")

    # CHAPTER 8
    c8 = chapter_title(8, "Hackathon Strategy")
    c8 += wrap("Hackathons need speed, teamwork and smart presentation.")

    # CHAPTER 9
    c9 = chapter_title(9, "Troubleshooting Guide")
    c9 += wrap("Common problems and simple fixes.")

    # CHAPTER 10
    c10 = chapter_title(10, "Resources & Next Steps")
    c10 += wrap("Continue learning robotics, AI, electronics and CAD modeling.")

    notes = "\n\n" + "=" * PAGE_WIDTH + "\nFinal Notes\n" + "=" * PAGE_WIDTH + "\n"
    notes += wrap("This is the Streamlit book version. You can download it below.")

    return intro + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + notes


# ---------------- STREAMLIT UI ----------------

st.title("🤖 Robotic Humanoid Book Generator (Streamlit Version)")

content = build_content()

st.text_area("Generated Humanoid Book:", content, height=600)

st.download_button(
    label="📥 Download Book as TXT",
    data=content,
    file_name="Robotic_Humanoid_Book.txt",
    mime="text/plain"
)

st.success("Book generated successfully!")














