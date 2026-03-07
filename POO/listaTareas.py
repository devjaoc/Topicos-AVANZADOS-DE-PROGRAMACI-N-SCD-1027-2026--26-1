tareas=[]
"""
tareas[0]{"tarea":ssss,"Completada":False}
tareas[1]{"tarea":2222,"Completada":False}
tareas[2]{"tarea":eee,"Completada":False}
"""
while True:
    print("1 Agregar Tarea")
    print("2 Mostrar")
    print("3 Marcar tarea como completada")
    print("4 eliminar")
    print("5 para Salir")
    opcion=input("Elige una opción: ")    
    if(opcion=="1"):
        tarea=input("Tarea : ")
        tareas.append({"tarea":tarea,"Completada":False})
    elif(opcion=="2"):
        for i,t in enumerate(tareas,start=1):
            print(str(i)+t['tarea']+" Completada")            
    elif(opcion=="3"):
        numeroTarea=input("Numero de Tarea: ")
        tareas[numeroTarea-1]['Completada']=True;
    elif(opcion=="4"):
        numeroTarea=input("Numero de Tarea a eliminar: ")
        tareas.pop(numeroTarea-1)
    elif(opcion=="5"):
        break
    else:
        print("Opción  invalida");
    
