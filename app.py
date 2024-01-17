import json
import requests
import pytest
import unittest
def test_list_avah():
    data = {
    "cmd": "unit",
    "msisdn": "89170698"
}
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json = data)
    print(response.text)

    expected_json = {
    "result": {
        "offer": [
            {
                "unit": "3000",
                "period": "0",
                "price": "6900",
                "name": "6900 төг",
                "cardType": "34000",
                "description": [
                    "5GB дата | 5 хоног"
                ],
                "isAuto": "N",
                "id": "99"
            },
            {
                "unit": "5000",
                "period": "0",
                "price": "9900",
                "name": "9900 төг",
                "cardType": "33999",
                "description": [
                    "15GB дата | 10 хоног "
                ],
                "isAuto": "N",
                "id": "100"
            }
        ],
        "unitPackages": [
            {
                "name": "Хоногтой",
                "packages": [
                    {
                        "unit": "3000",
                        "period": "30",
                        "price": "3000",
                        "name": "3000 төг",
                        "cardType": "4",
                        "description": [],
                        "isAuto": "Y",
                        "id": "47"
                    },
                    {
                        "unit": "5000",
                        "period": "50",
                        "price": "5000",
                        "name": "5000 төг",
                        "cardType": "5",
                        "description": [],
                        "isAuto": "Y",
                        "id": "42"
                    },
                    {
                        "unit": "10000",
                        "period": "100",
                        "price": "10000",
                        "name": "10000 төг",
                        "cardType": "7",
                        "description": [
                            "3GB | 5 хоног"
                        ],
                        "isAuto": "Y",
                        "id": "43"
                    },
                    {
                        "unit": "15000",
                        "period": "150",
                        "price": "15000",
                        "name": "15000 төг",
                        "cardType": "9",
                        "description": [
                            "5GB | 5 хоног"
                        ],
                        "isAuto": "Y",
                        "id": "44"
                    },
                    {
                        "unit": "20000",
                        "period": "200",
                        "price": "20000",
                        "name": "20000 төг",
                        "cardType": "33485",
                        "description": [],
                        "isAuto": "N",
                        "id": "66"
                    },
                    {
                        "unit": "5000",
                        "period": "30",
                        "price": "25000",
                        "name": "25000 төг",
                        "cardType": "33474",
                        "description": [
                            "10GB дата",
                            "Сүлжээндээ ∞ яриа"
                        ],
                        "isAuto": "Y",
                        "id": "64"
                    },
                    {
                        "unit": "40000",
                        "period": "360",
                        "price": "40000",
                        "name": "40000 төг",
                        "cardType": "10221",
                        "description": [],
                        "isAuto": "Y",
                        "id": "54"
                    },
                    {
                        "unit": "50000",
                        "period": "360",
                        "price": "50000",
                        "name": "50000 төг",
                        "cardType": "33486",
                        "description": [],
                        "isAuto": "N",
                        "id": "65"
                    },
                    {
                        "unit": "70000",
                        "period": "360",
                        "price": "70000",
                        "name": "70000 төг",
                        "cardType": "10220",
                        "description": [],
                        "isAuto": "N",
                        "id": "55"
                    },
                    {
                        "unit": "120000",
                        "period": "360",
                        "price": "120000",
                        "name": "120000 төг",
                        "cardType": "10219",
                        "description": [],
                        "isAuto": "N",
                        "id": "56"
                    }
                ]
            },
            {
                "name": "Хоноггүй",
                "packages": [
                    {
                        "unit": "3000",
                        "period": "0",
                        "price": "6900",
                        "name": "6900 төг",
                        "cardType": "34000",
                        "description": [
                            "5GB дата | 5 хоног"
                        ],
                        "isAuto": "N",
                        "id": "99"
                    },
                    {
                        "unit": "5000",
                        "period": "0",
                        "price": "9900",
                        "name": "9900 төг",
                        "cardType": "33999",
                        "description": [
                            "15GB дата | 10 хоног "
                        ],
                        "isAuto": "N",
                        "id": "100"
                    }
                ]
            }
        ]
    },
    "resultCode": "000",
    "resultStr": "Амжилттай!"
}
    assert response.json() == expected_json, "Unexpected JSON structure in the response"

    print(response.text)

