#todo; construir todo fluxo de fitros sobre determinados endpoints.

def normalize_path_params(cidade=None,
                          estrelas_min = 0,
                          estrelas_max = 10,
                          diaria_min = 0,
                          diaria_max = 10000,
                          limit = 50,
                          offset = 0, **dados):
    if cidade:
        return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'cidade': cidade,
            'limit': limit,
            'offset': offset}
    return {
        'estrelas_min': estrelas_min,
        'estrelas_max': estrelas_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'limit': limit,
        'offset': offset}



consulta_sem_carga = "SELECT * FROM motoristas \
WHERE (estrelas >= ? and estrelas <= ?) \
and (diaria >= ? and diaria <= ?) \
LIMIT ? OFFSET ?"

consulta_com_carga = "SELECT * FROM motoristas \
WHERE (estrelas >= ? and estrelas <= ?) \
and (diaria >= ? and diaria <= ?) \
and cidade = ? LIMIT ? OFFSET ?"

