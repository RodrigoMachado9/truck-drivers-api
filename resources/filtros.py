__author__='RodrigoMachado'
__license__ = "MIT"
__version__ = "1.0.1"
__status__ = "Production"
__copyright__ = "Copyright 2019"
__maintainer__ = "RodrigoMachado9"
__email__ = "rodrigo.machado3.14@hotmail.com"
__credits__ = ["Python is life", "Live the opensource world"]

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
motorista_sem_carga ="""SELECT 
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
caminhoneiro_possue_veiculo_proprio="""SELECT COUNT(possueveiculoproprio) possueveiculoproprio
                                        FROM motoristas
                                        WHERE possueveiculoproprio='true' 
                                        AND (possueveiculoproprio IS NOT NULL
                                        AND(possueveiculoproprio !=''))"""

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

top_caminhoneiros ="""SELECT 
                        mo.nome,
                        lc.avaliacao
                        FROM motoristas mo
                        INNER JOIN local_carga lc ON lc.motorista_id = mo.motorista_id
                        WHERE(
                        lc.avaliacao
                        >= 1 OR (lc.avaliacao <=10))"""


#todo; /* caminhoneiros disponiveis para carga*/
caminhoneiro_disponivel="""SELECT
                                mo.nome nome,
                                mo.sexo sexo,
                                mo.idade idade,
                                mo.cnhcategoria cnhcategoria,
                                v.marca marca,
                                v.tipo_de_carroceria tipo_de_carroceria,
                                v.caminhao_possue_rastreador rastreador,
                                tpv.modal modal,
                                tpv.cargamin cargamin,
                                tpv.cargamax cargamax
                            FROM motoristas mo 
                                LEFT JOIN local_carga lc ON lc.motorista_id = mo.motorista_id
                                LEFT JOIN veiculo v ON v.motorista_id = mo.motorista_id
                                LEFT JOIN tipo_veiculo tpv ON tpv.veiculo_id = v.veiculo_id
                                INNER JOIN status_veiculo stv ON stv.veiculo_id = v.veiculo_id
                            WHERE( 
                                    stv.carregado='false' OR( stv.carregado != 'true'
                                    OR(stv.carregado IS NULL 
                                    OR(stv.carregado ='')))
                                    )"""