def test_data_list():
    data = {
            "cmd": "data",
            "msisdn": "89132412"
    }
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    expected_json = {
    "result": {
        "dataPackages": [
            {
                "name": "Их дататай",
                "packages": [
                    {
                        "promoPrice": "",
                        "period": "1",
                        "amount": "2048",
                        "price": "2500",
                        "name": "2GB",
                        "description": "",
                        "id": "1",
                        "type": "BigData",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "2",
                        "amount": "3072",
                        "price": "3500",
                        "name": "3GB",
                        "description": "",
                        "id": "2",
                        "type": "BigData",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "5",
                        "amount": "6144",
                        "price": "6000",
                        "name": "6GB",
                        "description": "",
                        "id": "3",
                        "type": "BigData",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "7",
                        "amount": "12288",
                        "price": "12000",
                        "name": "12GB",
                        "description": "",
                        "id": "4",
                        "type": "BigData",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "10",
                        "amount": "20480",
                        "price": "22000",
                        "name": "20GB",
                        "description": "",
                        "id": "5",
                        "type": "BigData",
                        "pill": "",
                        "isPromo": "N"
                    }
                ]
            },
            {
                "name": "Урт хугацаатай",
                "packages": [
                    {
                        "promoPrice": "",
                        "period": "3",
                        "amount": "2560",
                        "price": "3500",
                        "name": "2.5GB",
                        "description": "",
                        "id": "6",
                        "type": "LongTerm",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "10",
                        "amount": "4096",
                        "price": "6000",
                        "name": "4GB",
                        "description": "",
                        "id": "7",
                        "type": "LongTerm",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "3584",
                        "price": "12000",
                        "name": "3.5GB",
                        "description": "",
                        "id": "8",
                        "type": "LongTerm",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "35000",
                        "period": "30",
                        "amount": "18432",
                        "price": "21000",
                        "name": "18GB",
                        "description": "",
                        "id": "10",
                        "type": "LongTerm",
                        "pill": "",
                        "isPromo": "Y"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "8192",
                        "price": "22000",
                        "name": "8GB",
                        "description": "",
                        "id": "9",
                        "type": "LongTerm",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "50000",
                        "period": "30",
                        "amount": "51200",
                        "price": "30000",
                        "name": "50GB",
                        "description": "",
                        "id": "11",
                        "type": "LongTerm",
                        "pill": "",
                        "isPromo": "Y"
                    }
                ]
            },
            {
                "name": "Энтертайнмент",
                "packages": [
                    {
                        "promoPrice": "",
                        "period": "7",
                        "amount": "1024",
                        "price": "2000",
                        "name": "GAMING хязгааргүй",
                        "description": "Pubg, Mobile Legend, Clash of Clans, Fortnite, League of legends Wild Rift, Roblox, Call of Duty, Fifa, Standoff2, World of Tanks, Genshin Impact апп-ууд хамаарна",
                        "id": "16",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "",
                        "price": "2000",
                        "name": "NEWS хязгааргүй",
                        "description": "Unread, news.mn, ikon.mn, bloomberg news апп, вэбүүд хамаарна",
                        "id": "17",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "",
                        "price": "2000",
                        "name": "EDU хязгааргүй",
                        "description": "ШУТИС, СУИС, Хүмүүнлэг,  ДХИС болон Pearson онлайн сургалтын вебүүд хамаарна.",
                        "id": "20",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "0",
                        "price": "2900",
                        "name": "LookTV хязгааргүй",
                        "description": "",
                        "id": "12",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "",
                        "price": "5000",
                        "name": "MUSIC хязгааргүй",
                        "description": "Apple music, Soundcloud, Mmusic, Stitcher, Spotify апп-ууд хамаарна",
                        "id": "14",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "2048",
                        "price": "5000",
                        "name": "GAMING хязгааргүй",
                        "description": "Pubg, Mobile Legend, Clash of Clans, Fortnite, League of legends Wild Rift, Roblox, Call of duty, Fifa, Standoff2, World of Tanks, Genshin Impact апп-ууд хамаарна",
                        "id": "15",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "7",
                        "amount": "",
                        "price": "5000",
                        "name": "E-Meeting 10GB",
                        "description": "Zoom, Skype, Teams, Telegram, Google Classroom, Google Meet, Clubhouse апп-ууд хамаарна",
                        "id": "18",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "",
                        "price": "10000",
                        "name": "E-Meeting 25GB",
                        "description": "Zoom, Skype, Teams, Telegram, Google Classroom, Google Meet, Clubhouse апп-ууд хамаарна",
                        "id": "19",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "30",
                        "amount": "20480",
                        "price": "15000",
                        "name": "STREAMING 20GB",
                        "description": "LookTV, Netflix, Twitch апп-ууд хамаарна",
                        "id": "13",
                        "type": "Entertainment",
                        "pill": "",
                        "isPromo": "N"
                    }
                ]
            },
            {
                "name": "Роуминг",
                "packages": [
                    {
                        "promoPrice": "",
                        "period": "3",
                        "amount": "",
                        "price": "20000",
                        "name": "Asia 1GB",
                        "description": "China, Hong Kong, South Korea, Japan, Turkey, Malaysia, Singapore, Indonesia, Philippines, Kazakhstan, Kyrgyzstan, India, Macao, Taiwan, Thailand, Vietnam, Cyprus, Israel ",
                        "id": "72",
                        "type": "Roaming",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "3",
                        "amount": "",
                        "price": "30000",
                        "name": "Europe 1GB",
                        "description": "Turkey, China, Hong Kong, South Korea, Japan, Spain, Portugal, France, Italy, United Kingdom, Ireland, Germany, Netherlands, Belgium, Luxembourg, Switzerland, Austria, Hungary, Liechtenstein, Poland, Czechia, Slovakia, Norway, Sweden, Denmark, Russia, Latvia, Lithuania, Ukraine, Romania, Bulgaria, Albania, Greece, Malta, Cyprus, Israel, Croatia",
                        "id": "74",
                        "type": "Roaming",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "3",
                        "amount": "",
                        "price": "40000",
                        "name": "North America 1GB",
                        "description": "Hong Kong, China, South Korea, Japan, Turkey, USA, Canada, Mexico ",
                        "id": "76",
                        "type": "Roaming",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "3",
                        "amount": "",
                        "price": "40000",
                        "name": "Australia 1GB",
                        "description": "China, Turkey, Hong Kong, South Korea, Japan, Australia, New Zealand ",
                        "id": "78",
                        "type": "Roaming",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "10",
                        "amount": "",
                        "price": "50000",
                        "name": "Asia 3GB",
                        "description": "China, Hong Kong, South Korea, Japan, Turkey, Malaysia, Singapore, Indonesia, Philippines, Kazakhstan, Kyrgyzstan, India, Macao, Taiwan, Thailand, Vietnam, Cyprus, Israel ",
                        "id": "73",
                        "type": "Roaming",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "10",
                        "amount": "",
                        "price": "80000",
                        "name": "Europe 3GB",
                        "description": "China, Turkey, South Korea, Hong Kong, Spain, Japan, France, Portugal, United Kingdom, Italy, Germany, Ireland, Belgium, Netherlands, Switzerland, Luxembourg, Hungary, Austria, Poland, Liechtenstein, Slovakia, Czechia, Sweden, Norway, Denmark, Latvia, Russia, Lithuania, Ukraine, Romania, Bulgaria, Albania, Greece, Malta, Cyprus, Israel, Croatia",
                        "id": "75",
                        "type": "Roaming",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "10",
                        "amount": "",
                        "price": "100000",
                        "name": "North America 3GB",
                        "description": "Mexico, China, Hong Kong, Japan, South Korea, USA, Turkey, Canada",
                        "id": "77",
                        "type": "Roaming",
                        "pill": "",
                        "isPromo": "N"
                    },
                    {
                        "promoPrice": "",
                        "period": "10",
                        "amount": "",
                        "price": "100000",
                        "name": "Australia 3GB",
                        "description": "New Zealand, Turkey, China, South Korea, Hong Kong, Australia, Japan",
                        "id": "79",
                        "type": "Roaming",
                        "pill": "",
                        "isPromo": "N"
                    }
                ]
            }
        ]
    },
    "resultCode": "000",
    "resultStr": "Амжилттай!"
}
    assert response.json() == expected_json

    print(response.text)

