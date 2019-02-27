import ast 
import csv 
import sys 
import math 
import os 


def cargar_csv_al_header_datos(nombrearchivo):
    ruta_archivo = os.path.join(os.getcwd(), nombrearchivo)
    sistemadearchivo = csv.reader(open(ruta_archivo, newline='\n'))

    toda_fila = []
    for r in sistemadearchivo:
        toda_fila.append(r)

    headers = toda_fila[0]
    idx_al_nombre, nombre_al_idx = get_header_nombre_al_idx_maps(headers)

    datos = {
        'header': headers,
        'rows': toda_fila[1:],
        'nombre_al_idx': nombre_al_idx,
        'idx_al_nombre': idx_al_nombre
    }
    return datos


def get_header_nombre_al_idx_maps(headers):
    nombre_al_idx = {}
    idx_al_nombre = {}
    for i in range(0, len(headers)):
        nombre_al_idx[headers[i]] = i
        idx_al_nombre[i] = headers[i]
    return idx_al_nombre, nombre_al_idx


def columnas_del_proyecto(datos, columns_to_project):
    datos_h = list(datos['header'])
    datos_r = list(datos['rows'])

    all_cols = list(range(0, len(datos_h)))

    columns_to_project_ix = [datos['nombre_al_idx'][name] for name in columns_to_project]
    columns_to_remove = [cidx for cidx in all_cols if cidx not in columns_to_project_ix]

    for delc in sorted(columns_to_remove, reverse=True):
        del datos_h[delc]
        for r in datos_r:
            del r[delc]

    idx_al_nombre, nombre_al_idx = get_header_nombre_al_idx_maps(datos_h)

    return {'header': datos_h, 'rows': datos_r,
            'nombre_al_idx': nombre_al_idx,
            'idx_al_nombre': idx_al_nombre}


def obten_valores_unicos(datos):
    idx_al_nombre = datos['idx_al_nombre']
    idxs = idx_al_nombre.keys()

    val_map = {}
    for idx in iter(idxs):
        val_map[idx_al_nombre[idx]] = set()

    for datos_row in datos['rows']:
        for idx in idx_al_nombre.keys():
            att_name = idx_al_nombre[idx]
            val = datos_row[idx]
            if val not in val_map.keys():
                val_map[att_name].add(val)
    return val_map


def obten_etiquetas_datos(datos, atributo_objetivo):
    rows = datos['rows']
    col_idx = datos['nombre_al_idx'][atributo_objetivo]
    etiquetas = {}
    for r in rows:
        val = r[col_idx]
        if val in etiquetas:
            etiquetas[val] = etiquetas[val] + 1
        else:
            etiquetas[val] = 1
    return etiquetas


def entropia(n, etiquetas):
    ent = 0
    for etiqueta in etiquetas.keys():
        p_x = etiquetas[etiqueta] / n
        ent += - p_x * math.log(p_x, 2)
    return ent


def particion_datos(datos, group_att):
    particiones = {}
    datos_rows = datos['rows']
    particion_att_idx = datos['nombre_al_idx'][group_att]
    for row in datos_rows:
        row_val = row[particion_att_idx]
        if row_val not in particiones.keys():
            particiones[row_val] = {
                'nombre_al_idx': datos['nombre_al_idx'],
                'idx_al_nombre': datos['idx_al_nombre'],
                'rows': list()
            }
        particiones[row_val]['rows'].append(row)
    return particiones


def promedio_entropia_w_particiones(datos, splitting_att, atributo_objetivo):
    # find uniq values of splitting att
    datos_rows = datos['rows']
    n = len(datos_rows)
    particiones = particion_datos(datos, splitting_att)

    promedio_ent = 0

    for particion_key in particiones.keys():
        particioned_datos = particiones[particion_key]
        particion_n = len(particioned_datos['rows'])
        particion_etiquetas = obten_etiquetas_datos(particioned_datos, atributo_objetivo)
        particion_entropia = entropia(particion_n, particion_etiquetas)
        promedio_ent += particion_n / n * particion_entropia

    return promedio_ent, particiones


def most_common_etiqueta(etiquetas):
    mcl = max(etiquetas, key=lambda k: etiquetas[k])
    return mcl


def id3(datos, uniqs, restantes_atributos, atributo_objetivo):
    etiquetas = obten_etiquetas_datos(datos, atributo_objetivo)

    node = {}

    if len(etiquetas.keys()) == 1:
        node['etiqueta'] = next(iter(etiquetas.keys()))
        return node

    if len(restantes_atributos) == 0:
        node['etiqueta'] = most_common_etiqueta(etiquetas)
        return node

    n = len(datos['rows'])
    ent = entropia(n, etiquetas)

    max_info_ganancia = None
    max_info_ganancia_att = None
    max_info_ganancia_particiones = None

    for restantes_att in restantes_atributos:
        promedio_ent, particiones = promedio_entropia_w_particiones(datos, restantes_att, atributo_objetivo)
        info_ganancia = ent - promedio_ent
        if max_info_ganancia is None or info_ganancia > max_info_ganancia:
            max_info_ganancia = info_ganancia
            max_info_ganancia_att = restantes_att
            max_info_ganancia_particiones = particiones

    if max_info_ganancia is None:
        node['etiqueta'] = most_common_etiqueta(etiquetas)
        return node

    node['attribute'] = max_info_ganancia_att
    node['nodes'] = {}

    restantes_atributos_for_subarboles = set(restantes_atributos)
    restantes_atributos_for_subarboles.discard(max_info_ganancia_att)

    valor_unico_atributos = uniqs[max_info_ganancia_att]

    for valor_atributos in valor_unico_atributos:
        if valor_atributos not in max_info_ganancia_particiones.keys():
            node['nodes'][valor_atributos] = {'etiqueta': most_common_etiqueta(etiquetas)}
            continue
        particion = max_info_ganancia_particiones[valor_atributos]
        node['nodes'][valor_atributos] = id3(particion, uniqs, restantes_atributos_for_subarboles, atributo_objetivo)

    return node


def cargar_configuracion(archivo_configuracion):
    with open(archivo_configuracion, 'r') as myfile:
        datos = myfile.read().replace('\n', '')
    return ast.literal_eval(datos)


def imprimir_arbol_bonito(raiz):
    stack = []
    reglas = set()

    def atravesar(node, stack, reglas):
        if 'etiqueta' in node:
            stack.append(' entonces ' + node['etiqueta'])
            reglas.add(''.join(stack))
            stack.pop()
        elif 'attribute' in node:
            ifnd = 'Si ' if not stack else ' y '
            stack.append(ifnd + node['attribute'] + ' es igual a ')
            for subnode_key in node['nodes']:
                stack.append(subnode_key)
                atravesar(node['nodes'][subnode_key], stack, reglas)
                stack.pop()
            stack.pop()

    atravesar(raiz, stack, reglas)
    print(os.linesep.join(reglas))


def main():
    print ("CLASIFICACION ID3 ")
    argv = sys.argv
    print("Argumentos de la linea de comandos son {}: ".format(argv))

    config = cargar_configuracion(argv[1])

    datos = cargar_csv_al_header_datos(config['archivo_datos'])
    datos = columnas_del_proyecto(datos, config['datos_columnas_del_proyecto'])
    
    atributo_objetivo = config['atributo_objetivo']
    
    restantes_attributes = set(datos['header'])
    restantes_attributes.remove(atributo_objetivo)

    uniqs = obten_valores_unicos(datos)

    raiz = id3(datos, uniqs, restantes_attributes, atributo_objetivo)

    imprimir_arbol_bonito(raiz)


if __name__ == "__main__": main()
