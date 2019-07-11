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


#todo; /* origem e destino do caminhoneiro*/
caminhoneiro_origem_destino ="""SELECT
                                    mo.nome,
                                    lc.origem,
                                    lc.destino,
                                    lc.latitude,
                                    lc.longitude	
                                FROM motoristas mo
                                INNER JOIN local_carga lc ON lc.motorista_id = mo.motorista_id
                                WHERE 
                                lc.origem IS NOT NULL 
                                AND ( lc.origem !=''  AND( lc.destino IS NOT NULL ) AND (lc.destino !=''))"""

#todo;  /*motoristas que não possuem carga para voltar ao seu local de origem*/
caminhoneiro_sem_carga ="""SELECT 
                            mo.nome nome,
                            mo.sexo sexo,
                            mo.rg rg,
                            lc.origem origem
                        FROM motoristas mo
                        LEFT JOIN local_carga lc ON lc.motorista_id = mo.motorista_id
                        WHERE 
                        lc.origem IS NULL 
                        OR (
                        lc.origem ='' )"""


#todo; /* caminhoneiros com veiculo proprio*/
caminhoneiro_possue_veiculo_proprio="""SELECT * FROM motoristas
                                    WHERE possueveiculoproprio ='true'"""


#todo; /* listagem de origem e destino agrupado por tipos */
listagem_origem_destino="""SELECT DISTINCT 
                                mo.nome nome,
                                lc.origem origem,
                                lc.destino destino,
                                tpv.modal modal
                            FROM motoristas mo
                            INNER JOIN local_carga lc ON lc.motorista_id = mo.motorista_id
                            LEFT JOIN veiculo v ON v.motorista_id = mo.motorista_id
                            INNER JOIN tipo_veiculo tpv ON tpv.veiculo_id = v.veiculo_id
                            WHERE 
                            lc.origem IS NOT NULL 
                            AND(lc.origem !='' AND(lc.destino IS NOT NULL) AND (lc.destino !=''))
                            GROUP BY modal
                            ORDER BY origem"""