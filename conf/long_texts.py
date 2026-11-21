from conf.game import GO_MONEY
from conf.texts import PROPERTY_NAME, price

UTILITY_CARD_TEXT = "Ühe kommunaalettevõtte\nkorral on rent 4-kordne\ntäringusilmade arv.\n\nMõlema kommunaalettevõtte\nkorral on rent 10-kordne\ntäringusilmade arv."

# chance and community chest texts
if_you_pass_go = f"Kui läbid stardiruudu, saad {price(GO_MONEY)}."

if_not_bought_may_buy = "Kui see ei ole ostetud, võid selle pangalt osta."
if_bought = "Kui see on ostetud"

def go_to_text(zone, index):
	return f"Mine ruudule {PROPERTY_NAME[zone][index]}. {if_you_pass_go}"

def pay(money):
	return f"Maksa {price(money)}"

def collect(money):
	return f"Saad {price(money)}"

go_to_jail = f"Eksid Pihla rappa ära.\nÄra mine läbi stardiruudu."
get_out_of_jail_free = f"RABAST PÄÄSEMISE KAART.\nSeda kaarti võib hoida kuni kasutamise või kauplemiseni."

def per_house_and_hotel(text: str, house_price: int, hotel_price: int):
	return f"{text}.\nMaksa iga maja eest {price(house_price)}.\nMaksa iga hotelli eest {price(hotel_price)}."

CH_TEXTS = [
	go_to_text(4, 2),
	go_to_text(2, 0),
	go_to_text(7, 1),
	f"Mine järgmisele kommunaalettevõtte ruudule.\n{if_not_bought_may_buy}\n{if_bought}, viska täringuid ja maksa\nomanikule 10-kordne täringusilmade arv.",
	f"Mine järgmisele sadamaruudule.\n{if_not_bought_may_buy}\n{if_bought}, maksa omanikule\nkahekordne rent.",
	f"Mine järgmisele sadamaruudule.\n{if_not_bought_may_buy}\n{if_bought}, maksa omanikule\nkahekordne rent.",
	f"Mine esimesele sadamaruudule.\n{if_you_pass_go}",
	f"Mine stardiruudule.\n({collect(GO_MONEY)})",
	f"Mine kolm ruutu tagasi.",
	go_to_jail,
	f"Sõid kohvikutepäevadel kõhu täis.\n{pay(15)}.",
	f"Tegid Hiiumaa parima seenekoha avalikuks.\nKõik hiidlased on su peale vihased.\nMaksa igale mängijale {price(50)}.",
	per_house_and_hotel("Teed üldremonti", 25, 100),
	f"Võitsid Hiiumaa Köök ja Pagar ostuloosis.\n{collect(50)}.",
	f"Leidsid metsast Ungru krahvi salajase varanduse.\n{collect(150)}.",
	get_out_of_jail_free
]

CC_TEXTS = [
	f"Mine stardiruudule.\n({collect(GO_MONEY)})",
	get_out_of_jail_free,
	go_to_jail,
	f"Pidutsesid odratolgustega.\n{pay(50)}.",
	per_house_and_hotel("Teed tänavaparandusi", 40, 115),
	f"Olid autoõnnetuses.\n{pay(100)}.",
	f"Uuendasid kalapüügiluba.\n{pay(50)}.",
	f"Aitasid naabrimeest.\n{collect(25)}.",
	f"Said teise koha orienteerumisvõistlusel.\n{collect(10)}.",
	f"Panga viga sinu kasuks.\n{collect(200)}.",
	f"Korjasid ja müüsid mustikaid.\n{collect(50)}.",
	f"Sul on sünnipäev.\nSaad igalt mängijalt {price(10)}.",
	f"Turist viskas tuletornist raha alla.\n{collect(100)}.",
	f"Tulumaksutagastus.\n{collect(20)}.",
	f"Hiiumaa vald tänab sind.\n{collect(100)}.",
	f"Müüsid kila-kola laadal oma kola maha.\n{collect(100)}."
]