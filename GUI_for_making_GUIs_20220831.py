# -*- coding: utf-8 -*-
"""
Title:
GUI for making GUIs

Purpose:
Many python codes do not have a GUI and are less accessible to people unfamiliar 
with the programming language. 
This code allows people with almost no python experience to create their own GUI 
and add it to their code.

Author Information:
Harry Dempsey
Research assistant
Department of Physiology
Monash University, Clayton
Andrews lab and Foldi lab
https://github.com/H-Dempsey
harry.dempsey@monash.edu

About the labs:
The Andrews lab investigates how the brain senses and responds to hunger.
The Foldi lab investigates the biological underpinnings of anorexia nervosa and feeding disorders.
https://www.monash.edu/discovery-institute/andrews-lab
https://www.monash.edu/discovery-institute/foldi-lab
"""

# Type 'pip install PySimpleGUI' into the console.
# If you have done this once, you do not need to do it again.
# This script makes a GUI code, which you can copy onto the start of another code.
# Click run and follow the instructions in the GUI.

import PySimpleGUI as sg


# GUI 1: CHOOSE HOW MANY INPUT TYPES.


sg.theme("DarkTeal2")
title = "Choose the number of input types."
layout = [
    [sg.T("")], [sg.Text("How many import or export browsers?"), 
                 sg.Combo(list(range(0,15+1)),default_value=0,key="Import",enable_events=True)],
    [sg.T("")], [sg.Text("How many text entries?"), 
                 sg.Combo(list(range(0,15+1)),default_value=0,key="Text",enable_events=True)],
    [sg.T("")], [sg.Text("How many number entries?"), 
                 sg.Combo(list(range(0,15+1)),default_value=0,key="Num",enable_events=True)],
    [sg.T("")], [sg.Text("How many checkboxes?"), 
                 sg.Combo(list(range(0,15+1)),default_value=0,key="Checkboxes",enable_events=True)],
    [sg.T("")], [sg.Text("How many dropdown menus?"), 
                 sg.Combo(list(range(0,15+1)),default_value=0,key="Dropdown",enable_events=True)],
    [sg.T("")], [sg.Button("Submit")]
         ]