def test_logout():
    data ={
            "cmd": "logout",
            "token": "JQDSDYVV0GRUFUS1S6I3"
    }
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json= data)
    print(response.text)
    expected_json = {
    "result": {},
    "resultCode": "000",
    "resultStr": "Амжилттай!"
    }
    assert response.json() == expected_json
def test_account_switch_sms_otp():
        data = {
        "cmd": "checkSwitch",
        "msisdn": "",
        "smscode": "",
        "fromToken": ""
    }
        response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
        print(response.text)


def test_negjiin_cardiin_list():
    data = {
    "cmd": "unit",
    "msisdn": "89170698"
}
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    expected_json = {
    "result": {
        "offer": [
            {
                "unit": "3000",
                "period": "0",
                "price": "6900",
                "name": "6900 төг",
                "cardType": "34000",
                "description": [
                    "5GB дата | 5 хоног"
                ],
                "isAuto": "N",
                "id": "99"
            },
            {
                "unit": "5000",
                "period": "0",
                "price": "9900",
                "name": "9900 төг",
                "cardType": "33999",
                "description": [
                    "15GB дата | 10 хоног "
                ],
                "isAuto": "N",
                "id": "100"
            }
        ],
        "unitPackages": [
            {
                "name": "Хоногтой",
                "packages": [
                    {
                        "unit": "3000",
                        "period": "30",
                        "price": "3000",
                        "name": "3000 төг",
                        "cardType": "4",
                        "description": [],
                        "isAuto": "Y",
                        "id": "47"
                    },
                    {
                        "unit": "5000",
                        "period": "50",
                        "price": "5000",
                        "name": "5000 төг",
                        "cardType": "5",
                        "description": [],
                        "isAuto": "Y",
                        "id": "42"
                    },
                    {
                        "unit": "10000",
                        "period": "100",
                        "price": "10000",
                        "name": "10000 төг",
                        "cardType": "7",
                        "description": [
                            "3GB | 5 хоног"
                        ],
                        "isAuto": "Y",
                        "id": "43"
                    },
                    {
                        "unit": "15000",
                        "period": "150",
                        "price": "15000",
                        "name": "15000 төг",
                        "cardType": "9",
                        "description": [
                            "5GB | 5 хоног"
                        ],
                        "isAuto": "Y",
                        "id": "44"
                    },
                    {
                        "unit": "20000",
                        "period": "200",
                        "price": "20000",
                        "name": "20000 төг",
                        "cardType": "33485",
                        "description": [],
                        "isAuto": "N",
                        "id": "66"
                    },
                    {
                        "unit": "5000",
                        "period": "30",
                        "price": "25000",
                        "name": "25000 төг",
                        "cardType": "33474",
                        "description": [
                            "10GB дата",
                            "Сүлжээндээ ∞ яриа"
                        ],
                        "isAuto": "Y",
                        "id": "64"
                    },
                    {
                        "unit": "40000",
                        "period": "360",
                        "price": "40000",
                        "name": "40000 төг",
                        "cardType": "10221",
                        "description": [],
                        "isAuto": "Y",
                        "id": "54"
                    },
                    {
                        "unit": "50000",
                        "period": "360",
                        "price": "50000",
                        "name": "50000 төг",
                        "cardType": "33486",
                        "description": [],
                        "isAuto": "N",
                        "id": "65"
                    },
                    {
                        "unit": "70000",
                        "period": "360",
                        "price": "70000",
                        "name": "70000 төг",
                        "cardType": "10220",
                        "description": [],
                        "isAuto": "N",
                        "id": "55"
                    },
                    {
                        "unit": "120000",
                        "period": "360",
                        "price": "120000",
                        "name": "120000 төг",
                        "cardType": "10219",
                        "description": [],
                        "isAuto": "N",
                        "id": "56"
                    }
                ]
            },
            {
                "name": "Хоноггүй",
                "packages": [
                    {
                        "unit": "3000",
                        "period": "0",
                        "price": "6900",
                        "name": "6900 төг",
                        "cardType": "34000",
                        "description": [
                            "5GB дата | 5 хоног"
                        ],
                        "isAuto": "N",
                        "id": "99"
                    },
                    {
                        "unit": "5000",
                        "period": "0",
                        "price": "9900",
                        "name": "9900 төг",
                        "cardType": "33999",
                        "description": [
                            "15GB дата | 10 хоног "
                        ],
                        "isAuto": "N",
                        "id": "100"
                    }
                ]
            }
        ]
    },
    "resultCode": "000",
    "resultStr": "Амжилттай!"
}
    assert response.json() == expected_json

