
# def box_list(key,value):

#     each_box = {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [

#                 {
#                     "type": "text",
#                     "text": "| {}".format(key),  ## Mark up message
#                     "size": "sm",
#                     "color": "#888888",
#                     "flex": 0
#                 },

#                 {
#                     "type": "text",
#                     "text": value, ## Mark up message
#                     "size": "xxs",
#                     "color": "#111111",
#                     "align": "start",
#                     "wrap": True
#                 }

#                 ]

#         }

#     return each_box



# def flex_find_row(แถวที่พบ,คำที่ค้นหา,คะแนนความเที่ยงตรง,คอลัมน์ที่ค้นพบคำนี้,รายการที่ค้นพบ):  ### ฟังก์ชั่นค้นหาข้อมูล   แล้วมันจะสร้าง list เปล่า หลังจากก็จะเอา list เปล่า ไว้ใน Func make courasel

#     all_boxes = []
#     for key,val in รายการที่ค้นพบ.items():
#         box = box_list(key,val) ### เก็บค่า eachbox ของ func box_list ไว้ใน all_box
#         all_boxes.append(box)
#     seperator = {  ## คือเส้นปิดข้างล่าง ในข้อความ
#                 "type": "separator",
#                 "margin": "sm"
#             }

#     all_boxes.append(seperator)
#     bubble ={
#     "type": "bubble",
#     "size": "giga",
#     "body": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#         {
#             "type": "text",
#             "text": "โครงการ :บ้านสองชั้น 20 ล้าน",
#             "weight": "bold",
#             "color": "#1DB446",
#             "size": "sm"
#         },

#         {
#             "type": "text",
#             "text": "| ตำแหน่งที่พบ : แถวที่ {}".format(แถวที่พบ),
#             "weight": "bold",
#             "size": "md",
#             "margin": "xs"
#         },

#         {
#             "type": "text",
#             "text": "คำที่ค้นหา : {}".format(คำที่ค้นหา),
#             "size": "xs",
#             "color": "#aaaaaa",
#             "wrap": True,
#             "align": "start",
#             "margin": "md"
#         },

#         {
#             "type": "text",
#             "text": "คะแนนความเที่ยงตรง : {}".format(คะแนนความเที่ยงตรง),
#             "size": "xs",
#             "color": "#aaaaaa",
#             "wrap": True,
#             "align": "start",
#             "margin": "none"
#         },

#         {
#             "type": "text",
#             "size": "xs",
#             "color": "#aaaaaa",
#             "wrap": True,
#             "align": "start",
#             "text": "คอลัมน์ที่ค้นพบคำนี้ : {}".format(คอลัมน์ที่ค้นพบคำนี้)
#         },

#         {
#             "type": "separator",
#             "margin": "xxl"
#         },

#         {
#             "type": "box",
#             "layout": "vertical",
#             "margin": "xl",
#             "spacing": "sm",
#             "contents": all_boxes
#         },

#         {
#             "type": "separator",
#             "margin": "xxl"
#         },

#         {
#             "type": "box",
#             "layout": "horizontal",
#             "margin": "md",
#             "contents": [
#             {
#                 "type": "text",
#                 "text": "ลิงค์ Google Sheet",
#                 "size": "xs",
#                 "color": "#aaaaaa",
#                 "flex": 0
#             },

#             {
#                 "type": "text",
#                 "text": "คลิก",
#                 "color": "#1DB446",
#                 "size": "xs",
#                 "align": "end",

#                 "action": {
#                 "type": "uri",
#                 "label": "action",
#                 "uri": "https://docs.google.com/spreadsheets/d/1jJh2FrTGco-c_-W_a6ZRvr_Vhu3lu5lxS5TalCLozqg/edit#gid=680682167"
#                 }

#             }

#             ]

#         },

#         {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#             {
#                 "type": "image",
#                 "url": "https://cdn-images.prod.thinkofliving.com/wp-content/uploads/1/2019/04/24112413/05-NEO-HOME_Italian-Style.jpg",
#                 "position": "relative",
#                 "size": "md",
#                 "aspectMode": "cover"
#             }

#             ],
#             "position": "absolute",
#             "cornerRadius": "50px",
#             "borderWidth": "2px",
#             "borderColor": "#000000",
#             "offsetEnd": "20px",
#             "offsetTop": "20px"
#         }

#         ]

#     },
#     "styles": {
#         "footer": {
#         "separator": True
#         }

#     }

#     }

#     return bubble


# def make_carousel(all_bubble): ### เนื่องจากการค้นหา 1 result = 1 bubble  ซึ่งการค้นหาแต่ละครั้งมีหลาย result 
    

#     carousel = {    ## เป็นรูปแบบ carousel
#   "type": "carousel",
#   "contents": all_bubble
#   }
#     flex = {
#   "type": "flex",
#   "altText": "Flex Message",
#   "contents": carousel
#   }
#     return flex

def flex_find_value(คำที่ค้นหา ,result):

    all_box = []
    
    for num,each in enumerate(result ,start=1): ###enumurate => ทำการนับไปด้วย
        box =  {
              "type": "box",
              "layout": "baseline",
              "contents": [

                {
                  "type": "icon",
                  "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQayagdVWgO6eySgP_PEqC8D5j8P18MQmdIe2eYZjnZ2GH-SAbE&usqp=CAU",
                  "margin": "none",
                  "size": "lg"
                },

                {
                  "type": "text",
                  "text": "รายการที่ {}".format(num),
                  "flex": 0,
                  "margin": "sm",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": each,
                  "margin": "none",
                  "size": "sm",
                  "align": "end"
                }
              ]
            }
        all_box.append(box)

    
    
        # text = {
        #       "type": "text",
        #       "text": "พบรายการจากคำที่ท่านค้นหา {} รายการ".format(num),
        #       "margin": "none",
        #       "size": "sm"
        #     }
        # all_text.append(text)

    flex = {
    "type": "flex",
    "altText": "ข้อความจาก Sakuragi",
    "contents": {
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://i.ytimg.com/vi/FCD1a_blXhM/hqdefault.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
        }
        },
        "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com"
        },
        "contents": [
            {
            "type": "text",
            "text": "| Result",
            "size": "xl",
            "weight": "bold",
            "color": "#F74C4C"
            },

            {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "text",
              "text": "พบรายการจากคำที่ท่านค้นหา x รายการ",
              "margin": "none",
              "size": "sm"
            }]
        },
            
            {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": all_box
            },
            {
            "type": "text",
            "text": "พบรายการจากคำที่ท่านค้นหา",
            "margin": "none",
            "size": "xs",
            "color": "#AAAAAA",
            "wrap": True
            },
            {
            "type": "separator",
            "color": "#8C8484"
            }
        ]
        },
        "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "spacer",
            "size": "xs"
            },
            {
            "type": "button",
            "action": {
                "type": "uri",
                "label": "Add to Cart",
                "uri": "https://linecorp.com"
            },
            "color": "#CF2619",
            "style": "primary"
            }
        ]
        }
    }
    }
    return flex