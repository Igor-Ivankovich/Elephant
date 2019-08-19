# How to start

Run the program main.py, a file with input values and a file for output are used as parameters.

        $ python main.py input.txt output.txt                
        
# How to change color

In the file constant.py sets the desired colors (characters) for drawing:

```python
    LINE_CHARACTER = 'x'
    RECTANGLE_CHARACTER = 'x'
```
# How it works

#### Drawing lines:

    Horizontal:
    
        The line is found at the given coordinates, we loop through it and is drawn when the
        condition is true: `if x1 <= index <= x2 (i.e. in the interval where the horizontal
        line should be) where x1,x2 - given coordinates;index - current position in line:
```python
    for index in range(len(self.field[y1])):
      if x1 <= index <= x2:
        self.field[y1] = ''.join((
             self.field[y1][:index],
             self.character,
             self.field[y1][index + 1:])
```
    Vertical:
    
        Goes through all the lines and is drawn when the conditions are true: `if y1 <= index <= y2
        ` (i.e. in the interval where the vertical line should be) where y1,y2 - given coordinates;
        index - current position in line:
        
```python
    for index in range(len(self.field)):
      if y1 <= index <= y2:
        self.field[index] = ''.join((self.field[index][:x1],
             self.character,
             self.field[index][x1 + 1:]))
```

#### Drawing rectangle:
    
    To draw a rectangle, code is used that draws vertical and horizontal lines.
   
#### Bucket fill:

    On the line given by coordinates, those places are painted over that fall into the list when passing
    through the line and fulfilling the conditions:

```python
        for index, value in enumerate(self.field[y][1:-1]):
            if self.valid(value):
                empty_place_index.append(index+1)
            elif index+1 < x:
                empty_place_index.clear()
            elif index+1 > x:
                break
```
    Going down  and up, recursively repeat the previous operation.