def test_tulburiin_dood_dun():
    data = {
    "cmd":"checkAmount",
    "msisdn":"",
    "amount":550
}
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    expected_json = {
    "resultCode": "805",
    "resultStr": "Төлбөр төлөх боломжит доод үнэ 1’000₮ болно."
    }
    assert response.json() == expected_json


def test_banknii_songolt():
    data = {
    "cmd":"paymentOptions"
}
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    expected_json = {
    "result": {
        "qpay": [
            "khanbank",
            "statebank",
            "most",
            "xacbank",
            "capitronbank",
            "tdbbank",
            "bogdbank",
            "mbank",
            "statebankmongolia"
        ],
        "banks": [
            "socialpay",
            "tokipay",
            "card"
        ]
    },
    "resultCode": "000",
    "resultStr": "Амжилттай!"
}
    assert response.json() == expected_json, "Unexpecter JSON structure"
    print(response.text)


def test_baiguullagin_ner_check():
    data = {
    "cmd": "checkCorpNo",
    "corpno": "5388457"
}
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    expected_json = {
    "result": {
        "name": "Юнивишн"
    },
    "resultCode": "000",
    "resultStr": "Амжилттай!"
}
    assert response.json() == expected_json

def test_banner_list():
    data = {
    "cmd": "getPromoList"
}
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    expected_json = {
    "result": {
        "list": [
            {
                "imageLink": "https://www.unitel.mn/img/news/d84b3-shinele_-unitel-banner_500x266.png",
                "promoLink": "https://www.unitel.mn/unitel/promotion/881",
                "endDate": "2024-02-29 00:00:00",
                "bannerImageLink": "https://www.unitel.mn/img/banners/99254-shinele_-unitel-banner_600x250.png",
                "link": "https://www.unitel.mn/unitel/promotion/881",
                "regdate": "2024-01-15 19:16:45",
                "id": "345",
                "title": "9’900₮-өөр дансаа цэнэглээд сар шинийн урамшууллаа аваарай"
            },
            {
                "imageLink": "https://www.unitel.mn/img/news/3d06f-t-r-lzh-alhana-unitel-500x266.jpg",
                "promoLink": "https://www.unitel.mn/unitel/promotion/863",
                "endDate": None,
                "bannerImageLink": "https://www.unitel.mn/img/banners/b2c56-t-r-lzh-alhana-unitel-app-600x250.jpg",
                "link": "https://www.unitel.mn/unitel/promotion/863",
                "regdate": "2023-10-10 17:12:29",
                "id": "336",
                "title": "Өнгөрсөн, одоо, ирээдүйд хамтдаа түрүүлж алхана"
            },
            {
                "imageLink": "https://www.unitel.mn/img/news/c3077-500x266-1-.jpg",
                "promoLink": "https://www.unitel.mn/unitel/promotion/866",
                "endDate": None,
                "bannerImageLink": "https://www.unitel.mn/img/banners/323d6-600x250-1-.jpg",
                "link": "https://www.unitel.mn/unitel/promotion/866",
                "regdate": "2023-10-24 13:48:18",
                "id": "339",
                "title": "U brand-ийн залуус автобусаар зорчих бүрд дататай"
            },
            {
                "imageLink": "https://www.unitel.mn/img/news/b66e2-500x266-3-.jpg",
                "promoLink": "https://www.unitel.mn/unitel/promotion/877",
                "endDate": "2024-01-19 00:00:00",
                "bannerImageLink": "https://www.unitel.mn/img/banners/9bc23-600x250-3-.jpg",
                "link": "https://www.unitel.mn/unitel/promotion/877",
                "regdate": "2023-12-21 12:13:05",
                "id": "344",
                "title": "U brand-ийн залуусыг Celebrate U"
            },
            {
                "imageLink": "https://www.unitel.mn/img/news/bbbbf-medee-banner-500x266.png",
                "promoLink": "https://www.unitel.mn/unitel/promotion/862",
                "endDate": None,
                "bannerImageLink": "https://www.unitel.mn/img/banners/e30a0-artboard-1-copy.jpg",
                "link": "https://www.unitel.mn/unitel/promotion/862",
                "regdate": "2023-10-09 12:17:48",
                "id": "335",
                "title": "Юнител групп орон даяар 5G сүлжээний туршилтын станцаа асаалаа "
            }
        ]
    },
    "resultCode": "000",
    "resultStr": "Амжилттай!"
}
    assert response.json() == expected_json
    print(response.text)
