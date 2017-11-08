def distanceBLOB(blobs,central): #inserta blobD e indice de el blob a investigar (lo ultimo le da flexibilidad para el futuro)
    distcenter = np.sqrt(((blobs[0]-central[0])**2)+((blobs[1]-central[1])**2))
    plt.plot([central[1],blobs[1]],[central[0],blobs[0]],hold = True)
    return distcenter

#IMPORTANTE, ESTE CODIGO NO CONSIDERARA CADA UNA DE NUESTRAS IMAGENES COMO DISTINTAS, NUESTRO RADIO ES DISTINTO PARA
#CADA IMAGEN, NUESTRAS DISTANCIAS SON "DISTINTAS" PARA CADA IMAGEN Y ESO ES LO QUE CORRELACIONAMOS PARA CADA INTENTO
#DEL EXPERIMENTO, POR LO CUAL FLUOPI, QUE USA TIMELAPSES, PARA --LAS MISMAS PLACAS-- NO NOS SIRVE.

distcen = []
radius = r_fit
plt.figure(figsize=(8,8))
i = 0

for element in blobD:
    i += 1
    central = 12 #por ejemplo
    distances = distanceBLOB(element,blobD[central])
    distrad.append([distances,radius[i], radius[central],len(blobD)]) #distrad es [distancia,radiosatelite,radiocentral,numerodeblobs] 
    avdist += distances/len(blobD)
    avrad +=radius[central]/len(blodD)
    
for element in distrad:
    xi,xp = element[2],avdrad
    yi,yp = element[0],avdist
    aux1, aux2, aux3 += (xi-xp)*(yi-yp),np.sqrt((xi-xp)**2)),np.sqrt((yi-yp)**2)
    
correlation = aux1/(aux2*aux3)
#aca tenemos una correlacion para 1 n, luego lo hacemos para multiples n y graficamos n versus correlacion, encon-
#trando como varia el crecimiento de las baterias dependiendo del numero de bacterias satelites
#Ademas si la curva es bonita, podemos modelarle una curva y asi predecir para cualquier n y aplicarlo a cualquier
#muestra y cualquier colonia centrar.

plt.imshow(sDatSall, cmap='gray',hold = True)
plt.show()
print(distcen)
