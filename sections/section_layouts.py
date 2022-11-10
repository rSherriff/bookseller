
dialog_box_decoration =  chr(198) + chr(9608) + chr(201) + chr(9608)+ " "+ chr(9608) + chr(244)+ chr(9608)+ chr(230)
dialog_box_decoration_filled =  chr(198) + chr(9608) + chr(201) + chr(9608)+ chr(9608)+ chr(9608) + chr(244)+ chr(9608)+ chr(230)

button_box_decoration  =  chr(238) + chr(9604) + chr(232) + chr(9616)+ chr(9608)+chr(9612)+ chr(239) + chr(9600)+ chr(235)

black = (0,0,0)
white = (255,255,255)
grey=(158,158,158)
pink = (255,51,102)
orange = (255,191,0)
red=(255,0,0)

main_background = (23,18,25)


home_screen_info = {
    "title":{
        "x":10,
        "y":5,
        "width":36,
        "height":1
    },
    "advance_day_btn":{
        "x":6,
        "y":26,
        "width": 15,
        "height":5
    }
}

location_screen_info = {
    "title":{
        "x":10,
        "y":5,
        "width":36,
        "height":1
    },
    "locations":{
        "x":12,
        "y":9,
        "gap": 3,
        "button_delta" : 28
    },
    "description":{
        "x":10,
        "y":22,
        "width":38,
        "height":5
    },
    "search_bar":{
        "x":19,
        "y":30,
        "width":20,
        "height":1
    },
    "button_decoration":button_box_decoration,
    "button_width":4,
    "button_height":3,
    "b_fg_color": main_background,
    "b_bg_color":main_background,
    "b_h_color":orange,
    "b_font_fg_color":grey,
    "b_font_bg_color":main_background,
}

museum_screen_info = {
    "title":{
        "x":10,
        "y":5,
        "width":36,
        "height":1
    },
    "description":{
        "x":10,
        "y":22,
        "width":38,
        "height":5
    },
    "search_bar":{
        "x":18,
        "y":20,
        "width":20,
        "height":1
    },
    "button_decoration":button_box_decoration,
    "button_width":4,
    "button_height":3,
    "b_fg_color": main_background,
    "b_bg_color":main_background,
    "b_h_color":orange,
    "b_font_fg_color":grey,
    "b_font_bg_color":main_background,
}

map_screen_info = {
    "locations":{
        ("Chelsea", 13, 25, 8, 1),
        ("Bloomsbury", 29, 11, 11, 1),
        ("Southwark", 37, 31, 10, 1),
        ("Covent Garden", 29, 19, 14, 1),
    }
}

client_misc_tiles_info = {
    "speech_mark":
    {
        "x":0,
        "y":0,
        "width":4,
        "height":4
    }
}

client_screen_info = {
    "text":
    {
        "x":21,
        "y":5,
        "width":30,
        "height":10,
        "decoration":dialog_box_decoration_filled,
        "max_width":25
    },
    "speech_mark":
    {
        "x":20,
        "y":8,
        "width":4,
        "height":4
    }
}

client_character_info = {
    "x":5,
    "y":5,
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
    "title":{
        "x":10,
        "y":5,
        "width":36,
        "height":1
    },
    "shop_info":{
       "x":10,
        "y":9
    },
    "description":{
        "x":10,
        "y":22,
        "width":38,
        "height":5
    },
    "books":{
        "x":12,
        "y":12,
        "gap": 3,
        "button_delta" : 28
    },
    "button_decoration":button_box_decoration,
    "button_width":5,
    "button_height":3,
    "b_fg_color": main_background,
    "b_bg_color":main_background,
    "b_h_color":orange,
    "b_font_fg_color":grey,
    "b_font_bg_color":main_background,
}

presentation_dialog_info = {
    "books":{
        "x":2,
        "y":5,
        "gap": 3
    },
    "close_button":{
        "x":11,
        "y":16,
        "text":"Close"
    },
    "button_decoration":button_box_decoration,
    "button_height":3,
    "b_fg_color": main_background,
    "b_bg_color":main_background,
    "b_h_color":orange,
    "b_font_fg_color":grey,
    "b_font_bg_color":main_background,
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