def test_salbar_list():
    data = {
    "cmd": "getBranchList"
}
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    expected_json = {
        "result": {
            "salbar": {
                "country": {
                    "list": [
                        {
                            "descr": "Өмнөговь, Даланзадгад сум, Говийн хөгжлийн ордон 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/a0306-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Даланзадгад"
                        },
                        {
                            "descr": "Өмнөговь, Цогтцэций сум, Төрийн банкны 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/8e674-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Цогтцэций-1"
                        },
                        {
                            "descr": "Хөвсгөл, Мөрөн хот, 15 байрны залгаа шилэн барилга 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/7c0f3-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Хөвсгөл"
                        },
                        {
                            "descr": "Баянхонгор номгон 1 баг,  Голомт банкны байр 1 давхарт Урагшаа харсан хаалга",
                            "image": "https://www.unitel.mn/img/branch/ef614-bayanhongor.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Баянхонгор"
                        },
                        {
                            "descr": "Өвөрхангай, Арвайхээр, 5-р баг, Бумбат худалдааны төв, 1-р давхар",
                            "image": "https://www.unitel.mn/img/branch/ac945-s-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Ням"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба"
                                }
                            ],
                            "title": "Өвөрхангай"
                        },
                        {
                            "descr": "Орхон аймаг, Баян-Өндөр сум, Согоот баг, Сонор хайрхан Төвийн 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/a96c5-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Эрдэнэт"
                        },
                        {
                            "descr": "Дорнод, Хэрлэн сум, 6-р баг 70-р байр Гэгээ төв 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/91d30-gs.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Дорнод - Хэрлэн"
                        },
                        {
                            "descr": "Дорноговь, Сайншанд сум, Монгол даатгал ХХК-ийн байр",
                            "image": "https://www.unitel.mn/img/branch/3bbd4-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Сайншанд-1"
                        },
                        {
                            "descr": "Дархан-Уул, Дархан сум, Дархан зах, 40-р павилон",
                            "image": "https://www.unitel.mn/img/branch/649c5-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Мягмар-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба-Ням"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Даваа"
                                }
                            ],
                            "title": "Дархан"
                        },
                        {
                            "descr": "Улаанбаатар, Багануур дүүрэг, 1-р хороо, 64Б байр 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/66445-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Багануур"
                        },
                        {
                            "descr": "Дундговь, Сайнцагаан сум Бүрд рестораны 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/9476d-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Дундговь"
                        },
                        {
                            "descr": "Сүхбаатар, Баруун-Урт, 7 баг, Одкон хотхон, 1 байр, 1 давхар, 0 тоот",
                            "image": "https://www.unitel.mn/img/branch/1c09c-suhbaatar-baruun-urt.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Сүхбаатар Баруун-Урт"
                        },
                        {
                            "descr": "Ховд, Жаргалант сум, Цамбагарав баг, АН-ын байр 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/d34e1-hovd.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Ховд"
                        },
                        {
                            "descr": "Төв аймаг Зуунмод сум 1-р баг Монгол даатгалын байр 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/7ce1f-zuunmod.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Зуунмод"
                        },
                        {
                            "descr": "Завхан аймаг Улиастай хот Жинст баг төвийн хэсэг",
                            "image": "https://www.unitel.mn/img/branch/41398-zavhan_branch.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Завхан-Улиастай"
                        },
                        {
                            "descr": "Увс, Улаангом, 11р баг Юнителийн байр ",
                            "image": "https://www.unitel.mn/img/branch/97537-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Увс"
                        },
                        {
                            "descr": "Говь-Алтай,  Есөнбулаг сум, Мон-Алтай Үйлчилгээний төв",
                            "image": "https://www.unitel.mn/img/branch/c6a82-altay-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Говь-Алтай"
                        },
                        {
                            "descr": "Булган аймаг, Булган сум, 5-р баг, Хатанбаатар Магсаржавын гудамж, 262 -Б байр",
                            "image": "https://www.unitel.mn/img/branch/116d9-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Булган"
                        },
                        {
                            "descr": "Завхан, Тосонцэнгэл сум, Дархан Уул баг, Харгант төв 1-р давхар",
                            "image": "https://www.unitel.mn/img/branch/b3798-tosontsengel-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Тосонцэнгэл "
                        },
                        {
                            "descr": "Сэлэнгэ аймаг, Сайхан сум 1-р баг 26-р байр 1 давхар ",
                            "image": "https://www.unitel.mn/img/branch/c8300-1-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Хөтөл "
                        },
                        {
                            "descr": "Өвөрхангай аймаг, Хархорин сум, Ганган-Орхон баг Хасбанкны 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/a0456-harhorin-gs-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Хархорин "
                        },
                        {
                            "descr": "Хэнтий аймаг, Хэрлэн 1-р баг, Монгол эмипэкстэй байр",
                            "image": "https://www.unitel.mn/img/branch/43fc7-herlen-gs-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Хэрлэн-1"
                        },
                        {
                            "descr": "Сэлэнгэ, Мандал сум, Буян Тахь худалдааны төвийн 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/3dd1d-haraa-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Зүүнхараа "
                        },
                        {
                            "descr": "Дорноговь, Замын-Үүд, УБТЗ-ын зорчигч үйлчилгээний төв",
                            "image": "https://www.unitel.mn/img/branch/aa229-zamiinuud-location.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "11:00 - 18:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Замын-Үүд"
                        },
                        {
                            "descr": "Дархан-Уул аймаг, Шарын гол сум, Хайрхан баг  11 байр 16 тоот",
                            "image": "https://www.unitel.mn/img/branch/319ea-gol-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Дархан-Шарын Гол "
                        },
                        {
                            "descr": "Баян-өлгий аймаг, Өлгий сум 5-р баг, Үйлдвэрчний эвлэлийн байр, 1 давхар ",
                            "image": "https://www.unitel.mn/img/branch/7f5ba-lgiy.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Баян-Өлгий"
                        },
                        {
                            "descr": "Архангай, Эрдэнэбулган сум, 1-р баг 999 төвийн 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/6c9e4-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Архангай"
                        },
                        {
                            "descr": "Сэлэнгэ, Сүхбаатар 6-р баг, 1-р хэсэг Стандарт дэлгүүрийн хажуу талд",
                            "image": "https://www.unitel.mn/img/branch/b2eb3-s-hbaatar-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Сэлэнгэ"
                        },
                        {
                            "descr": "Хэнтий, Эвт худалдааны төв 1  давхарт",
                            "image": "https://www.unitel.mn/img/branch/6eea9-herlen2.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Хэрлэн-2"
                        },
                        {
                            "descr": "Говьсүмбэр, Сүмбэр 1-р, баг, МАН-ын байр 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/2a762-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Сүмбэр"
                        },
                        {
                            "descr": "Дорнод аймаг Хэрлэн сум 7-р баг Үйлчилгээний төв МХС байр зүүн жигүүр 1 давхарт ",
                            "image": "https://www.unitel.mn/img/branch/edc37-dornod2.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Дорнод-2"
                        },
                        {
                            "descr": "Өмнөговь Ханбогд сум, Жавхлант баг, Их булаг 103 тоот ",
                            "image": "https://www.unitel.mn/img/branch/de61f-salbar-1-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Ханбогд"
                        },
                        {
                            "descr": "Хөшигийн хөндий \"Шинэ нисэх буудал\" 1 давхрын хүлээн авах лобби 201-2",
                            "image": "https://www.unitel.mn/img/branch/6f3ad-nubia.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "08:00 - 18:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "08:00 - 18:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "НУБИА салбар"
                        },
                        {
                            "descr": "Ховд аймаг, Булган сум, Бүрэнхайрхан баг, Төрийн банкны хажууд Юнител салбар",
                            "image": "https://www.unitel.mn/img/branch/d7d5b-bulgan-gs.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                }
                            ],
                            "title": "Ховд - Булган гэрээт салбар"
                        },
                        {
                            "descr": "Хэнтий аймаг, Бор-Өндөр сум, 1-р баг, 36-р  байр, 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/30d7a-bor-nd-r-gs-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Хэнтий - Бор-Өндөр гэрээт салбар"
                        },
                        {
                            "descr": "Дархан-Уул аймаг, Шинэ хороолол Орос элчингийн замын зүүн талд",
                            "image": "https://www.unitel.mn/img/branch/5db50-photo-1-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Дархан - 3 "
                        },
                        {
                            "descr": "Өмнөговь Ханбогд сум, Оюутолгой уурхай",
                            "image": "https://www.unitel.mn/img/branch/27616-salbar-1-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "08:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "08:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Өмнөговь - Оюутолгой "
                        }
                    ]
                },
                "ub": {
                    "list": [
                        {
                            "descr": "БЗД, 15р хороолол, Баянцээл худалдааны төвөөс хойш 200м ",
                            "image": "https://www.unitel.mn/img/branch/b1331-sansar.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Сансар салбар"
                        },
                        {
                            "descr": "СХД, Москвагийн гудамж, Бармон бюлдинг 2 давхарт",
                            "image": "https://www.unitel.mn/img/branch/4c3e4-sapporo.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Саппоро салбар"
                        },
                        {
                            "descr": "БГД, 3,4-р хороолол, Сансар центрийн 1-р давхарт",
                            "image": "https://www.unitel.mn/img/branch/dc9e5-horoolol.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба"
                                }
                            ],
                            "title": "Хороолол салбар"
                        },
                        {
                            "descr": "ХУД, Оргил шилтгээн төвийн 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/803df-Orgil-Location.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Хан уул Оргил салбар"
                        },
                        {
                            "descr": "Москвагийн гудамж, Драгон Төв – н 2 давхрын баруун жигүүрт",
                            "image": "https://www.unitel.mn/img/branch/ba4ba-jpg.jpeg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Драгон салбар"
                        },
                        {
                            "descr": "СБД, УИД-ийн замын баруун урд, 18-р байр",
                            "image": "https://www.unitel.mn/img/branch/06997-40.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба"
                                }
                            ],
                            "title": "40 Мянгат салбар"
                        },
                        {
                            "descr": "ЧД, 14-р хороо 7 буудал Бүрэн плаза, Номин үйлчилгээний төв",
                            "image": "https://www.unitel.mn/img/branch/a9822-7-buudal.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "7 Буудал салбар"
                        },
                        {
                            "descr": "СБД, 100 айл, Ампер хаус Барилгын Их дэлгүүр",
                            "image": "https://www.unitel.mn/img/branch/04f50-100-ayl.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "100 айл салбар"
                        },
                        {
                            "descr": "БГД, 3-р хороолол, Номин их дэлгүүрийн 3 давхар",
                            "image": "https://www.unitel.mn/img/branch/c2d9d-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 20:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 19:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Номин салбар "
                        },
                        {
                            "descr": "СХД, Хархорин автобусны буудлын баруун хойно",
                            "image": "https://www.unitel.mn/img/branch/571ab-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Пирамид салбар"
                        },
                        {
                            "descr": "БЗД, Саруул тэнгэр 2 цогцолборын үйлчилгээний төв",
                            "image": "https://www.unitel.mn/img/branch/4415d-tenger.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Саруул тэнгэр салбар"
                        },
                        {
                            "descr": "БЗД, Баянзүрх захын хойно, Шинэ од ХХК-н байр, 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/58712-jpg.jpeg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Эрхэт салбар"
                        },
                        {
                            "descr": "СХД, 21-р хороолол, Содон хорооллын 2-р давхарт",
                            "image": "https://www.unitel.mn/img/branch/d46a8-21.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "21 салбар"
                        },
                        {
                            "descr": "ЧД, Тэнгис кино театрын урд, MN Tower-н 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/7d8fe-mn-tower.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Эм Эн Тауэр салбар"
                        },
                        {
                            "descr": "СХД, Баянхошууны шинэ эцэс, БОСА төвийн 2 давхарт ",
                            "image": "https://www.unitel.mn/img/branch/584c4-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Баянхошуу БОСА салбар"
                        },
                        {
                            "descr": "Улаанбаатар, Налайх дүүрэг, Буян-Налайх ХХК-ийн байр",
                            "image": "https://www.unitel.mn/img/branch/4c8bd-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 18:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Налайх салбар"
                        },
                        {
                            "descr": "БГД, 5-р хороо, 10-р хорооллын автобусны буудлын зүүн хойно",
                            "image": "https://www.unitel.mn/img/branch/6d90a-10.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "10-р хороолол салбар"
                        },
                        {
                            "descr": "ХУД, 4-р хороо, Яармагийн 1-р буудал, Carrefour дэлгүүрийн 2 давхарт",
                            "image": "https://www.unitel.mn/img/branch/b4019-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Яармаг салбар "
                        },
                        {
                            "descr": "ЧД, 3-р хороо, Улсын их дэлгүүрийн 5 давхарт ",
                            "image": "https://www.unitel.mn/img/branch/2fc93-ih-delguur-location.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 20:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "09:30 - 20:00",
                                    "days": "Бямба"
                                }
                            ],
                            "title": "Их Дэлгүүр салбар"
                        },
                        {
                            "descr": "БЗД 8-р хороо Emart худалдааны төвийн 2- р давхар",
                            "image": "https://www.unitel.mn/img/branch/7aed0-sky-location.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 21:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "09:00 - 21:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Скай салбар"
                        },
                        {
                            "descr": "ХУД, 2-р хрооо, Нисэхийн автобусны буудлын хажууд, 61-2 байр",
                            "image": "https://www.unitel.mn/img/branch/bf11d-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Нисэх салбар"
                        },
                        {
                            "descr": "СХД, 22-р хороо орбитын тойрог, Алаг тараг дэлгүүрийн 2 давхар",
                            "image": "https://www.unitel.mn/img/branch/8af21-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Орбит салбар"
                        },
                        {
                            "descr": "БЗД, 10-р хороо, Амгалан зах дотор",
                            "image": "https://www.unitel.mn/img/branch/31b3d-png.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Мягмар-Ням"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Даваа"
                                }
                            ],
                            "title": "Улиастай салбар"
                        },
                        {
                            "descr": "СБД 8-р хороо, Сүхбаатарын талбай-2, Сэнтрэл тауэр 2 давхар баруун жигүүрт буюу 201 тоот",
                            "image": "https://www.unitel.mn/img/branch/11791-central-location.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Сэнтрал Тауэр салбар"
                        },
                        {
                            "descr": "БЗД, 14-р хороо, НТОУХТөв, Баялаг Ундраа төвийн 2 давхарт",
                            "image": "https://www.unitel.mn/img/branch/34142-undraa.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа-Ням"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Мягмар"
                                }
                            ],
                            "title": "Баялаг ундраа салбар"
                        },
                        {
                            "descr": "ХУД, 77А байр,  Морьтон цогцолборын 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/656fe-uul.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Хан уул салбар"
                        },
                        {
                            "descr": "БЗД, 8-р хороо, Тэнгэр худалдааны төвийн 1-р давхарт",
                            "image": "https://www.unitel.mn/img/branch/54474-tenger-plaza.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "yes"
                                },
                                {
                                    "elderly_no_queue": "yes"
                                },
                                {
                                    "handicap": "yes"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 17:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Тэнгэр плаза салбар"
                        },
                        {
                            "descr": "ХУД, 15-р хороо, Стадион Оргил, Имарт Хан уул",
                            "image": "https://www.unitel.mn/img/branch/7d681-hanuul.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 21:00",
                                    "days": "Даваа-Ням"
                                }
                            ],
                            "title": "Имарт Хан уул салбар"
                        }
                    ]
                }
            },
            "kiosk": {
                "country": {
                    "list": [
                        {
                            "descr": "Дархан-Уул, шинэ хороолол 380 айлын орон сууц",
                            "image": "https://www.unitel.mn/img/branch/afdd8-kiosk.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                }
                            ],
                            "title": "Дархан Киоск"
                        },
                        {
                            "descr": "Архангай, Эрдэнэбулган, Кактус үйлчилгээний төв, 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/35dbe-kiosk.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                }
                            ],
                            "title": "Архангай Киоск"
                        },
                        {
                            "descr": "Дорнод, Хэрлэн сум, ЭХСХҮТөвийн 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/c9949-kiosk.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 17:00",
                                    "days": "Даваа"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                }
                            ],
                            "title": "Дорнод Киоск"
                        },
                        {
                            "descr": "Дархан сум, 8-р баг, Оргил худалдааны төв 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/f1124-1.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Дархан худалдааны төв Киоск"
                        },
                        {
                            "descr": "Баянхонгор номгон 1 баг, Голомт банкны байр 1 давхарт Урагшаа харсан хаалга",
                            "image": "https://www.unitel.mn/img/branch/1986f-microsoftteams-image-15-.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Баянхонгор Киоск"
                        },
                        {
                            "descr": "Хөвсгөл, Мөрөн хот, 15 байрны залгаа шилэн барилга 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/2c882-khuvsgul.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                },
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                }
                            ],
                            "title": "Хөвсгөл-Мөрөн Киоск"
                        },
                        {
                            "descr": "Өвөрхангай, Арвайхээр, 5-р баг, Бумбат худалдааны төв, 1-р давхар",
                            "image": "https://www.unitel.mn/img/branch/c0de3-uvurkhangai.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Өвөрхангай-Арвайхээр Киоск"
                        },
                        {
                            "descr": "Өмнөговь, Даланзадгад сум, Говийн хөгжлийн ордон 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/1711a-umnugovi.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Өмнөговь-Даланзадгад Киоск"
                        },
                        {
                            "descr": "Орхон аймаг баянөндөр сум согоот баг Сонор хайрхан Төвийн 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/b86ec-erdenet.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 20:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 18:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Эрдэнэт Киоск"
                        },
                        {
                            "descr": "Орхон, Баян-Өндөр, Бүрэнбүст баг, Орхон молл худалдааны төв",
                            "image": "https://www.unitel.mn/img/branch/11c11-microsoftteams-image-1-.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 18:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Эрдэнэт Орхон худалдааны төв Киоск"
                        },
                        {
                            "descr": "Сүхбаатар, Баруун-Урт, 7 баг, Одкон хотхон, 1 байр, 1 давхар, 0 тоот",
                            "image": "https://www.unitel.mn/img/branch/305fc-sukhbaatar.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 18:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Сүхбаатар-Баруун-Урт Киоск"
                        },
                        {
                            "descr": "Хэнтий хэрлэн 1-баг Монгол эмипэкстэй байр",
                            "image": "https://www.unitel.mn/img/branch/d921c-hentii.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Хэнтий-Хэрлэн Киоск"
                        },
                        {
                            "descr": "Жаргалант сум Цамбагарав баг, АН-ын байр 1 давхар",
                            "image": "https://www.unitel.mn/img/branch/8a19c-40e50-hovd-location.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "08:00 - 18:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Ховд-Жаргалант Киоск"
                        },
                        {
                            "descr": "Увс, Улаангом,  6-р баг Дөрвөн замд байрлах Хишигт худалдааны төв",
                            "image": "https://www.unitel.mn/img/branch/4584b-c9949-kiosk.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "10:00 - 16:00",
                                    "days": "Бямба"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Ням"
                                }
                            ],
                            "title": "Увс-Улаангом Киоск"
                        },
                        {
                            "descr": "Дорноговь, Сайншанд сум, Монгол даатгал ХХК-ийн байр",
                            "image": "https://www.unitel.mn/img/branch/4191c-sainshand-gadna-zurag.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "12:00 - 20:00",
                                    "days": "Даваа-Лхагва"
                                },
                                {
                                    "hours": "Амарна",
                                    "days": "Пүрэв-Баасан"
                                },
                                {
                                    "hours": "12:00 - 20:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Дорноговь-Сайншанд ГС Киоск"
                        }
                    ]
                },
                "ub": {
                    "list": [
                        {
                            "descr": "БГД, 5-р хороо, 3-р эмнэлэгийн 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/1312e-3-r-emneleg.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "no"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "00:00 - 00:00",
                                    "days": "Даваа"
                                }
                            ],
                            "title": "3-р эмнэлэг Киоск /Түр ажиллахгүй/"
                        },
                        {
                            "descr": "БЗД, 18-р хороо, Хавдар судлалын Төв эмнэлэг 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/2ab10-khavdar.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "11:00 - 17:00",
                                    "days": "Даваа"
                                }
                            ],
                            "title": "Хавдар судлал Киоск"
                        },
                        {
                            "descr": " ЧД, 1-р хороо, МЦХолбооны 1 давхарт ",
                            "image": "https://www.unitel.mn/img/branch/bc4b7-tuv-shuudan.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "08:30 - 19:00",
                                    "days": "Даваа-Баасан"
                                },
                                {
                                    "hours": "11:00 - 16:00",
                                    "days": "Бямба-Ням"
                                }
                            ],
                            "title": "Төв шуудан Киоск"
                        },
                        {
                            "descr": "Сүхбаатар дүүрэг, 3-р хороо, Тээвэрчдийн гуд, Саруул төв  (Нарны зам-53) 1 давхарт",
                            "image": "https://www.unitel.mn/img/branch/bfa75-saruul-supermarket.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "Амарна",
                                    "days": "Лхагва"
                                },
                                {
                                    "hours": "09:00 - 19:00",
                                    "days": "Даваа-Ням"
                                }
                            ],
                            "title": "Саруул зах Киоск"
                        },
                        {
                            "descr": "Хан-Уул дүүрэг, 4-р хороо, Хүннү молл төвийн нэг давхар ",
                            "image": "https://www.unitel.mn/img/branch/b5d9b-hunnumall.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "11:00 - 22:00",
                                    "days": "Даваа-Ням"
                                }
                            ],
                            "title": "Хүннү Молл Киоск"
                        },
                        {
                            "descr": "БГД, 16-р хороо, Maxmall худалдааны төв, 4-р давхар",
                            "image": "https://www.unitel.mn/img/branch/a99ca-1495183735.7283.jpg",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 21:00",
                                    "days": "Даваа-Ням"
                                }
                            ],
                            "title": "Макс Молл Киоск"
                        },
                        {
                            "descr": "Сүхбаатар 8-р хороо, Мэдээлэл Технологийн Үндэсний Парк",
                            "image": "https://www.unitel.mn/img/branch/920d5-urgoo_cinema_2_building-1.png",
                            "additional": [
                                {
                                    "pregnant_no_queue": "no"
                                },
                                {
                                    "elderly_no_queue": "no"
                                },
                                {
                                    "handicap": "no"
                                },
                                {
                                    "kiosk": "yes"
                                }
                            ],
                            "time": [
                                {
                                    "hours": "10:00 - 22:00",
                                    "days": "Даваа-Ням"
                                }
                            ],
                            "title": "Өргөө-2 Киоск"
                        }
                    ]
                }
            }
        },
        "resultCode": "000",
        "resultStr": "Амжилттай!"
    }
    assert response.json() == expected_json

def test_contact_list():
    data = {
    "cmd": "getContactDeepLinks"
}
    response = requests.post("https://endpoint.unitel.mn/unitelapp/test/api/test", json=data)
    print(response.text)
    expected_json = {
            "result": [
                {
                    "id": "1",
                    "type": "unitel",
                    "url": "http://m.me/unitelofficial/?ref=start"
                },
                {
                    "id": "2",
                    "type": "univision",
                    "url": "http://m.me/UnivisionMN/?ref=start"
                },
                {
                    "id": "3",
                    "type": "ger",
                    "url": "http://m.me/gerinternet/?ref=start"
                },
                {
                    "id": "4",
                    "type": "digital",
                    "url": "http://m.me/unitelofficial/?ref=/call_agent_from_app"
                }
            ],
            "resultCode": "000",
            "resultStr": "Амжилттай!"
    }
    assert response.json() == expected_json


