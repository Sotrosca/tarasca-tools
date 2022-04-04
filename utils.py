def simular_inversion(monto_inicial, meses, tna, agregar_monto_inicial_por_mes=True, inflacion_mensual=0.035):
    '''
    Simula una inversion de un monto en una cantidad de meses.
    @param monto_inicial: monto inicial de la inversión
    @param meses: cantidad de meses a simular
    @param tna: tasa nominal anual de la inversion
    @param agregar_monto_inicial_por_mes: si es True, agrega el monto inicial recalculado por inflacion a la inversion por mes
    @param inflacion_mensual: inflacion mensual
    @return: lista con la tenencia de la inversion por mes y lista con los montos aportados por mes en la inversion
    '''
    interes = tna / 12
    montos_agregados = []
    if agregar_monto_inicial_por_mes:
        tenencia_por_mes = [monto_inicial]
        montos_agregados = [monto_inicial]
        monto_auxiliar = tenencia_por_mes[-1]
        for i in range(1, meses + 1):
            monto_agregado = monto_inicial * (1 + inflacion_mensual) ** i
            monto_aumentado = (monto_auxiliar + monto_agregado)
            montos_agregados.append(monto_agregado)
            tenencia_por_mes.append(monto_aumentado * (1 + interes))
            monto_auxiliar = tenencia_por_mes[-1]
    else:
        tenencia_por_mes = [monto_inicial * (1 + interes) ** i for i in range(0, meses + 1)]
        montos_agregados = [0 for i in range(0, meses)]
    
    return tenencia_por_mes, montos_agregados

def calcular_precio_con_inflacion(precio, meses, inflacion_mensual):
    '''
    Calcula el precio de un activo que se ajusta a la inflacion mensual luego de una cantidad de meses.
    @param precio: precio inicial del activo
    @param meses: cantidad de meses a ajustar
    @param inflacion_mensual: inflacion mensual
    @return: lista con el precio del activo ajustado por mes
    '''
    precio_recalculado_por_mes = [precio * (1 + inflacion_mensual) ** i for i in range(0, meses + 1)]
    return precio_recalculado_por_mes    
