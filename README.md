# Turnaround Maker

## Important
This Addon is No Longer Being Maintained By Me, You Are Free to Fork, Maintain, or Contribute to this.

# About Turnaround Maker

Turnaround Maker is a very simple Addon that helps you to create your turnaround. It creates an Empty that rotate (Using Drivers & Expression) and parent the active object onto it. 

![image_processing20210507-3-e2bp7m](https://user-images.githubusercontent.com/79613445/180134662-3a72a3db-d659-4874-ac7d-eb03a9179237.png)


This Addon can be find in the Add Menu (Shift - A)


## Creates Turnaround Effortlessly

It helps by turning multiple clicks into just one click, and skipping the hassle of manually setting up key frame yourself. You can choose to rotate Left or Right

![uploads_1593069488404-MakeTurnaround](https://user-images.githubusercontent.com/79613445/180135022-0ad5dc7c-f8ff-4d56-969d-84379cf08ae2.gif)

## Dynamic Rotation Speed

It also reacts to the frame range (Start & End) of the scene and can change the speed of the speed of the rotation dynamically base on the frame range in the scene to ensure seamless turnaround.

![uploads_1592458174922-dYNAMIC](https://user-images.githubusercontent.com/79613445/180135081-889c95f7-c5d0-4828-b7f7-d1bf8bb91ebb.gif)

## Choose Axis

You can now select which axis you want it to rotate. You can also choose you want it to rotate left or right. 

![uploads_1593070086491-X](https://user-images.githubusercontent.com/79613445/180135123-a2576b5b-63bf-4613-a623-f6b6ec05d1e2.gif)

![uploads_1593070095635-Y](https://user-images.githubusercontent.com/79613445/180135165-a35fe94c-2746-4db2-9be3-b60925d7fcf1.gif)

![uploads_1593070100697-Z](https://user-images.githubusercontent.com/79613445/180135187-ce0f8008-600e-49a2-a6f3-ac177f9ed03f.gif)


## Rotation Center

You have multiple choice of rotation center to choose from. 

Origin = Rotate from the object's origin point

Center = Rotate from the center of the mesh

Bottom Vertex = Rotate from the average of the lowest point vertices, or the vertex at the lowest point if there is only one. 

Bottom Center = Rotate from the Bottom of the object, but stays center at X and Y axis. 

![uploads_1593070790760-Origin](https://user-images.githubusercontent.com/79613445/180135243-48ec5373-2736-4040-9713-0065f36b4f88.png)

# Extra Utility

## Three Step Turnaround

You can create a turnaround easily with just three steps if you just want to create a simple three point lighting turnaround.

![uploads_1593069602075-1593069602075](https://user-images.githubusercontent.com/79613445/180135333-6e873012-7b16-4f7d-827d-dfddfd263bdc.png)


## Fit Camera

Create a camera in front of the selected object and making sure that the object is inside the frame. A track to constraint is added to the camera to make sure that the camera will always be aiming at the object. 

(Only works for 16:9 aspect ratio for now, the object might go out of camera if is not in 16:9)

You also instantly go into the camera view when you create a fit camera.

![uploads_1593069170697-FitCamera](https://user-images.githubusercontent.com/79613445/180135367-d153842f-3440-497c-8d57-23da8477a2fb.gif)

## Create 3  Point Light

Creates a 3 Point light system using sun lamp. It will create a light Main light, Fill Light, and Rim Light. This is useful if you just want to create a simple lighting and done with it. 

![uploads_1593069362225-tpl](https://user-images.githubusercontent.com/79613445/180135401-a3b68952-435e-4ea8-bae9-769d0a944a5a.gif)


## Aim Camera

Creates a camera that automatically aims at the selected object using track to constraints. If none is selected, an Empty will be created and that will be aimed instead

![uploads_1593069988765-AimCamera](https://user-images.githubusercontent.com/79613445/180135434-591fc2c5-7c87-449c-80dd-129cb2ff26c8.gif)

## Turnaround Camera

Creates a camera that automatically aims at the selected object using track to constraints. If none is selected, an Empty will be created and that will be aimed instead

![uploads_1593070971302-TurnaroundCamera](https://user-images.githubusercontent.com/79613445/180135472-c148669c-ac85-4f66-96b9-a3702e6a8580.gif)


