UTILITY_CARD_TEXT = "Ühe kommunaalettevõtte korral on rent 4-kordne täringusilmade arv.\n\nMõlema kommunaalettevõtte korral on rent 10-kordne täringusilmade arv."

from generators.utils import price
from conf.game import GO_MONEY
from conf.texts import PROPERTY_NAME

# chance and community chest texts
if_you_pass_go = f"Kui läbid stardiruudu, saad {price(GO_MONEY)}."

if_not_bought_may_buy = "Kui see ei ole ostetud, võid selle pangast osta."
if_bought = "Kui see on ostetud"

def go_to_text(zone, index):
	return f"Mine ruudule {PROPERTY_NAME[zone][index]}. {if_you_pass_go}"

def pay(money):
	return f"Maksa {price(money)}"

def collect(money):
	return f"Saad {price(money)}"

go_to_jail = f"Mine rappa.\nMine otse rappa.\nSa ei lähe läbi stardiruudu.\nSa ei saa {price(GO_MONEY)}."
get_out_of_jail_free = f"RABAST PÄÄSEMISE KAART.\nSeda kaarti võib hoida kuni kasutamise või kauplemiseni."

def per_house_and_hotel(text: str, house_price: int, hotel_price: int):
	return f"{text}.\nMaksa iga maja eest {price(house_price)}.\nMaksa iga hotelli eest {price(hotel_price)}."

CH_TEXTS = [
	go_to_text(4, 2),
	go_to_text(2, 0),
	go_to_text(7, 1),
	f"Mine järgmisele kommunaalettevõtte ruudule.\n{if_not_bought_may_buy}\n{if_bought}, viska täringuid ja maksa omanikule 10-kordne täringusilmade arv.",
	f"Mine järgmisele sadamaruudule.\n{if_not_bought_may_buy}\n{if_bought}, maksa omanikule kahekordne rent.",
	f"Mine järgmisele sadamaruudule.\n{if_not_bought_may_buy}\n{if_bought}, maksa omanikule kahekordne rent.",
	f"Mine esimesele sadamaruudule. {if_you_pass_go}",
	f"Mine stardiruudule.\n({collect(GO_MONEY)})",
	f"Mine tagasi kolm ruutu.",
	go_to_jail,
	f"Trahv prügi maha viskamise eest.\n{pay(15)}.",
	f"Sind valiti juhatuse esimeheks.\nMaksa igale mängijale {price(50)}.",
	per_house_and_hotel("Teed üldremonti", 25, 100),
	f"Võitsid ostuloosis.\n{collect(50)}.",
	f"Leidsid metsast varanduse.\n{collect(150)}.",
	get_out_of_jail_free
]

CC_TEXTS = [
	f"Mine stardiruudule.\n({collect(GO_MONEY)})",
	get_out_of_jail_free,
	go_to_jail,
	f"Ostad koolitarbeid.\n{pay(50)}.",
	per_house_and_hotel("Teed tänavaparandusi", 40, 115),
	f"Olid autoõnnetuses.\n{pay(100)}.",
	f"Arsti arved.\n{pay(50)}.",
	f"Aitasid naabrimeest.\n{collect(25)}.",
	f"Said teise koha orienteerumisvõistlusel.\n{collect(10)}.",
	f"Panga viga sinu kasuks.\n{collect(200)}.",
	f"Korjasid ja müüsid mustikaid.\n{collect(50)}.",
	f"Sul on sünnipäev.\nSaad igalt mängijalt {price(10)}.",
	f"Saad päranduseks {price(100)}.",
	f"Tulumaksutagastus.\n{collect(20)}.",
	f"Hiiumaa vald tänab sind.\n{collect(100)}.",
	f"Kogusid rahapõrsa täis.\n{collect(100)}."
]