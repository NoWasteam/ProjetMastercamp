import torch
 
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/maayg/OneDrive/Bureau/Modele/best.pt')
 
img = "https://grist.org/wp-content/uploads/2017/08/ocean-plastic.jpg"
 
results = model(img)
 
results.print()
results.show()
