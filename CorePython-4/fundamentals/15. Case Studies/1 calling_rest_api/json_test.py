result1 = {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',  'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217', 'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'], 'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'splunk', 'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count', 'slo': '99.8', 'formType': 'SLO', 'status': 'Published', 'comments': [], 'comment': None}
result2 = {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',  'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217', 'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'], 'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'splunk', 'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count', 'slo': '99.8', 'formType': 'CTA', 'status': 'Published', 'comments': [], 'comment': None}
result3 = {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',  'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217', 'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'], 'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'prometheus', 'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count', 'slo': '99.8', 'formType': 'CTA', 'status': 'Published', 'comments': [], 'comment': None}
result4 = {'partitionKey': 'cta', 'sortKey': '98t9t0tt006060', 'exp': None, 'id': '896006070707070oho',  'cr_by': 'adbkad', 'cr_dt': '2022-01-10T20:09:55.752+00.00', 'mdfd_by': 'SLY217', 'mdfd_dt': '2022-02-01T19:15:02.124+00.00', 'asv': ['ASVSTANDARDDATAPIPELINES'], 'pic': 'nima.sherpa@capital.com', 'metricName': 'Application Performance', 'datasource': 'prometheus', 'query': 'index=asvstandarddatapipelines source="/prod/logs/*planner.log" | eval response=case(like(HttpStatus,"2"),"Good", like(HttpStatus,"4"),"Good",true(),"Bad") | time chart span=1m count AS Attempts_Count, count(eval(response="Bad")) As Fail_Count', 'slo': '99.8', 'formType': 'CTA', 'status': 'Published', 'comments': [], 'comment': None}

# print(result1['formType']) # SLO/CTA
# index_str = result1['query']
# print(type(index_str))
# print(index_str)

if result1['formType'] =='SLO' or result1['formType'] =='CTA':
    ds = result1['datasource']
    if ds=='splunk' or ds == 'prometheus':
        index_str = result1['query']
        if index_str.count('index') >=1 and index_str.count('eval') and index_str.count('time chart'):
            print(index_str)
"""
if formType is SLO than
    if datasource is  splunk than
        keywords = ?
    else if datasource is  prometheus than
        keywords = query->(index, source, eval, timechart) -> present or not?       
        if not write error log -> text file?                     
    end if
else if formType is CTA than
    
end if    
"""

# portal -> request -> response
# data source type,
