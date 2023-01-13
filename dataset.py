from roboflow import Roboflow

def importar():

    rf = Roboflow(api_key="KOrKgmkGRHqzxP6SuKTp") #se crea la conexion

    project = rf.workspace("prueba-catzq").project("prueba-33")

    dataset = project.version(3).download("yolov8",location='datasets')
