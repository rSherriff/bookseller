
dialog_box_decoration =  chr(198) + chr(9608) + chr(201) + chr(9608)+ " "+ chr(9608) + chr(244)+ chr(9608)+ chr(230)
dialog_box_decoration_filled =  chr(198) + chr(9608) + chr(201) + chr(9608)+ chr(9608)+ chr(9608) + chr(244)+ chr(9608)+ chr(230)

button_box_decoration  =  chr(238) + chr(9604) + chr(232) + chr(9616)+ chr(9608)+chr(9612)+ chr(239) + chr(9600)+ chr(235)

black = (0,0,0)
white = (255,255,255)
grey=(158,158,158)
pink = (255,51,102)

main_background = (23,18,25)


home_screen_info = {
    "advance_day_btn":{
        "x":6,
        "y":6,
        "width": 15,
        "height":5
    }
}

location_screen_info = {
    "locations":{
        "x":6,
        "y":7,
        "gap": 2,
        "button_delta" : 25
    }
}

map_screen_info = {
    "locations":{
        ("Client", 13, 25, 7, 1),
        ("Bloomsbury", 29, 11, 11, 1),
        ("Home", 37, 31, 5, 1),
    }
}

client_misc_tiles_info = {
    "speech_mark":
    {
        "x":0,
        "y":0,
        "width":3,
        "height":3
    }
}

client_screen_info = {
    "text":
    {
        "x":18,
        "y":4,
        "width":30,
        "height":10
    },
    "speech_mark":
    {
        "x":14,
        "y":4,
        "width":3,
        "height":3
    }
}

client_character_info = {
    "x":3,
    "y":3,
    "width":11,
    "height":14,
    "sprites":{
        "talk_one":{
            "x":0,
            "y":0
        },
        "talk_two":{
            "x":12,
            "y":0
        }
    }
}


shop_screen_info = {
    "books":{
        "x":6,
        "y":7,
        "gap": 2,
        "button_delta" : 25
    }
}

confirmation_dialog_info = {
    "dialog_decoration":dialog_box_decoration_filled,
    "button_decoration":button_box_decoration,
    "fg_color":white,
    "bg_color":black,
    "b_fg_color": white,
    "b_bg_color":white,
    "b_h_color":pink,
    "b_font_fg_color":grey,
    "b_font_bg_color":white,
    "max_width" : 40,
    "button_width" : 3,
    "button_height": 3
}

notification_dialog_info = {
    "dialog_decoration":dialog_box_decoration_filled,
    "button_decoration":button_box_decoration,
    "fg_color":white,
    "bg_color":black,
    "b_fg_color": white,
    "b_bg_color":white,
    "b_h_color":pink,
    "b_font_fg_color":grey,
    "b_font_bg_color":white,
    "max_width" : 40,
    "button_width" : 7,
    "button_height": 3
}