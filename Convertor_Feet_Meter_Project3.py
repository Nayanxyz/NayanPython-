from Convertor_Feet_Meter import convert

import FreeSimpleGUI as g

g.theme("GreenMono")

label = g.Text("Convertor_Feet_Meter")

enter_feet = g.Text("Enter Feet")
feet_input = g.InputText(tooltip="Enter Feet", key="feet")


enter_inch = g.Text("Enter Inches")
inch_input = g.InputText(tooltip="Enter Inches",key="inches")

convert_button = g.Button("Convert")

exit_button = g.Button("Exit")

meter_text = g.Text(key="output", text_color="Black")

window = g.Window("Convertor",layout=[[label], [enter_feet, feet_input],
                                      [enter_inch, inch_input],[convert_button, exit_button, meter_text]],
                    font=['Helvetica',12])

while True:
    event , values = window.read()
    if event == g.WIN_CLOSED:
        break
    if event == "Convert":

        feet = values["feet"]
        inches = values["inches"]

        result = convert(feet,inches)
        window["output"].update(value=f"{result} Meters")
    if event=="Exit":
        break

window.close()