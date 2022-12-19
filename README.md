# Rubik's cube solver
A **3x3** rubik's cube solver made with **python** using the CFOP method (Fridrich method). It's not using any external libraries to solve the cube, all the logic is implemented using **pure python**.
<br>
Only **pygame** is used for the GUI.
<br>
The project comes with a decent amount of cases provided by the tester.py file. 

### <span style="color: cornflowerblue"> RUN
```
pip install pygame
```
```
python gui.py
```
<p float="left">
<img src="gui_utils/assets/gui_preview.png" width="490">
<img src="gui_utils/assets/terminal_solver_3.png" width="410" height="405">
</p>

 ---
    
 ### What is provided
| GUI| text-based UI | random tester | 
|:--:|:--:|:--:|
| A graphical user interface made with pygame.| A text-based interface created using pure python. | A tester which tries to solve the cube previously scrambled with a random sequence, if the cube is solved then it tries another one.
<span style="color: ; font-size: 15px;">gui.py</span>|<span style="color: ; font-size: 15px;">terminal_ui.py|<span style="color: ; font-size: 15px;">tester.py</span>


---
## <span style="color: cornflowerblue"> SOLVING PROCESS (simplified CFOP, simplified Fridrich method)

### **1. first cross**
```
white center down
for color in (red, green, orange, blue)
    center color in front
    place white-color edge in the bottom-front position
```

### **2. F2L (first two layers)**
```
for color in (blue, red, green, orange)
    center color in front
    correct corner in the top right position
    place correct corner
    place correct edge
```
### **3. last cross**
Solve the last cross according to 4 different cross' states.

### **4. OLL (orient last layer)**
Solves the cube according to 7 different cases. (OLL cross)

### **5. PLL (permute last layer)**
Solves the pll according to 21 pll cases.

### **6. rotate last layer**
Turns the last layer, the pll sometimes leaves one face to turn.


</div>
