![alt text](http://planb.com.mx/wp-content/uploads/2019/01/cropped-mxplanb.png)

# Instrucciones para uso del backend 🚀
### `Registrar y consultar Bares`
Debes entrar al siguiente endpoint:
```
http://127.1.0.0:8000/directorio/registros-de-bares/`
```

Para hacer una consulta referente a los bares registrados tiene que usar como elemento de busqueda en la api el slug del bar o el id del usuario, para ello debes usar la siguiete url ( recuerda sustiruir tu slug por lo que buscas o poner numero del id del usuario)  la url del host puede cambiar.
Se utiliza para entrar al detail
```
http://127.1.0.0:8000/directorio/registros-de-bares/?slug=tuslug`
http://127.1.0.0:8000/directorio/registros-de-bares/?iduser=idusuario`
```


### `Registrar y consultar bebidas`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar las bebidas según el id del bar para visualizar a cual bar pertenece cada una
(recuerda que iddelbar es el numero que distingue a cada bar)
```
http://localhost:8000/directorio/registros-de-bebidas/?idbar=iddelbar`
```


### `SOLO registrar ofertas`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar las ofertas según el id del bar para visualizar a cual bar pertenece cada una
(recuerda que iddelbar es el numero que distingue a cada bar)
```
http://localhost:8000/directorio/registros-de-ofertas/?idbar=iddelbar`
```

### ` CONSULTAR Ofertas`
Debes entrar al siguiente endpoint (unicamente para consultar):
```
http://localhost:8000/directorio/get-ofertas/`
```


### ` Registrar imagenes`
Debes entrar al siguiente endpoint (unicamente para consultar):
Dentro de este endpoint se pueden filtrar las imagenes según el id del bar para visualizar a cual bar pertenece cada una
(recuerda que iddelbar es el numero que distingue a cada bar)
```
http://localhost:8000/directorio/registros-de-imagenes?idbar=iddelbar`
```