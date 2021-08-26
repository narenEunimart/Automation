from azure.servicebus import ServiceBusClient, ServiceBusMessage
from sqlalchemy import create_engine
import pandas as pd
import logging
import json


connect = {
    "azure_connection_string":{
        "Amazon India":
        {
            "hierarchy" : "Endpoint=sb://rabbitmq-crawlers.servicebus.windows.net/;SharedAccessKeyName=shareMessages;SharedAccessKey=AO4gTFzQyeZFcK/wMbS7OFF8IoLIeINb34bkcUkYjDs=;EntityPath=amazon_india.hierarchy",
            "product_pages" : "Endpoint=sb://rabbitmq-crawlers.servicebus.windows.net/;SharedAccessKeyName=shareMessages;SharedAccessKey=Wv2fT5s4GkwXnJsp8FQwcTAAmJQF/CLbgZEnsNDP6Is=;EntityPath=amazon_india.product_pages",
            "product_parser" : "Endpoint=sb://rabbitmq-crawlers.servicebus.windows.net/;SharedAccessKeyName=SharedAccessKey;SharedAccessKey=IMAYH7i0U7I4sZzNAmMQxEiFb8CuFBkBmgq9DixYj8c=;EntityPath=amazon_india.product_parser"
        },
        "Flipkart":
        {
            "hierarchy" : "Endpoint=sb://rabbitmq-crawlers.servicebus.windows.net/;SharedAccessKeyName=shareMessages;SharedAccessKey=x72amvfqc2+4D/bXXl7PoXgPmbkxoOhyjr0O8vDLKYU=;EntityPath=flipkart.hierarchy",
            "product_pages" : "Endpoint=sb://rabbitmq-crawlers.servicebus.windows.net/;SharedAccessKeyName=shareMessages;SharedAccessKey=E20Wjc1pUDgSeFm/vnMkrBHw4QX+WpHiuBybPVlvsCs=;EntityPath=flipkart.product_pages",
            "product_parser" : "Endpoint=sb://rabbitmq-crawlers.servicebus.windows.net/;SharedAccessKeyName=shareMessages;SharedAccessKey=zFb382dlAXOtQ/n0iIU7h0KxOyY+kQysT9+l35EAlI0=;EntityPath=flipkart.product_parser"
        }
    },
}

def main(req: func.HttpRequest) -> func.HttpResponse:    
    logging.info('Python HTTP trigger function processed a request.')

    marketplace = req.params.get('name')
    queue_name = req.params.get('type')
    if not marketplace:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            marketplace = req_body.get('marketplace')
            queue_name = req_body.get('queue_name')

    azure_queue_name = '{0}.{1}'.format(marketplace.lower().replace(' ','_'),queue_name)

    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connect['azure_connection_string'][marketplace][queue_name], logging_enable=True)
    sender = servicebus_client.get_queue_sender(azure_queue_name)    

    engine = create_engine("postgresql://eunimart_user:o2R7chzDlxEYKDvp2g2W@crawl-data.cluster-cqxnvh2hudf5.us-east-2.rds.amazonaws.com:5432/crawled_data")
    cursor = engine.connect()

    urls = str('''select pid,fid,hierarchy,marketplace,product_url,type,position,page_no,is_best_seller from products_metadata where marketplace='{}' limit 10'''.format(marketplace))
    leaf_urls = cursor.execute(urls).fetchall()

    urls_df = pd.DataFrame(leaf_urls,columns = ['pid','fid','hierarchy','marketplace','product_url','type','position','page_no','is_best_seller'])
    
    for ind in urls_df.index:
        msg = {}
        msg["marketplace"] = urls_df['marketplace'][ind]
        msg['url'] = urls_df['product_url'][ind]
        msg['type'] = urls_df['type'][ind]
        msg['pid'] = urls_df['pid'][ind]
        msg['fid'] = urls_df['fid'][ind]
        msg['position'] = urls_df['position'][ind]
        msg['page_no'] = urls_df['page_no'][ind]
        msg['is_best_seller'] = urls_df['is_best_seller'][ind]
        msg['hierarchy'] = urls_df['hierarchy'][ind]
        
        message = ServiceBusMessage(json.dumps(msg))        
        sender.send_messages(message)