window = sg.Window(title, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        window.close()
        exit()
    elif event == "Submit":
        tot_import_export_folders = values["Import"]
        tot_text_entries = values["Text"]
        tot_number_entries = values["Num"]
        tot_checkboxes = values["Checkboxes"]
        tot_lists = values["Dropdown"]
        window.close()
        break
    
    
# GUI 2: FILL IN THE INFORMATION ABOUT EACH INPUT.
    

sg.theme("DarkTeal2")
layout = []
title = "Fill in information about each input."
types_data = ["Text", "Numbers (integer)", "Numbers (decimal)", "True or False"]
list_keys = []
column1_size = (17,1)
column2_size = (13,1)
column3_size = (45,1)
column4_size = (15,1)

for i in range(tot_import_export_folders):
    layout += [[sg.T("")],
        [sg.Text("Import or export line " + str(i+1),size=column1_size), 
         sg.Text("Display text",size=column2_size), 
         sg.Input(default_text="Choose a folder for the import or export location",key="Import"+str(i),enable_events=True),
         sg.Text("Type of data",size=column2_size), 
         sg.Combo(types_data,default_value="Text",key="Type Import"+str(i),enable_events=True)],
        [sg.Text("",size=column1_size), sg.Text("Default value",size=column2_size), 
         sg.Input(default_text="/Users/hazza/Desktop/Import",key="Default Import"+str(i),enable_events=True),
         sg.Text("Variable name",size=column2_size), 
         sg.Input(default_text="import_location"+str(i),key="Variable Import"+str(i),enable_events=True)]]
    list_keys.append("Import"+str(i))
    
for i in range(tot_text_entries):
    layout += [[sg.T("")],
        [sg.Text("Text entry line " + str(i+1),size=column1_size), 
         sg.Text("Display text",size=column2_size), 
         sg.Input(default_text="Behaviour name",key="Text"+str(i),enable_events=True),
         sg.Text("Type of data",size=column2_size), 
         sg.Combo(types_data,default_value="Text",key="Type Text"+str(i),enable_events=True)],
        [sg.Text("",size=column1_size),sg.Text("Default value",size=column2_size), 
         sg.Input(default_text="Walking",key="Default Text"+str(i),enable_events=True),
         sg.Text("Variable name",size=column2_size), 
         sg.Input(default_text="text"+str(i),key="Variable Text"+str(i),enable_events=True)]]
    list_keys.append("Text"+str(i))

for i in range(tot_number_entries):
    layout += [[sg.T("")],
        [sg.Text("Number entry line " + str(i+1),size=column1_size),
         sg.Text("Display text",size=column2_size), 
         sg.Input(default_text="Number of behaviours",key="Num"+str(i),enable_events=True),
         sg.Text("Type of data",size=column2_size), 
         sg.Combo(types_data,default_value="Numbers (integer)",key="Type Num"+str(i),enable_events=True)],
        [sg.Text("",size=column1_size),sg.Text("Default value",size=column2_size),
         sg.Input(default_text="5",key="Default Num"+str(i),enable_events=True),
         sg.Text("Variable name",size=column2_size),
         sg.Input(default_text="number"+str(i),key="Variable Num"+str(i),enable_events=True)]]
    list_keys.append("Num"+str(i))
    
for i in range(tot_checkboxes):
    layout += [[sg.T("")],
        [sg.Text("Checkbox line " + str(i+1),size=column1_size),
         sg.Text("Display text",size=column2_size),
         sg.Input(default_text="Find overlap with a zone",key="Checkbox"+str(i),enable_events=True),
         sg.Text("Type of data",size=column2_size),
         sg.Combo(types_data,default_value="True or False",key="Type Checkbox"+str(i),enable_events=True)],
        [sg.Text("",size=column1_size),sg.Text("Default value",size=column2_size),
         sg.Input(default_text="True",key="Default Checkbox"+str(i),enable_events=True),
         sg.Text("Variable name",size=column2_size), 
         sg.Input(default_text="checkbox"+str(i),key="Variable Checkbox"+str(i),enable_events=True)]]
    list_keys.append("Checkbox"+str(i))
    
for i in range(tot_lists):
    layout += [[sg.T("")],
        [sg.Text("Dropdown line " + str(i+1),size=column1_size),
         sg.Text("Display text",size=column2_size),
         sg.Input(default_text="Number of zones",key="List"+str(i),enable_events=True),
         sg.Text("Type of data",size=column2_size),
         sg.Combo(types_data,default_value="Numbers (integer)",key="Type List"+str(i),enable_events=True)],
        [sg.Text("",size=column1_size),sg.Text("Default value",size=column2_size),
         sg.Input(default_text="5",key="Default List"+str(i),enable_events=True),
         sg.Text("Variable name",size=column2_size),
         sg.Input(default_text="list"+str(i),key="Variable List"+str(i),enable_events=True)],
        [sg.Text("",size=column1_size), sg.Text("Dropdown items",size=column2_size),
         sg.Input(default_text="1, 2, 3, 4, 5, 6, 7, 8, 9",key="Items List"+str(i),enable_events=True)]]
    list_keys.append("List"+str(i))

layout += [[sg.T("")],[sg.Button("Submit")]]
window = sg.Window(title, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        window.close()
        exit()
    elif event == "Submit":
        window.close()
        break
    
    
# GUI 3: PREVIEW THE GUI.


def boolean(value):
    if value == 'True':
        return(True)
    elif value == 'False':
        return(False)
    else:
        return(value)
sg.theme("DarkTeal2")
input_type = {"Text":str,"Numbers (integer)":int,"Numbers (decimal)":float,"True or False":boolean}
# Create a dictionary that stores the input type, display text, default value and 
# variable name for each line in the GUI.
layout = {}
for key in list_keys:
    layout[key, "input type"] = input_type[values["Type "+key]]
    layout[key, "display text"] = values[key]
    layout[key, "default value"] = layout[key, "input type"](values["Default "+key])
    layout[key, "variable name"] = values["Variable "+key]
    if "List" in key:
        temp_list = (values["Items "+key]).split(",")
        temp_list = [item.strip() for item in temp_list]
        for i in range(len(temp_list)):
            temp_list[i] = layout[key, "input type"](temp_list[i])
        layout[key, "dropdown list"] = temp_list

GUI = []
title = "Preview the GUI you have made."

for key_word in list_keys:
    if "Import" in key_word:
        GUI += [[sg.T("")], [sg.Text(layout[key_word, "display text"]),
                 sg.Input(default_text=layout[key_word, "default value"],key=key_word,enable_events=True),sg.FolderBrowse()]]
    elif "Text" in key_word:
        GUI += [[sg.T("")], [sg.Text(layout[key_word, "display text"]),
                 sg.Input(default_text=layout[key_word, "default value"],key=key_word,enable_events=True)]]
    elif "Num" in key_word:
        GUI += [[sg.T("")], [sg.Text(layout[key_word, "display text"]),
                 sg.Input(default_text=layout[key_word, "default value"],key=key_word,enable_events=True)]]
    elif "Checkbox" in key_word:
        GUI += [[sg.T("")], [sg.Text(layout[key_word, "display text"]),
                 sg.Checkbox('',default=layout[key_word, "default value"],key=key_word,enable_events=True)]]
    elif "List" in key_word:
        GUI += [[sg.T("")], [sg.Text(layout[key_word, "display text"]),
                 sg.Combo(layout[key_word, "dropdown list"],default_value=str(layout[key_word, "default value"]),key=key_word,enable_events=True)]]

GUI += [[sg.T("")],[sg.Button("Submit")]]
window = sg.Window(title, GUI)
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        window.close()
        exit()
    elif event == "Submit":
        window.close()
        break


# GUI 4: PRESENT THE CODE TO BE COPIED.


sg.theme("DarkTeal2")
title = "Copy this GUI script to the start of your code and then quit."
GUI = [[sg.Text("DO NOT quit this window until you have pasted the code.")],
       [sg.MLine(key='Multiline'+sg.WRITE_ONLY_KEY, size=(700,700))]]
GUI += [[sg.T("")],[sg.Button("Exit")]]
window = sg.Window(title, GUI, size=(800,400), finalize=True)

# Start printing the code.
window['Multiline'+sg.WRITE_ONLY_KEY].print("# Create a layout with information for the GUI.")
printed_layout = str(layout)
printed_layout = printed_layout.replace(r"<class 'str'>",'str').replace(r"<class 'bool'>",'bool')
printed_layout = printed_layout.replace(r"<class 'int'>",'int').replace(r"<class 'float'>",'float')
# Now replace '<function boolean at 0x...>' with 'bool'.
phrases_indices = []
look_for_greater_sign = False
for i in range(len(printed_layout)):
    if printed_layout[i:i+23] == '<function boolean at 0x':
        phrases_indices.append([i,'end'])
        look_for_greater_sign = True
    elif printed_layout[i] == '>' and look_for_greater_sign == True:
        phrases_indices[-1][-1] = i
        look_for_greater_sign = False
function_outputs = [printed_layout[pair[0]:pair[1]+1] for pair in phrases_indices]
for output in function_outputs:
    printed_layout = printed_layout.replace(output,'bool')
window['Multiline'+sg.WRITE_ONLY_KEY].print("layout=",printed_layout)
window['Multiline'+sg.WRITE_ONLY_KEY].print("list_keys=",list_keys)
window['Multiline'+sg.WRITE_ONLY_KEY].print("GUI_title=","'GUI'")
window['Multiline'+sg.WRITE_ONLY_KEY].print(
"""
import PySimpleGUI as sg
sg.theme("DarkTeal2")

# Create the GUI.
GUI = []
for key_word in list_keys:
    if "Import" in key_word:
        GUI += [[sg.T("")],[sg.Text(layout[key_word, "display text"]),
                 sg.Input(default_text=layout[key_word, "default value"],
                          key=key_word,enable_events=True), sg.FolderBrowse()]]
    elif "Text" in key_word:
        GUI += [[sg.T("")],[sg.Text(layout[key_word, "display text"]),
                 sg.Input(default_text=layout[key_word, "default value"],
                          key=key_word,enable_events=True)]]
    elif "Num" in key_word:
        GUI += [[sg.T("")],[sg.Text(layout[key_word, "display text"]),
                 sg.Input(default_text=layout[key_word, "default value"],
                          key=key_word,enable_events=True)]]
    elif "Checkbox" in key_word:
        GUI += [[sg.T("")],[sg.Text(layout[key_word, "display text"]),
                 sg.Checkbox('',default=layout[key_word, "default value"],
                             key=key_word,enable_events=True)]]
    elif "List" in key_word:
        GUI += [[sg.T("")],[sg.Text(layout[key_word, "display text"]),
                 sg.Combo(layout[key_word, "dropdown list"],
                          default_value=str(layout[key_word, "default value"]),
                          key=key_word,enable_events=True)]]
GUI += [[sg.T("")],[sg.Button("Submit")]]
window = sg.Window(GUI_title, GUI)

# Update the values.
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        window.close()
        exit()
    elif event == "Submit":
        window.close()
        break
    
inputs = {}
for key_word in list_keys:
    inputs[key_word] = layout[key_word, "input type"](values[key_word])
"""
)
window['Multiline'+sg.WRITE_ONLY_KEY].print("# Assign the inputs to the variables.")
for key in list_keys:
    if "Import" in key:
        window['Multiline'+sg.WRITE_ONLY_KEY].print(
            layout[key,"variable name"]+" = "+r"inputs['"+str(key)+r"']"+r" + '/'"
            +" # "+layout[key,'display text'])
    else:
        window['Multiline'+sg.WRITE_ONLY_KEY].print(
            layout[key,"variable name"]+" = "+r"inputs['"+str(key)+r"']"+" # "
            +layout[key,'display text'])
        
window['Multiline'+sg.WRITE_ONLY_KEY].print(
"""
# Verify the inputs by printing them in the console.
print("Verify the inputs from the GUI:")
print("")
for key in list_keys:
    print(layout[key,"variable name"],'is',inputs[key],"("+layout[key,"display text"]+")")
"""
)
# Finish printing the code.
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        window.close()
        exit()
    elif event == "Submit":
        window.close()
        break