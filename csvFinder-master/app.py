import os
import glob
from utils.csvFinder import csvFinder
from utils.dialogflow_uncle import detect_intent_texts
from utils.reply import reply_msg ,SetMessage_Object

from msgflex.flex import *

from flask import Flask, request, abort

app = Flask(__name__)
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_storage_path = os.path.join(base_dir,"CSVs")
csv_files = [f for f in os.listdir(csv_storage_path) if f.endswith('.csv')]

db = {}

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from config import channal_secret,channal_access_token

line_bot_api = LineBotApi(channal_access_token)
handler = WebhookHandler(channal_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    text_from_user = event.message.text
    reply_token = event.reply_token
    userid = event.source.user_id

    result_from_dialogflow = detect_intent_texts(project_id="natadsada-hfrcvi" ,   ### ถ้าส่งข้อมูล 4 ข้อมูลไปที่ dialogflow สิ่งที่จะได้กลับมาคือ action ของ User
                                        session_id=userid,
                                        text=text_from_user,
                                        language_code="th")

    action = result_from_dialogflow["action"]   ### action in dialogflow
    response = result_from_dialogflow["fulfillment_messages"] ### response in dialogflow  ## เป็นแบบ list

    print("action" + action)
    print("response" + str(response))

    if userid not in db.keys():
        db[userid] = {
            "keyword":None,
            "Column" :None
        }

    # if action == "Find_row":
    #     # 1.ตอบกลับไป กรุณาใส่คีเวิร์ด
        
    #     all_text = []
    #     for each in response:
    #         text = TextSendMessage(text=each)
    #         all_text.append(text)

    #     line_bot_api.reply_message(reply_token ,messages=all_text)   #reply message กลับไป

    #     return 'OK'

    # elif action == "Find_row_Result": 
        
    #     db[userid]["value"] = text_from_user        #เก็บข้อมูลการใช้งานของ user

    #     CSV = csvFinder(csvPath="./CSVs/รายการบ้านสองชั้น.csv")
    #     search_result = CSV.find_row(val=text_from_user,limit=10) ## search result => list of [dict]

    #     all_bubbles = []

    #     for each in search_result:
    #         แถวที่พบ = each["true_row"]
    #         คำที่ค้นหา = text_from_user ##คำที่ค้นหา
    #         คะแนนความเที่ยงตรง = each["score"]
    #         คอลัมน์ที่ค้นพบคำนี้ = each["col_name"]
            
    #         รายการที่ค้นพบ = each["result"] ##dictionary
            
    #         bubble = flex_find_row(แถวที่พบ ,คำที่ค้นหา ,คะแนนความเที่ยงตรง,คอลัมน์ที่ค้นพบคำนี้ ,รายการที่ค้นพบ)

    #         all_bubbles.append(bubble)
        
    #     flex_to_replay = make_carousel(all_bubble = all_bubbles)

    #     flex_to_replay = SetMessage_Object(flex_to_replay)  ###ข้อความตอบกลับ
    #     reply_msg(reply_token ,data=flex_to_replay ,bot_access_key=channal_access_token)
    #       #reply message กลับไป

    #     return 'OK'
     
    if action == "Find_Value":
        # 1.ตอบกลับไป กรุณาใส่คีเวิร์ด
        
        all_text = []
        for each in response:
            text = TextSendMessage(text=each)
            all_text.append(text)

        line_bot_api.reply_message(reply_token ,messages=all_text)   #reply message กลับไป

        return 'OK'
    
    elif action == "Find_Value_Getcolumn":
        all_text = []
        for each in response:
            text = TextSendMessage(text=each)
            all_text.append(text)

        line_bot_api.reply_message(reply_token ,messages=all_text)   #reply message กลับไป

        return 'OK'

    
    elif action == "Find_Value_Getcolumn_Result":
        
        col_to_find = response[0] ##Response เป็น list  #### dialogflow บอกว่า user ต้องการหา column ไหน

        CSV = csvFinder(csvPath="./CSVs/รายการบ้านสองชั้น.csv")
        search_result = CSV.find_value(val=text_from_user, col_to_find=col_to_find ,limit=10)


        results = [i["result"] for i in search_result]   ##List Compehension  
        ##Result ทั้งหมดจะเท่ากับ i ที่มี key เป็น result
        ### สำหรับ i ที่อยู่ใน search result
        ###สรุปคือจะได้ list ใหม่ ที่มีแค่ตัว result ตัวอื่นจะถูกตัดไป

        flex = flex_find_value(คำที่ค้นหา=text_from_user ,result = results)

        flex_to_replay = SetMessage_Object(flex)  ###ข้อความตอบกลับ
        reply_msg(reply_token ,data=flex_to_replay ,bot_access_key=channal_access_token)

        return 'OK'


    


    # CSV = csvFinder(csvPath=os.path.join(csv_storage_path,csv_files[0]))
    # res = CSV.find_row(val=text_from_user,limit=3)

    

if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Credentials.json"
    os.environ["DIALOGFLOW_PROJECT_ID"] = "natadsada-hfrcvi"
    app.run(port=5000,debug=True)


