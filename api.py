import query 
def Api(db, sch, tb):
    records,columns=query.consultarPostgres(db, sch, tb)
    api={'records':[],'columns':[]}
    for record in records:
        api['records'].append(record)       
    api['columns'].append(columns)
    
    return api