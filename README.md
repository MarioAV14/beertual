![alt text](http://planb.com.mx/wp-content/uploads/2019/01/cropped-mxplanb.png)
<img src=http://planb.com.mx/images/image/pQR>

# Instrucciones para uso del backend 🚀
### `Registro de Bares`
Debes entrar al siguiente endpoint:
```
https://host/directorio/registros-de-bares/`
```

### `Consulta de Bares`
Para hacer una consulta referente a los bares registrados tiene que usar como elemento de busqueda en la api el slug del bar o el id del usuario, para ello debes usar la siguiete url ( recuerda sustiruir tu slug por lo que buscas o poner numero del id del usuario).
Se utiliza para entrar al detail
```
https://host/directorio/registros-de-bares/?slug=tuslug`
https://host/directorio/registros-de-bares/?iduser=idusuario`
```

### `Registro de bebidas`
Debes entrar al siguiente endpoint:
```
https://host:8000/directorio/registros-de-bebidas/`
```

### `Consulta de bebidas`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar las bebidas según el id del bar para visualizar a cual bar pertenece cada una
(recuerda que iddelbar es el numero que distingue a cada bar)
```
https://host:8000/directorio/registros-de-bebidas/?idbar=iddelbar`
```

### `Registro de ofertas`
Debes entrar al siguiente endpoint:
```
https://host/directorio/registros-de-ofertas/`
```

### `Consulta de ofertas`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar las ofertas según el id del bar para visualizar a cual bar pertenece cada una
(recuerda que iddelbar es el numero que distingue a cada bar)
```
https://host/directorio/registros-de-ofertas/?idbar=iddelbar`
```


### `Consulta de Ofertas Generales`
Debes entrar al siguiente endpoint (unicamente para consultar):
```
https://host/directorio/get-ofertas/`
```


### ` Registro de imagenes`
Debes entrar al siguiente endpoint:
```
https://host/directorio/registros-de-imagenes/`
```

### ` Consulta de imagenes`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar las imagenes según el id del bar para visualizar a cual bar pertenece cada una
(recuerda que iddelbar es el numero que distingue a cada bar)
```
https://host/directorio/registros-de-imagenes/?idbar=iddelbar`
```