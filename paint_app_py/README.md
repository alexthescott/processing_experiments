## 2 variants on a painting application

### [simple implementation](https://github.com/alexthescott/processing_experiments/paint_app_py/simple_paint_app)
circles are placed at a cursor's position when a painter clicks and drags on the sketch window. Pressing the "c" character clears the window

<img src="./simple_paint_app/simple_paint_app.gif">

### [complex implementation](https://github.com/alexthescott/processing_experiments/paint_app_py/complex_paint_app)
In the simple implementation, because circles are placed every frame, a quick mouse movement will result in dots being placed. The complex iteration addresses this issue by keeping track of the prior point, drawing a line instead of placing a circle. Pressing the "c" character clears the window

<img src="./complex_paint_app/complex_paint_app.gif">