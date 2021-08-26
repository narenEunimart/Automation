from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json
import logging

seed_url={
    "Flipkart": [
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/books/pr?sid=bks&otracker=categorytree",
            "hierarchy":"Books"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/home-decor/pr?sid=arb&otracker=categorytree",
            "hierarchy":"Home Decor"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/home-furnishing/pr?sid=jra&otracker=categorytree",
            "hierarchy":"Home Furnishing"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/building-materials-and-supplies/pr?sid=b8s&otracker=categorytree",
            "hierarchy":"Building Materials And Supplies"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/industrial-scientific-supplies/pr?sid=gsx&otracker=categorytree",
            "hierarchy":"Industrial & Scientific Supplies"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/home-lighting/pr?sid=jhg&otracker=categorytree",
            "hierarchy":"Home Lighting"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/exercise-fitness/pr?sid=qoc&otracker=categorytree",
            "hierarchy":"Exercise & Fitness"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/kitchen-cookware-serveware/pr?sid=upp&otracker=categorytree",
            "hierarchy":"Kitchen, Cookware & Serveware"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/sports/pr?sid=abc&otracker=categorytree",
            "hierarchy":"Sports"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/pet-supplies/pr?sid=p3t&otracker=categorytree",
            "hierarchy":"Pet Supplies"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/festive-decor-gifting/pr?sid=bro&otracker=categorytree",
            "hierarchy":"Festive Decor & Gifting"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/home-cleaning-bathroom-accessories/pr?sid=rja&otracker=categorytree",
            "hierarchy":"Home Cleaning & Bathroom Accessories"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/health-care/pr?sid=hlc&otracker=categorytree",
            "hierarchy":"Health Care"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/beauty-and-grooming/pr?sid=g9b&otracker=categorytree",
            "hierarchy":"Beauty And Grooming"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/mobiles-accessories/pr?sid=tyy&otracker=categorytree",
            "hierarchy":"Mobiles & Accessories"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/health-care/pr?sid=hlc&otracker=categorytree",
            "hierarchy":"Health Care"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/home-improvement/pr?sid=h1m&otracker=categorytree",
            "hierarchy":"Home Improvement"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/computers/pr?sid=6bo&otracker=categorytree",
            "hierarchy":"Computers"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/cameras-accessories/pr?sid=jek&otracker=categorytree",
            "hierarchy":"Cameras Accessories"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/home-kitchen/pr?sid=j9e&otracker=categorytree",
            "hierarchy":"Home & Kitchen"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&otracker=categorytree",
            "hierarchy":"Clothing"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/footwear/pr?sid=osp&otracker=categorytree",
            "hierarchy":"Footwear"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/watches/pr?sid=r18&otracker=categorytree",
            "hierarchy":"Watches"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/bags-wallets-belts/pr?sid=reh&otracker=categorytree",
            "hierarchy":"Bags, Wallets & Belts"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/health-personal-care-appliances/pr?sid=zlw&otracker=categorytree",
            "hierarchy":"Health & Personal Care Appliances"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/audio-video/pr?sid=0pm&otracker=categorytree",
            "hierarchy":"Audio & Video"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/food-products/pr?sid=eat&otracker=categorytree",
            "hierarchy":"Food & Nutrition"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/furniture/pr?sid=wwe&otracker=categorytree",
            "hierarchy":"Furniture"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/music/pr?sid=p2c&otracker=categorytree",
            "hierarchy":"Music"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/automotive/pr?sid=0hx&otracker=categorytree",
            "hierarchy":"Automotive"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/kids-accessories/pr?sid=d69&otracker=categorytree",
            "hierarchy":"Kids Accessories"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/automation-robotics/pr?sid=igc&otracker=categorytree",
            "hierarchy":"Automation & Robotics"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/eyewear/pr?sid=u73&otracker=categorytree",
            "hierarchy":"Eyewear"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/wearable-smart-devices/pr?sid=ajy&otracker=categorytree",
            "hierarchy":"Wearable Smart Devices"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/musical-instruments/pr?sid=ypu&otracker=categorytree",
            "hierarchy":"Musical Instruments"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/sunglasses/pr?sid=26x&otracker=categorytree",
            "hierarchy":"Sunglasses"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/jewellery/pr?sid=mcr&otracker=categorytree",
            "hierarchy":"Jewellery"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/pens-stationery/pr?sid=dgv&otracker=categorytree",
            "hierarchy":"Pens & Stationery"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/toys/pr?sid=mgl&otracker=categorytree",
            "hierarchy":"Toys"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/baby-care/pr?sid=kyh&otracker=categorytree",
            "hierarchy":"Baby Care"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/gaming/pr?sid=4rr&otracker=categorytree",
            "hierarchy":"Gaming"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/music-movies-posters/pr?sid=4kt&otracker=categorytree",
            "hierarchy":"Music, Movies & Posters"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/automotive-accessories/pr?sid=1mt&otracker=categorytree",
            "hierarchy":"Automotive Accesories"
        },
        {  
            "marketplace":"Flipkart",
            "type":"hierarchy",
            "url":"https://www.flipkart.com/home-entertainment/pr?sid=ckf&otracker=categorytree",
            "hierarchy":"Home Entertainment"
        }
    ],
    "Amazon USA": [
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_arts?_encoding=UTF8&node=4954955011",
                "hierarchy":"Arts and Crafts"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_automotive?_encoding=UTF8&node=2562090011",
                "hierarchy":"Automotive"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_baby?_encoding=UTF8&node=16225005011",
                "hierarchy":"Baby"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_beauty?_encoding=UTF8&node=16225006011",
                "hierarchy":"Beauty & Personal Care"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_computers?_encoding=UTF8&node=16225007011",
                "hierarchy":"Computers"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_electronics?_encoding=UTF8&node=16225009011",
                "hierarchy":"Electronics"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_health?_encoding=UTF8&node=16225010011",
                "hierarchy":"Health & Household"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_kitchen?_encoding=UTF8&node=16225011011",
                "hierarchy":"Home & Kitchen"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_industrial?_encoding=UTF8&node=16225012011",
                "hierarchy":"Industrial & Scientific"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_pet?_encoding=UTF8&node=16225013011",
                "hierarchy":"Pet Supplies"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_sports?_encoding=UTF8&node=16225014011",
                "hierarchy":"Sports & Outdoors"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_tools?_encoding=UTF8&node=256643011",
                "hierarchy":"Tools & Home Improvement"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_video_games?_encoding=UTF8&node=16225016011",
                "hierarchy":"Video Games"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_software?_encoding=UTF8&node=16225008011",
                "hierarchy":"Software"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_toys?_encoding=UTF8&node=16225015011",
                "hierarchy":"Toys and Games"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_baby?_encoding=UTF8&node=16225005011",
                "hierarchy":"Baby"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/browse/ref=nav_shopall-export_nav_mw_sbd_intl_tools?_encoding=UTF8&node=256643011",
                "hierarchy":"Tools & Home Improvement"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_clothing",
                "hierarchy":"Clothing|Womens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A679337011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_shoes",
                "hierarchy":"Shoes|Womens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A7192394011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_jewelry",
                "hierarchy":"Jewelry|Womens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A6358543011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_watches",
                "hierarchy":"Watches|Womens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A15743631&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_handbags",
                "hierarchy":"Handbags|Womens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A2474936011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_accessories",
                "hierarchy":"Accesories|Womens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A1040658&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_clothing",
                "hierarchy":"Clothing|Mens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A679255011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_shoes",
                "hierarchy":"Shoes|Mens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A6358539011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_watches",
                "hierarchy":"Watches|Mens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A2474937011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_accessories",
                "hierarchy":"Accessories|Mens Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A1040664&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_clothing",
                "hierarchy":"Clothing|Girls Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A679217011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_shoes",
                "hierarchy":"Shoes|Girls Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A3880961&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_jewelry",
                "hierarchy":"Jewelry|Girls Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A6358547011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_watches",
                "hierarchy":"Watches|Girls Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225020011&rh=n%3A7141123011%2Cn%3A16225020011%2Cn%3A2474938011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_accessories",
                "hierarchy":"Accesories|Girls Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225020011&rh=n%3A7141123011%2Cn%3A7147442011%2Cn%3A7581687011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_school_uniforms",
                "hierarchy":"School Uniforms|Girls Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A1040666&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_clothing",
                "hierarchy":"Clothing|Boys Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A679182011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_shoes",
                "hierarchy":"Shoes|Boys Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A3880611&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_jewelry",
                "hierarchy":"Jewelry|Boys Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A6358551011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_watches",
                "hierarchy":"Watches|Boys Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=specialty-aps&bbn=16225021011&rh=n%3A7141123011%2Cn%3A16225021011%2Cn%3A2474939011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_accessories",
                "hierarchy":"Accesories|Boys Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s/ref=sd_allcat_nav_desktop_sa_intl_school_uniforms?_encoding=UTF8&bbn=7581691011&rh=i%3Aspecialty-aps%2Cn%3A7141123011%2Cn%3A7147443011%2Cn%3A7581691011",
                "hierarchy":"School Uniforms|Boys Fashion"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A15743261&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_carry_ons",
                "hierarchy":"Luggage|Carry-Ons"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A360832011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_backpacks",
                "hierarchy":"Luggage|Backpacks"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A15743271&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_garment_bags",
                "hierarchy":"Luggage|Garment Bags"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743241&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_travel_totes",
                "hierarchy":"Luggage|Travel Totes"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A15743291&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_luggage_sets",
                "hierarchy":"Luggage|Luggage Sets"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A9971584011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_laptop_bags",
                "hierarchy":"Luggage|Laptop Bags"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A2477388011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_suitcases",
                "hierarchy":"Luggage|Suitcases"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A2477386011&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_kids_luggage",
                "hierarchy":"Luggage|Kids Luggage"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743231&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_messenger_bags",
                "hierarchy":"Luggage|Messenger Bags"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15744111&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_umbrellas",
                "hierarchy":"Luggage|Umbrellas"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743211&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_duffles",
                "hierarchy":"Luggage|Duffels"
        },
        {  
                "marketplace":"Amazon USA",
                "type":"hierarchy",
                "url":"https://www.amazon.com/s?i=fashion-luggage&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743971&_encoding=UTF8&ref=sd_allcat_nav_desktop_sa_intl_travel_accessories",
                "hierarchy":"Luggage|Travel Accessories"
        }
    ],
    "Amazon India":[
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/Books/b?ie=UTF8&node=976389031&ref_=nav_shopall_sbc_books_all",
                "hierarchy":"Books"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_6612025031_ex_n_1?rh=n%3A976419031&bbn=976419031&ie=UTF8&qid=1552023679",
                "hierarchy":"Electronics"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_1968024031_ex_n_1?rh=n%3A1571271031&bbn=1571271031&ie=UTF8&qid=1552023991",
                "hierarchy":"Clothing & Accessories"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/beauty/b/ref=sd_allcat_sbc_bhg_beauty_all?ie=UTF8&node=1355016031",
                "hierarchy":"Beauty"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_5257478031_ex_n_1?rh=n%3A4772060031&bbn=4772060031&ie=UTF8&qid=1552024912",
                "hierarchy":"Car & Motorbike"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_1375392031_ex_n_1?rh=n%3A976392031&bbn=976392031&ie=UTF8&qid=1552023863",
                "hierarchy":"Computers & Accessories"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_1983578031_ex_n_1?rh=n%3A1571283031&bbn=1571283031&ie=UTF8&qid=1552024098",
                "hierarchy":"Shoes & Handbags"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_1374515031_ex_n_1?rh=n%3A1350384031&bbn=1350384031&ie=UTF8&qid=1552025310",
                "hierarchy":"Health & Personal Care"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_1380045031_ex_n_1?rh=n%3A976442031&bbn=976442031&ie=UTF8&qid=1552023371",
                "hierarchy":"Home & Kitchen"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/industrial-scientific/b/ref=sd_allcat_sbc_auto_ind_all?ie=UTF8&node=5866078031",
                "hierarchy":"Industrial & Scientific"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/Pet-Supplies/b/ref=sd_allcat_sbc_hk_pets_all?ie=UTF8&node=2454181031",
                "hierarchy":"Pet Supplies"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/Software/b/ref=sd_allcat_sbc_mobcomp_software?ie=UTF8&node=976451031",
                "hierarchy":"Software"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_3403635031_ex_n_1?rh=n%3A1984443031&bbn=1984443031&ie=UTF8&qid=1552025137",
                "hierarchy":"Sports, Fitness & Outdoors"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/Toys-Games/b/ref=sd_allcat_sbc_tbk_toys_games?ie=UTF8&node=1350380031",
                "hierarchy":"Toys & Games"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/video-games/b/ref=sd_allcat_sbc_mmvg_allvg?ie=UTF8&node=976460031",
                "hierarchy":"Video Games"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_4859498031_ex_n_1?rh=n%3A2454178031&bbn=2454178031&ie=UTF8&qid=1552025221",
                "hierarchy":"Grocery & Gourmet Foods"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_4068584031_ex_n_1?rh=n%3A976416031&bbn=976416031&ie=UTF8&qid=1552024842",
                "hierarchy":"Movies & TV Shows"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_14596996031_ex_n_1?rh=n%3A13712257031&bbn=13712257031&ie=UTF8&qid=1552024795",
                "hierarchy":"Collectibles & Fine Art"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_1375848031_ex_n_1?rh=n%3A976445031&bbn=976445031&ie=UTF8&qid=1552024598",
                "hierarchy":"Music"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_4654328031_ex_n_1?rh=n%3A3677697031&bbn=3677697031&ie=UTF8&qid=1552024568",
                "hierarchy":"Musical Instruments"
        },
        {  
                "marketplace":"Amazon India",
                "type":"hierarchy",
                "url":"https://www.amazon.in/s/ref=lp_3638784031_ex_n_1?rh=n%3A2454175031&bbn=2454175031&ie=UTF8&qid=1552024426",
                "hierarchy":"Outdoor Living"
        }
    ],
    "eBay":[
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/beauty",
                "hierarchy":"Fashion|Health & Beauty"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/handbags",
                "hierarchy":"Fashion|Womens Bags & Handbags"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/health",
                "hierarchy":"Fashion|Health"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/jewelry",
                "hierarchy":"Fashion|Jewelry"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/kids-baby",
                "hierarchy":"Fashion|Kids Clothing, Shoes & Accessories"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/mens-clothing",
                "hierarchy":"Fashion|Men Clothing"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/shoes",
                "hierarchy":"Fashion|Shoes"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/watches",
                "hierarchy":"Fashion|Watches, Parts & Accessories"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/womens-clothing",
                "hierarchy":"Fashion|Women Clothing"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/camera-photo",
                "hierarchy":"Electronics|Cameras & Photo"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/more-electronics",
                "hierarchy":"Electronics|Vehicle Electronics & GPS"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/cell-phone-pda",
                "hierarchy":"Electronics|Cell Phones, Smart Watches & Accessories"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/computers-networking",
                "hierarchy":"Electronics|Computers, Tablets & Network Hardware"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/tv-video-audio",
                "hierarchy":"Electronics|TV, Video & Home Audio Electronics"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/video-games",
                "hierarchy":"Electronics|Video Games & Consoles"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/antiques",
                "hierarchy":"Collectibles & Art|Antiques"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/art",
                "hierarchy":"Collectibles & Art|Art"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/coins",
                "hierarchy":"Collectibles & Art|Coins & Paper Money"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/collectibles",
                "hierarchy":"Collectibles & Art|Collectibles"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/comics",
                "hierarchy":"Collectibles & Art|Collectible Comics"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/dolls-bears",
                "hierarchy":"Collectibles & Art|Dolls & Teddy Bears"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/entertainment-memorabilia",
                "hierarchy":"Collectibles & Art|Entertainment Memorabilia"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/pottery-glass",
                "hierarchy":"Collectibles & Art|Pottery & Glass"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/sports-mem",
                "hierarchy":"Collectibles & Art|Sports Memorabilia, Fan Shop & Sports Cards"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/stamps",
                "hierarchy":"Collectibles & Art|Stamps"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/baby",
                "hierarchy":"Home & Garden|Baby Essentials"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Bath/26677/bn_824323",
                "hierarchy":"Home & Garden|Bathroom Supplies & Accessories"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/bedding",
                "hierarchy":"Home & Garden|Bedding"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/crafts",
                "hierarchy":"Home & Garden|Art & Craft Supplies"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Food-Beverages/14308/bn_1642947",
                "hierarchy":"Home & Garden|Food & Beverages"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/furniture",
                "hierarchy":"Home & Garden|Home & Garden Furniture"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/decor",
                "hierarchy":"Home & Garden|Home Décor"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/home-improvement",
                "hierarchy":"Home & Garden|Home Improvement"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/housekeeping",
                "hierarchy":"Home & Garden|Household & Cleaning Supplies"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/kitchen-dining",
                "hierarchy":"Home & Garden|Kitchen, Dining & Bar Supplies"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/major-appliances",
                "hierarchy":"Home & Garden|Major Appliances, Parts & Accessories"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/pet-supplies",
                "hierarchy":"Home & Garden|Pet Supplies"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/tools",
                "hierarchy":"Home & Garden|Tools & Workshop Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/yard-garden",
                "hierarchy":"Home & Garden|Yard, Garden & Outdoor Living Items"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/boxing-martial-arts-mma",
                "hierarchy":"Sporting Goods|Boxing & MMA Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/cycling",
                "hierarchy":"Sporting Goods|Cycling Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/fishing",
                "hierarchy":"Sporting Goods|Fishing Equipment & Supplies"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/exercise-fitness",
                "hierarchy":"Sporting Goods|Fitness, Running & Yoga Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/golf",
                "hierarchy":"Sporting Goods|Golf Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/hunting",
                "hierarchy":"Sporting Goods|Hunting Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/indoor-games",
                "hierarchy":"Sporting Goods|Indoor Games"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/outdoor-sports",
                "hierarchy":"Sporting Goods|Outdoor Sports"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/wholesale-sport-lots",
                "hierarchy":"Sporting Goods|Sporting Goods Wholesale Lots"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/team-sports",
                "hierarchy":"Sporting Goods|Team Sports"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/tennis-racquet-sports",
                "hierarchy":"Sporting Goods|Tennis & Racquet Sports"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/water-sports",
                "hierarchy":"Sporting Goods|Water Sports"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/winter-sports",
                "hierarchy":"Sporting Goods|Winter Sports"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Yoga-Pilates/158927/bn_1993406",
                "hierarchy":"Sporting Goods|Yoga & Pilates"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/action-figures",
                "hierarchy":"Toys & Hobbies|Action Figures"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/building-toys",
                "hierarchy":"Toys & Hobbies|Building Toys"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Diecast-Toy-Vehicles/222/bn_1850842",
                "hierarchy":"Toys & Hobbies|Diecast & Toy Vehicles"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/educational",
                "hierarchy":"Toys & Hobbies|Educational Toys"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/games",
                "hierarchy":"Toys & Hobbies|Games"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/model-railroads-trains",
                "hierarchy":"Toys & Hobbies|Model Railroads & Trains"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Toy-Models-Kits/1188/bn_1852447",
                "hierarchy":"Toys & Hobbies|Toy Models & Kits"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Preschool-Toys-Pretend-Play/19169/bn_1864380",
                "hierarchy":"Toys & Hobbies|Preschool Toys & Pretend Play"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/radio-control-control-line",
                "hierarchy":"Toys & Hobbies|RC Model Vehicles, Toys & Control Line"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/TV-Movie-Character-Toys/2624/bn_1865498",
                "hierarchy":"Toys & Hobbies|TV & Movie Character Toys"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Trading-Card-Games/2536/bn_1852210",
                "hierarchy":"Toys & Hobbies|Collectible Card Games & Accessories"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/agriculture-forestry",
                "hierarchy":"Business & Industrial|Agriculture & Forestry Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/construction",
                "hierarchy":"Business & Industrial|Other Building Materials"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/electrical-test-equipment",
                "hierarchy":"Business & Industrial|Electrical Equipment & Supplies"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Fuel-Energy/159693/bn_1865464",
                "hierarchy":"Business & Industrial|Industrial Fuel & Energy Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/office",
                "hierarchy":"Business & Industrial|Office Equipment & Supplies"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/healthcare-lab-life-science",
                "hierarchy":"Business & Industrial|Healthcare, Lab & Dental"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Heavy-Equipment-Attachments/177647/bn_1309146",
                "hierarchy":"Business & Industrial|Heavy Equipment Attachments"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/heavy-equipment",
                "hierarchy":"Business & Industrial|Heavy Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Heavy-Equipment-Parts-Accessories/41489/bn_7208228",
                "hierarchy":"Business & Industrial|Heavy Equipment Parts & Accessories"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Industrial-Automation-Control/42892/bn_2309506",
                "hierarchy":"Business & Industrial|Industrial Automation & Control Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Light-Industrial-Equipment-Tools/61573/bn_1521576",
                "hierarchy":"Business & Industrial|Light Industrial Equipment & Tools"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/mro-industrial-supply",
                "hierarchy":"Business & Industrial|Other Business & Industrial Equipment"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/manufacturing-metalworking",
                "hierarchy":"Business & Industrial|CNC, Metalworking & Manufacturing"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/packing-shipping",
                "hierarchy":"Business & Industrial|Packing & Shipping"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Printing-Graphic-Arts/26238/bn_1865538",
                "hierarchy":"Business & Industrial|Printing & Graphic Arts"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/restaurant-catering",
                "hierarchy":"Business & Industrial|Restaurant & Food Service"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/retail-services",
                "hierarchy":"Business & Industrial|Retail & Services"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"https://www.ebay.com/b/Websites-Businesses-for-Sale/11759/bn_1862440",
                "hierarchy":"Business & Industrial|Websites & Businesses for Sale"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/musical-instruments-gear",
                "hierarchy":"Music|Musical Instruments & Gear"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/recorded-music",
                "hierarchy":"Music|Music"
        },
        {  
                "marketplace":"eBay",
                "type":"hierarchy",
                "url":"http://www.ebay.com/rpp/tickets-experiences",
                "hierarchy":"Music|Tickets & Experiences"
        }
    ],
    "Etsy":[
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/craft-supplies-and-tools?explicit=1",
                "hierarchy":"Craft Supplies & Tools"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/jewelry?explicit=1",
                "hierarchy":"Jewellery"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/home-and-living?explicit=1",
                "hierarchy":"Home & Living"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/art-and-collectibles?explicit=1",
                "hierarchy":"Art & Collectibles"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/clothing?explicit=1",
                "hierarchy":"Clothing"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/paper-and-party-supplies?explicit=1",
                "hierarchy":"Paper & Party Supplies"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/accessories?explicit=1",
                "hierarchy":"Accessories"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/weddings?explicit=1",
                "hierarchy":"Weddings"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/bags-and-purses?explicit=1",
                "hierarchy":"Bags & Purses"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/bath-and-beauty?explicit=1",
                "hierarchy":"Bath & Beauty"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/toys-and-games?explicit=1",
                "hierarchy":"Toys & Games"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/books-movies-and-music?explicit=1",
                "hierarchy":"Books, Films & Music"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/electronics-and-accessories?explicit=1",
                "hierarchy":"Electronics & Accessories"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/pet-supplies?explicit=1",
                "hierarchy":"Pet Supplies"
        },
        {  
                "marketplace":"Etsy",
                "type":"hierarchy",
                "url":"https://www.etsy.com/in-en/c/shoes?explicit=1",
                "hierarchy":"Shoes"
            }
    ],
    "Bonanza":[
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=37903",
                "hierarchy":"Antiques|Antiquities"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=4707",
                "hierarchy":"Antiques|Architectural & Garden"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20082",
                "hierarchy":"Antiques|Asian Antiques"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20086",
                "hierarchy":"Antiques|Decorative Arts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2207",
                "hierarchy":"Antiques|Ethnographic"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20091",
                "hierarchy":"Antiques|Furniture"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=163008",
                "hierarchy":"Antiques|Home & Hearth"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=22422",
                "hierarchy":"Antiques|Incunabula"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181677",
                "hierarchy":"Antiques|Linens & Textiles (Pre-1930)"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=23048",
                "hierarchy":"Antiques|Manuscripts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=37958",
                "hierarchy":"Antiques|Maps, Atlases & Globes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=37965",
                "hierarchy":"Antiques|Maritime"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=163091",
                "hierarchy":"Antiques|Mercantile, Trades & Factories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181726",
                "hierarchy":"Antiques|Musical Instruments (Pre-1930)"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=12",
                "hierarchy":"Antiques|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=100927",
                "hierarchy":"Antiques|Periods & Styles"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1217",
                "hierarchy":"Antiques|Primitives"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=22608",
                "hierarchy":"Antiques|Reproduction Antiques"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=163101",
                "hierarchy":"Antiques|Restoration & Care"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=37978",
                "hierarchy":"Antiques|Rugs & Carpets"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20094",
                "hierarchy":"Antiques|Science & Medicine (Pre-1930)"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=156323",
                "hierarchy":"Antiques|Sewing (Pre-1930)"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20096",
                "hierarchy":"Antiques|Silver"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=552",
                "hierarchy":"Art|Art Drawings"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2211",
                "hierarchy":"Art|Art Photographs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=28009",
                "hierarchy":"Art|Art Posters"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=360",
                "hierarchy":"Art|Art Prints"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=553",
                "hierarchy":"Art|Art Sculptures"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=357",
                "hierarchy":"Art|Folk Art & Indigenous Art"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=554",
                "hierarchy":"Art|Mixed Media Art & Collage Art"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20158",
                "hierarchy":"Art|Other Art"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=551",
                "hierarchy":"Art|Paintings"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=156196",
                "hierarchy":"Art|Textile Art & Fiber Art"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=100223",
                "hierarchy":"Baby|Baby Gear"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20433",
                "hierarchy":"Baby|Baby Safety & Health"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20394",
                "hierarchy":"Baby|Bathing & Grooming"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=66692",
                "hierarchy":"Baby|Car Safety Seats"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=100982",
                "hierarchy":"Baby|Carriers, Slings & Backpacks"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=45455",
                "hierarchy":"Baby|Diapering"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20400",
                "hierarchy":"Baby|Feeding"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=117388",
                "hierarchy":"Baby|Keepsakes & Baby Announcements"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20416",
                "hierarchy":"Baby|Nursery Bedding"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=66697",
                "hierarchy":"Baby|Nursery Décor"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20422",
                "hierarchy":"Baby|Nursery Furniture"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1261",
                "hierarchy":"Baby|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=37631",
                "hierarchy":"Baby|Potty Training"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=66698",
                "hierarchy":"Baby|Strollers & Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=19068",
                "hierarchy":"Baby|Toys for Baby"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=48757",
                "hierarchy":"Baby|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=45110",
                "hierarchy":"Books|Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=29223",
                "hierarchy":"Books|Antiquarian & Collectible"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=29792",
                "hierarchy":"Books|Audiobooks"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=118254",
                "hierarchy":"Books|Catalogs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182882",
                "hierarchy":"Books|Children & Young Adults"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11104",
                "hierarchy":"Books|Cookbooks"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=171228",
                "hierarchy":"Books|Fiction & Literature"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=280",
                "hierarchy":"Books|Magazine Back Issues"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=171243",
                "hierarchy":"Books|Nonfiction"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=268",
                "hierarchy":"Books|Other Books"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2228",
                "hierarchy":"Books|Textbooks, Education"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=29399",
                "hierarchy":"Books|Wholesale & Bulk Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=109471",
                "hierarchy":"Business & Industrial|Adhesives, Sealants & Tapes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11748",
                "hierarchy":"Business & Industrial|Agriculture & Forestry"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=42892",
                "hierarchy":"Business & Industrial|Automation, Motors & Drives"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=46534",
                "hierarchy":"Business & Industrial|Cleaning & Janitorial Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11765",
                "hierarchy":"Business & Industrial|Construction"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=92074",
                "hierarchy":"Business & Industrial|Electrical & Test Equipment"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11897",
                "hierarchy":"Business & Industrial|Facility Maintenance & Safety"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183900",
                "hierarchy":"Business & Industrial|Fasteners & Hardware"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=159693",
                "hierarchy":"Business & Industrial|Fuel & Energy"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11815",
                "hierarchy":"Business & Industrial|Healthcare, Lab & Life Science"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=177641",
                "hierarchy":"Business & Industrial|Heavy Equipment"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=177647",
                "hierarchy":"Business & Industrial|Heavy Equipment Attachments"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=41489",
                "hierarchy":"Business & Industrial|Heavy Equipment Parts & Accs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=42909",
                "hierarchy":"Business & Industrial|HVAC"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183978",
                "hierarchy":"Business & Industrial|Hydraulics, Pneumatics & Pumps"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=61573",
                "hierarchy":"Business & Industrial|Light Equipment & Tools"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11804",
                "hierarchy":"Business & Industrial|Manufacturing & Metalworking"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=26221",
                "hierarchy":"Business & Industrial|Material Handling"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=25298",
                "hierarchy":"Business & Industrial|Office"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=26261",
                "hierarchy":"Business & Industrial|Other Business & Industrial"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=26238",
                "hierarchy":"Business & Industrial|Printing & Graphic Arts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11874",
                "hierarchy":"Business & Industrial|Restaurant & Catering"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11890",
                "hierarchy":"Business & Industrial|Retail & Services"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11759",
                "hierarchy":"Business & Industrial|Websites & Businesses for Sale"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=28179",
                "hierarchy":"Cameras & Photo|Binoculars & Telescopes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11724",
                "hierarchy":"Cameras & Photo|Camcorders"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=15200",
                "hierarchy":"Cameras & Photo|Camera & Photo Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182969",
                "hierarchy":"Cameras & Photo|Camera Drone Parts & Accs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=179697",
                "hierarchy":"Cameras & Photo|Camera Drones"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31388",
                "hierarchy":"Cameras & Photo|Digital Cameras"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=150044",
                "hierarchy":"Cameras & Photo|Digital Photo Frames"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=69323",
                "hierarchy":"Cameras & Photo|Film Photography"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=64353",
                "hierarchy":"Cameras & Photo|Flashes & Flash Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=78997",
                "hierarchy":"Cameras & Photo|Lenses & Filters"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=30078",
                "hierarchy":"Cameras & Photo|Lighting & Studio"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=4684",
                "hierarchy":"Cameras & Photo|Manuals & Guides"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=27432",
                "hierarchy":"Cameras & Photo|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182074",
                "hierarchy":"Cameras & Photo|Replacement Parts & Tools"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=30090",
                "hierarchy":"Cameras & Photo|Tripods & Supports"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=21162",
                "hierarchy":"Cameras & Photo|Video Production & Editing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3326",
                "hierarchy":"Cameras & Photo|Vintage Movie & Photography"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=45086",
                "hierarchy":"Cameras & Photo|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=9394",
                "hierarchy":"Cell Phones & Accessories|Cell Phone Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=9355",
                "hierarchy":"Cell Phones & Accessories|Cell Phones & Smartphones"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182064",
                "hierarchy":"Cell Phones & Accessories|Smart Watch Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=178893",
                "hierarchy":"Cell Phones & Accessories|Smart Watches"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182073",
                "hierarchy":"Cell Phones & Accessories|Vintage Cell Phones"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=45065",
                "hierarchy":"Cell Phones & Accessories|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=39482",
                "hierarchy":"Coins & Paper Money|Bullion"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=4733",
                "hierarchy":"Coins & Paper Money|Coins: Ancient"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3377",
                "hierarchy":"Coins & Paper Money|Coins: Canada"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=18466",
                "hierarchy":"Coins & Paper Money|Coins: Medieval"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=253",
                "hierarchy":"Coins & Paper Money|Coins: US"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=256",
                "hierarchy":"Coins & Paper Money|Coins: World"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3452",
                "hierarchy":"Coins & Paper Money|Exonumia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=169305",
                "hierarchy":"Coins & Paper Money|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3412",
                "hierarchy":"Coins & Paper Money|Paper Money: US"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3411",
                "hierarchy":"Coins & Paper Money|Paper Money: World"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=83274",
                "hierarchy":"Coins & Paper Money|Publications & Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3444",
                "hierarchy":"Coins & Paper Money|Stocks & Bonds, Scripophily"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=34",
                "hierarchy":"Collectibles|Advertising"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1335",
                "hierarchy":"Collectibles|Animals"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=13658",
                "hierarchy":"Collectibles|Animation Art & Characters"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=66502",
                "hierarchy":"Collectibles|Arcade, Jukeboxes & Pinball"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=14429",
                "hierarchy":"Collectibles|Autographs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=66503",
                "hierarchy":"Collectibles|Banks, Registers & Vending"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3265",
                "hierarchy":"Collectibles|Barware"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=156277",
                "hierarchy":"Collectibles|Beads"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=29797",
                "hierarchy":"Collectibles|Bottles & Insulators"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=562",
                "hierarchy":"Collectibles|Breweriana, Beer"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=898",
                "hierarchy":"Collectibles|Casino"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=397",
                "hierarchy":"Collectibles|Clocks"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=63",
                "hierarchy":"Collectibles|Comics"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1462",
                "hierarchy":"Collectibles|Credit, Charge Cards"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3913",
                "hierarchy":"Collectibles|Cultures & Ethnicities"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=13777",
                "hierarchy":"Collectibles|Decorative Collectibles"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=137",
                "hierarchy":"Collectibles|Disneyana"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=10860",
                "hierarchy":"Collectibles|Fantasy, Mythical & Magic"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=13877",
                "hierarchy":"Collectibles|Historical Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=907",
                "hierarchy":"Collectibles|Holiday & Seasonal"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=13905",
                "hierarchy":"Collectibles|Kitchen & Home"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1401",
                "hierarchy":"Collectibles|Knives, Swords & Blades"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1404",
                "hierarchy":"Collectibles|Lamps, Lighting"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=940",
                "hierarchy":"Collectibles|Linens & Textiles (1930-Now)"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1430",
                "hierarchy":"Collectibles|Metalware"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=13956",
                "hierarchy":"Collectibles|Militaria"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182982",
                "hierarchy":"Collectibles|Non-Sport Trading Cards"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=124",
                "hierarchy":"Collectibles|Paper"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=966",
                "hierarchy":"Collectibles|Pens & Writing Instruments"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=14005",
                "hierarchy":"Collectibles|Pez, Keychains, Promo Glasses"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1463",
                "hierarchy":"Collectibles|Phone Cards"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=14277",
                "hierarchy":"Collectibles|Photographic Images"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=39507",
                "hierarchy":"Collectibles|Pinbacks, Bobbles, Lunchboxes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=914",
                "hierarchy":"Collectibles|Postcards"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=29832",
                "hierarchy":"Collectibles|Radio, Phonograph, TV, Phone"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1446",
                "hierarchy":"Collectibles|Religion & Spirituality"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3213",
                "hierarchy":"Collectibles|Rocks, Fossils & Minerals"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=412",
                "hierarchy":"Collectibles|Science & Medicine (1930-Now)"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=152",
                "hierarchy":"Collectibles|Science Fiction & Horror"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=113",
                "hierarchy":"Collectibles|Sewing (1930-Now)"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=165800",
                "hierarchy":"Collectibles|Souvenirs & Travel Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=593",
                "hierarchy":"Collectibles|Tobacciana"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=13849",
                "hierarchy":"Collectibles|Tools, Hardware & Locks"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=417",
                "hierarchy":"Collectibles|Transportation"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=597",
                "hierarchy":"Collectibles|Vanity, Perfume & Shaving"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=69851",
                "hierarchy":"Collectibles|Vintage, Retro, Mid-Century"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=45058",
                "hierarchy":"Collectibles|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183062",
                "hierarchy":"Computers/Tablets & Networking|3D Printers & Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182094",
                "hierarchy":"Computers/Tablets & Networking|Computer Cables & Connectors"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=175673",
                "hierarchy":"Computers/Tablets & Networking|Computer Components & Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=171957",
                "hierarchy":"Computers/Tablets & Networking|Desktops & All-In-Ones"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=165",
                "hierarchy":"Computers/Tablets & Networking|Drives, Storage & Blank Media"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=175698",
                "hierarchy":"Computers/Tablets & Networking|Enterprise Networking, Servers"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11176",
                "hierarchy":"Computers/Tablets & Networking|Home Networking & Connectivity"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=176970",
                "hierarchy":"Computers/Tablets & Networking|iPad/Tablet/eBook Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=171485",
                "hierarchy":"Computers/Tablets & Networking|iPads, Tablets & eBook Readers"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3676",
                "hierarchy":"Computers/Tablets & Networking|Keyboards, Mice & Pointing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31530",
                "hierarchy":"Computers/Tablets & Networking|Laptop & Desktop Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=175672",
                "hierarchy":"Computers/Tablets & Networking|Laptops & Netbooks"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3516",
                "hierarchy":"Computers/Tablets & Networking|Manuals & Resources"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=162497",
                "hierarchy":"Computers/Tablets & Networking|Monitors, Projectors & Accs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=162",
                "hierarchy":"Computers/Tablets & Networking|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=86722",
                "hierarchy":"Computers/Tablets & Networking|Power Protection, Distribution"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=171961",
                "hierarchy":"Computers/Tablets & Networking|Printers, Scanners & Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=18793",
                "hierarchy":"Computers/Tablets & Networking|Software"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180235",
                "hierarchy":"Computers/Tablets & Networking|Tablet & eBook Reader Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11189",
                "hierarchy":"Computers/Tablets & Networking|Vintage Computing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=159260",
                "hierarchy":"Computers/Tablets & Networking|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=14948",
                "hierarchy":"Consumer Electronics|Gadgets & Other Electronics"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50582",
                "hierarchy":"Consumer Electronics|Home Automation"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=48633",
                "hierarchy":"Consumer Electronics|Home Surveillance"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3286",
                "hierarchy":"Consumer Electronics|Home Telephones & Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=48446",
                "hierarchy":"Consumer Electronics|Multipurpose Batteries & Power"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=15052",
                "hierarchy":"Consumer Electronics|Portable Audio & Headphones"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1500",
                "hierarchy":"Consumer Electronics|Radio Communication"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=32852",
                "hierarchy":"Consumer Electronics|TV, Video & Home Audio"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3270",
                "hierarchy":"Consumer Electronics|Vehicle Electronics & GPS"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183077",
                "hierarchy":"Consumer Electronics|Vintage Electronics"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183067",
                "hierarchy":"Consumer Electronics|Virtual Reality"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=184435",
                "hierarchy":"Consumer Electronics|Voice-Enabled Smart Assistants"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=61494",
                "hierarchy":"Consumer Electronics|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11783",
                "hierarchy":"Crafts|Art Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31723",
                "hierarchy":"Crafts|Beads & Jewelry Making"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183118",
                "hierarchy":"Crafts|Fabric Painting & Decorating"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=163778",
                "hierarchy":"Crafts|Glass & Mosaics"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=71183",
                "hierarchy":"Crafts|Handcrafted & Finished Pieces"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=160667",
                "hierarchy":"Crafts|Home Arts & Crafts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=116652",
                "hierarchy":"Crafts|Kids Crafts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=28131",
                "hierarchy":"Crafts|Leathercrafts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=28102",
                "hierarchy":"Crafts|Multi-Purpose Craft Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=160706",
                "hierarchy":"Crafts|Needlecrafts & Yarn"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=75576",
                "hierarchy":"Crafts|Other Crafts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11788",
                "hierarchy":"Crafts|Scrapbooking & Paper Crafts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183302",
                "hierarchy":"Crafts|Sculpting, Molding & Ceramics"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=160737",
                "hierarchy":"Crafts|Sewing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3122",
                "hierarchy":"Crafts|Stamping & Embossing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=45074",
                "hierarchy":"Crafts|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=999010",
                "hierarchy":"Digital Goods|Computer Software and Games"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=999011",
                "hierarchy":"Digital Goods|Digital Art"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=999014",
                "hierarchy":"Digital Goods|Movies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=999015",
                "hierarchy":"Digital Goods|Music"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=999016",
                "hierarchy":"Digital Goods|Photography"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50253",
                "hierarchy":"Dolls & Bears|Bear Making Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=386",
                "hierarchy":"Dolls & Bears|Bears"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1202",
                "hierarchy":"Dolls & Bears|Dollhouse Miniatures"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=238",
                "hierarchy":"Dolls & Bears|Dolls"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2440",
                "hierarchy":"Dolls & Bears|Paper Dolls"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=52546",
                "hierarchy":"Dolls & Bears|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=617",
                "hierarchy":"DVDs & Movies|DVD, HD DVD & Blu-ray"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=63821",
                "hierarchy":"DVDs & Movies|Film"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=381",
                "hierarchy":"DVDs & Movies|Laserdisc"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=41676",
                "hierarchy":"DVDs & Movies|Other Formats"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=52554",
                "hierarchy":"DVDs & Movies|Storage & Media Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=132975",
                "hierarchy":"DVDs & Movies|UMD"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=309",
                "hierarchy":"DVDs & Movies|VHS Tapes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31606",
                "hierarchy":"DVDs & Movies|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=57",
                "hierarchy":"Entertainment Memorabilia|Autographs-Original"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=104412",
                "hierarchy":"Entertainment Memorabilia|Autographs-Reprints"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=196",
                "hierarchy":"Entertainment Memorabilia|Movie Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2329",
                "hierarchy":"Entertainment Memorabilia|Music Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2312",
                "hierarchy":"Entertainment Memorabilia|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1424",
                "hierarchy":"Entertainment Memorabilia|Television Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2362",
                "hierarchy":"Entertainment Memorabilia|Theater Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=45101",
                "hierarchy":"Entertainment Memorabilia|Video Game Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3143",
                "hierarchy":"Everything Else|Career Development & Education"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=88739",
                "hierarchy":"Everything Else|Funeral & Cemetery"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20925",
                "hierarchy":"Everything Else|Genealogy"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=102480",
                "hierarchy":"Everything Else|Information Products"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=19266",
                "hierarchy":"Everything Else|Metaphysical"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=88433",
                "hierarchy":"Everything Else|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=102329",
                "hierarchy":"Everything Else|Personal Development"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=102535",
                "hierarchy":"Everything Else|Personal Security"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=102545",
                "hierarchy":"Everything Else|Religious Products & Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=102553",
                "hierarchy":"Everything Else|Reward Points & Incentives"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1466",
                "hierarchy":"Everything Else|Weird Stuff"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3082",
                "hierarchy":"Fashion|Baby & Toddler Clothing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=163147",
                "hierarchy":"Fashion|Costumes, Reenactment, Theater"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=155240",
                "hierarchy":"Fashion|Cultural & Ethnic Clothing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=112425",
                "hierarchy":"Fashion|Dancewear"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=171146",
                "hierarchy":"Fashion|Kids Clothing, Shoes & Accs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=4250",
                "hierarchy":"Fashion|Mens Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1059",
                "hierarchy":"Fashion|Mens Clothing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=93427",
                "hierarchy":"Fashion|Mens Shoes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=28015",
                "hierarchy":"Fashion|Uniforms & Work Clothing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=155184",
                "hierarchy":"Fashion|Unisex Clothing, Shoes & Accs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=175759",
                "hierarchy":"Fashion|Vintage"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3259",
                "hierarchy":"Fashion|Wedding & Formal Occasion"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=41964",
                "hierarchy":"Fashion|Wholesale, Large & Small Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=4251",
                "hierarchy":"Fashion|Womens Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=15724",
                "hierarchy":"Fashion|Womens Clothing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=169291",
                "hierarchy":"Fashion|Womens Handbags & Bags"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3034",
                "hierarchy":"Fashion|Womens Shoes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11838",
                "hierarchy":"Health & Beauty|Bath & Body"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=26396",
                "hierarchy":"Health & Beauty|Fragrances"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180345",
                "hierarchy":"Health & Beauty|Fragrances"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11854",
                "hierarchy":"Health & Beauty|Hair Care & Styling"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=67588",
                "hierarchy":"Health & Beauty|Health Care"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31786",
                "hierarchy":"Health & Beauty|Makeup"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=36447",
                "hierarchy":"Health & Beauty|Massage"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11778",
                "hierarchy":"Health & Beauty|Medical, Mobility & Disability"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=47945",
                "hierarchy":"Health & Beauty|Nail Care, Manicure & Pedicure"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=67659",
                "hierarchy":"Health & Beauty|Natural & Alternative Remedies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31769",
                "hierarchy":"Health & Beauty|Oral Care"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1277",
                "hierarchy":"Health & Beauty|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=177731",
                "hierarchy":"Health & Beauty|Salon & Spa Equipment"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31762",
                "hierarchy":"Health & Beauty|Shaving & Hair Removal"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11863",
                "hierarchy":"Health & Beauty|Skin Care"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31772",
                "hierarchy":"Health & Beauty|Sun Protection & Tanning"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=33914",
                "hierarchy":"Health & Beauty|Tattoos & Body Art"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31414",
                "hierarchy":"Health & Beauty|Vision Care"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180959",
                "hierarchy":"Health & Beauty|Vitamins & Dietary Supplements"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=40965",
                "hierarchy":"Health & Beauty|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=26677",
                "hierarchy":"Home & Garden|Bath"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20444",
                "hierarchy":"Home & Garden|Bedding"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=14308",
                "hierarchy":"Home & Garden|Food & Beverages"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=178069",
                "hierarchy":"Home & Garden|Fresh Cut Flowers & Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3197",
                "hierarchy":"Home & Garden|Furniture"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=16086",
                "hierarchy":"Home & Garden|Greeting Cards & Party Supply"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=38227",
                "hierarchy":"Home & Garden|Holiday & Seasonal Decor"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=10033",
                "hierarchy":"Home & Garden|Home Décor"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=159907",
                "hierarchy":"Home & Garden|Home Improvement"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=299",
                "hierarchy":"Home & Garden|Household Supplies & Cleaning"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=176988",
                "hierarchy":"Home & Garden|Kids & Teens at Home"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20625",
                "hierarchy":"Home & Garden|Kitchen, Dining & Bar"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20697",
                "hierarchy":"Home & Garden|Lamps, Lighting & Ceiling Fans"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20710",
                "hierarchy":"Home & Garden|Major Appliances"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181076",
                "hierarchy":"Home & Garden|Other Home & Garden"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20571",
                "hierarchy":"Home & Garden|Rugs & Carpets"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=631",
                "hierarchy":"Home & Garden|Tools"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11827",
                "hierarchy":"Home & Garden|Wedding Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31605",
                "hierarchy":"Home & Garden|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=63514",
                "hierarchy":"Home & Garden|Window Treatments & Hardware"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=159912",
                "hierarchy":"Home & Garden|Yard, Garden & Outdoor Living"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=84605",
                "hierarchy":"Jewelry & Watches|Childrens Jewelry"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=91427",
                "hierarchy":"Jewelry & Watches|Engagement & Wedding"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11312",
                "hierarchy":"Jewelry & Watches|Ethnic, Regional & Tribal"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=10968",
                "hierarchy":"Jewelry & Watches|Fashion Jewelry"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=4196",
                "hierarchy":"Jewelry & Watches|Fine Jewelry"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=110633",
                "hierarchy":"Jewelry & Watches|Handcrafted, Artisan Jewelry"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=10321",
                "hierarchy":"Jewelry & Watches|Jewelry Boxes & Organizers"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=164352",
                "hierarchy":"Jewelry & Watches|Jewelry Design & Repair"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=179264",
                "hierarchy":"Jewelry & Watches|Loose Beads"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=491",
                "hierarchy":"Jewelry & Watches|Loose Diamonds & Gemstones"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=10290",
                "hierarchy":"Jewelry & Watches|Mens Jewelry"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=98863",
                "hierarchy":"Jewelry & Watches|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=48579",
                "hierarchy":"Jewelry & Watches|Vintage & Antique Jewelry"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=14324",
                "hierarchy":"Jewelry & Watches|Watches"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=40131",
                "hierarchy":"Jewelry & Watches|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=52473",
                "hierarchy":"Music|Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=176983",
                "hierarchy":"Music|Cassettes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=176984",
                "hierarchy":"Music|CDs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=618",
                "hierarchy":"Music|Other Formats"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=176985",
                "hierarchy":"Music|Records"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=31608",
                "hierarchy":"Music|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=16212",
                "hierarchy":"Musical Instruments & Gear|Brass"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180008",
                "hierarchy":"Musical Instruments & Gear|Equipment"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3858",
                "hierarchy":"Musical Instruments & Gear|Guitars & Basses"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182150",
                "hierarchy":"Musical Instruments & Gear|Instruction Books, CDs & Video"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=175696",
                "hierarchy":"Musical Instruments & Gear|Karaoke Entertainment"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=308",
                "hierarchy":"Musical Instruments & Gear|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180012",
                "hierarchy":"Musical Instruments & Gear|Percussion"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180010",
                "hierarchy":"Musical Instruments & Gear|Pianos, Keyboards & Organs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180014",
                "hierarchy":"Musical Instruments & Gear|Pro Audio Equipment"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=15197",
                "hierarchy":"Musical Instruments & Gear|Pro Audio Equipment"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180015",
                "hierarchy":"Musical Instruments & Gear|Sheet Music & Song Books"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=12922",
                "hierarchy":"Musical Instruments & Gear|Stage Lighting & Effects"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180016",
                "hierarchy":"Musical Instruments & Gear|String"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181162",
                "hierarchy":"Musical Instruments & Gear|Vintage Musical Instruments"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=52555",
                "hierarchy":"Musical Instruments & Gear|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=10181",
                "hierarchy":"Musical Instruments & Gear|Wind & Woodwind"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=6747",
                "hierarchy":"Parts & Accessories|Apparel & Merchandise"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=43962",
                "hierarchy":"Parts & Accessories|ATV Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=26435",
                "hierarchy":"Parts & Accessories|Aviation Parts & Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=26443",
                "hierarchy":"Parts & Accessories|Boat Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=6030",
                "hierarchy":"Parts & Accessories|Car & Truck Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=38635",
                "hierarchy":"Parts & Accessories|Car Electronics"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=170140",
                "hierarchy":"Parts & Accessories|Golf Car Parts & Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=6029",
                "hierarchy":"Parts & Accessories|Manuals & Literature"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=25622",
                "hierarchy":"Parts & Accessories|Motorcycle Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=10063",
                "hierarchy":"Parts & Accessories|Motorcycle Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=6755",
                "hierarchy":"Parts & Accessories|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=34285",
                "hierarchy":"Parts & Accessories|Other Vehicle Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=107057",
                "hierarchy":"Parts & Accessories|Performance & Racing Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=124107",
                "hierarchy":"Parts & Accessories|Personal Watercraft Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50067",
                "hierarchy":"Parts & Accessories|RV, Trailer & Camper Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=168693",
                "hierarchy":"Parts & Accessories|Salvage Parts Cars"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=84149",
                "hierarchy":"Parts & Accessories|Scooter Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=111098",
                "hierarchy":"Parts & Accessories|Services & Installation"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=100448",
                "hierarchy":"Parts & Accessories|Snowmobile Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=10073",
                "hierarchy":"Parts & Accessories|Vintage Car & Truck Parts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50467",
                "hierarchy":"Parts & Accessories|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=177801",
                "hierarchy":"Pet Supplies|Backyard Poultry Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20734",
                "hierarchy":"Pet Supplies|Bird Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20737",
                "hierarchy":"Pet Supplies|Cat Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20742",
                "hierarchy":"Pet Supplies|Dog Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20754",
                "hierarchy":"Pet Supplies|Fish & Aquariums"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=301",
                "hierarchy":"Pet Supplies|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=116391",
                "hierarchy":"Pet Supplies|Pet Memorials & Urns"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1285",
                "hierarchy":"Pet Supplies|Reptile Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=26696",
                "hierarchy":"Pet Supplies|Small Animal Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=48760",
                "hierarchy":"Pet Supplies|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50693",
                "hierarchy":"Pottery & Glass|Glass"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=18875",
                "hierarchy":"Pottery & Glass|Pottery & China"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=47126",
                "hierarchy":"Specialty Services|Artistic Services"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50343",
                "hierarchy":"Specialty Services|Custom Clothing & Jewelry"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=47131",
                "hierarchy":"Specialty Services|Graphic & Logo Design"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=170048",
                "hierarchy":"Specialty Services|Home Improvement Services"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=175814",
                "hierarchy":"Specialty Services|Item Based Services"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50355",
                "hierarchy":"Specialty Services|Media Editing & Duplication"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=317",
                "hierarchy":"Specialty Services|Other Services"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=20943",
                "hierarchy":"Specialty Services|Printing & Personalization"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=47119",
                "hierarchy":"Specialty Services|Restoration & Repair"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=47104",
                "hierarchy":"Specialty Services|Web & Computer Services"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=179767",
                "hierarchy":"Sporting Goods|Boxing, Martial Arts & MMA"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=7294",
                "hierarchy":"Sporting Goods|Cycling"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1492",
                "hierarchy":"Sporting Goods|Fishing"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=15273",
                "hierarchy":"Sporting Goods|Fitness, Running & Yoga"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1513",
                "hierarchy":"Sporting Goods|Golf"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=7301",
                "hierarchy":"Sporting Goods|Hunting"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=36274",
                "hierarchy":"Sporting Goods|Indoor Games"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=310",
                "hierarchy":"Sporting Goods|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=159043",
                "hierarchy":"Sporting Goods|Outdoor Sports"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=159049",
                "hierarchy":"Sporting Goods|Team Sports"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=159134",
                "hierarchy":"Sporting Goods|Tennis & Racquet Sports"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=159136",
                "hierarchy":"Sporting Goods|Water Sports"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=40146",
                "hierarchy":"Sporting Goods|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=36259",
                "hierarchy":"Sporting Goods|Winter Sports"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=51",
                "hierarchy":"Sports Mem, Cards & Fan Shop|Autographs-Original"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50115",
                "hierarchy":"Sports Mem, Cards & Fan Shop|Autographs-Reprints"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=24409",
                "hierarchy":"Sports Mem, Cards & Fan Shop|Fan Apparel & Souvenirs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50116",
                "hierarchy":"Sports Mem, Cards & Fan Shop|Game Used Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=141755",
                "hierarchy":"Sports Mem, Cards & Fan Shop|Sports Stickers, Sets & Albums"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=212",
                "hierarchy":"Sports Mem, Cards & Fan Shop|Sports Trading Cards"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=50123",
                "hierarchy":"Sports Mem, Cards & Fan Shop|Vintage Sports Memorabilia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=56080",
                "hierarchy":"Sports Mem, Cards & Fan Shop|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181423",
                "hierarchy":"Stamps|Africa"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181416",
                "hierarchy":"Stamps|Asia"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181424",
                "hierarchy":"Stamps|Australia & Oceania"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=65174",
                "hierarchy":"Stamps|British Colonies & Territories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3478",
                "hierarchy":"Stamps|Canada"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=179377",
                "hierarchy":"Stamps|Caribbean"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=4742",
                "hierarchy":"Stamps|Europe"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3499",
                "hierarchy":"Stamps|Great Britain"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181417",
                "hierarchy":"Stamps|Latin America"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181422",
                "hierarchy":"Stamps|Middle East"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=170137",
                "hierarchy":"Stamps|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181421",
                "hierarchy":"Stamps|Publications & Supplies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=7898",
                "hierarchy":"Stamps|Specialty Philately"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=4752",
                "hierarchy":"Stamps|Topical Stamps"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=261",
                "hierarchy":"Stamps|United States"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=181420",
                "hierarchy":"Stamps|Worldwide"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=173634",
                "hierarchy":"Tickets & Experiences|Concerts"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1306",
                "hierarchy":"Tickets & Experiences|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=178892",
                "hierarchy":"Tickets & Experiences|Parking Passes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=170591",
                "hierarchy":"Tickets & Experiences|Special Experiences"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=173633",
                "hierarchy":"Tickets & Experiences|Sports"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=173635",
                "hierarchy":"Tickets & Experiences|Theater"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=170594",
                "hierarchy":"Tickets & Experiences|Theme Park & Club Passes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=246",
                "hierarchy":"Toys & Hobbies|Action Figures"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=49019",
                "hierarchy":"Toys & Hobbies|Beanbag Plush, Beanie Babies"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183446",
                "hierarchy":"Toys & Hobbies|Building Toys"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=19016",
                "hierarchy":"Toys & Hobbies|Classic Toys"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2536",
                "hierarchy":"Toys & Hobbies|Collectible Card Games"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=222",
                "hierarchy":"Toys & Hobbies|Diecast & Toy Vehicles"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11731",
                "hierarchy":"Toys & Hobbies|Educational"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=19071",
                "hierarchy":"Toys & Hobbies|Electronic, Battery & Wind-Up"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=19077",
                "hierarchy":"Toys & Hobbies|Fast Food & Cereal Premiums"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=233",
                "hierarchy":"Toys & Hobbies|Games"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=58799",
                "hierarchy":"Toys & Hobbies|Marbles"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=180250",
                "hierarchy":"Toys & Hobbies|Model Railroads & Trains"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1188",
                "hierarchy":"Toys & Hobbies|Models & Kits"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=11743",
                "hierarchy":"Toys & Hobbies|Outdoor Toys & Structures"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=19169",
                "hierarchy":"Toys & Hobbies|Preschool Toys & Pretend Play"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2613",
                "hierarchy":"Toys & Hobbies|Puzzles"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2562",
                "hierarchy":"Toys & Hobbies|Radio Control & Control Line"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=19192",
                "hierarchy":"Toys & Hobbies|Robots, Monsters & Space Toys"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2616",
                "hierarchy":"Toys & Hobbies|Slot Cars"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=436",
                "hierarchy":"Toys & Hobbies|Stuffed Animals"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2631",
                "hierarchy":"Toys & Hobbies|Toy Soldiers"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=2624",
                "hierarchy":"Toys & Hobbies|TV, Movie & Character Toys"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=717",
                "hierarchy":"Toys & Hobbies|Vintage & Antique Toys"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=40149",
                "hierarchy":"Toys & Hobbies|Wholesale Lots"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=3253",
                "hierarchy":"Travel|Airline"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=164802",
                "hierarchy":"Travel|Campground & RV Parks"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=147399",
                "hierarchy":"Travel|Car Rental"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=16078",
                "hierarchy":"Travel|Cruises"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=16123",
                "hierarchy":"Travel|Lodging"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=16080",
                "hierarchy":"Travel|Luggage"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=173520",
                "hierarchy":"Travel|Luggage Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=164803",
                "hierarchy":"Travel|Maps"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=1310",
                "hierarchy":"Travel|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=98982",
                "hierarchy":"Travel|Rail"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=93838",
                "hierarchy":"Travel|Travel Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=29578",
                "hierarchy":"Travel|Vacation Packages"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=183477",
                "hierarchy":"Travel|Vintage Luggage & Travel Accs"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182174",
                "hierarchy":"Video Games & Consoles|Manuals, Inserts & Box Art"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=38583",
                "hierarchy":"Video Games & Consoles|Merchandise"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=182175",
                "hierarchy":"Video Games & Consoles|Original Game Cases & Boxes"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=187",
                "hierarchy":"Video Games & Consoles|Other"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=156597",
                "hierarchy":"Video Games & Consoles|Prepaid Gaming Cards"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=171833",
                "hierarchy":"Video Games & Consoles|Replacement Parts & Tools"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=156595",
                "hierarchy":"Video Games & Consoles|Strategy Guides & Cheats"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=139971",
                "hierarchy":"Video Games & Consoles|Systems"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=54968",
                "hierarchy":"Video Games & Consoles|Video Game Accessories"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=139973",
                "hierarchy":"Video Games & Consoles|Video Games"
        },
        {  
                "marketplace":"Bonanza",
                "type":"hierarchy",
                "url":"https://www.bonanza.com/items/search?q%5Bfilter_category_id%5D=48749",
                "hierarchy":"Video Games & Consoles|Wholesale Lots"
        }
    ]
}

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

    marketplace = req.params.get('marketplace')
    queue_name = req.params.get('type')    
    azure_queue_name = '{0}.{1}'.format(marketplace.lower().replace(' ','_'),queue_name)

    servicebus_client = ServiceBusClient.from_connection_string(conn_str=connect['azure_connection_string'][marketplace][queue_name], logging_enable=True)    
    if not marketplace:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            marketplace = req_body.get('marketplace')
            queue_name = req_body.get('queue_name')
    if marketplace:
    
        with servicebus_client:                
            for url in seed_url[marketplace]:                                    
                print(url)
                sender = servicebus_client.get_queue_sender(azure_queue_name)                       
                sender.send_messages(ServiceBusMessage(json.dumps(url)))

        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
