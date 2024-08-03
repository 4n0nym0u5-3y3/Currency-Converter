import requests
import json
import sys
from pprint import pprint

# you can get API from fixer.io. You need to register and get a unique access key.

api_url = "API"
response_data = requests.get(api_url).text
parsed_data = json.loads(response_data) # Parse the JSON data to get whether request was successful, timestamp, etc.
exchange_rates = parsed_data["rates"]

available_currencies = [
    "AED : Emirati Dirham,United Arab Emirates Dirham",
    "AFN : Afghan Afghani,Afghanistan Afghani",
    "ALL : Albanian Lek,Albania Lek",
    "AMD : Armenian Dram,Armenia Dram",
    "ANG : Dutch Guilder,Netherlands Antilles Guilder,Bonaire,Curaçao,Saba,Sint Eustatius,Sint Maarten",
    "AOA : Angolan Kwanza,Angola Kwanza",
    "ARS : Argentine Peso,Argentina Peso,Islas Malvinas",
    "AUD : Australian Dollar,Australia Dollar,Christmas Island,Cocos (Keeling) Islands,Norfolk Island,Ashmore and Cartier Islands,Australian Antarctic Territory,Coral Sea Islands,Heard Island,McDonald Islands,Kiribati,Nauru",
    "AWG : Aruban or Dutch Guilder,Aruba Guilder",
    "AZN : Azerbaijan Manat,Azerbaijan Manat",
    "BAM : Bosnian Convertible Mark,Bosnia and Herzegovina Convertible Mark",
    "BBD : Barbadian or Bajan Dollar,Barbados Dollar",
    "BDT : Bangladeshi Taka,Bangladesh Taka",
    "BGN : Bulgarian Lev,Bulgaria Lev",
    "BHD : Bahraini Dinar,Bahrain Dinar",
    "BIF : Burundian Franc,Burundi Franc",
    "BMD : Bermudian Dollar,Bermuda Dollar",
    "BND : Bruneian Dollar,Brunei Darussalam Dollar",
    "BOB : Bolivian Boliviano,Bolivia Boliviano",
    "BRL : Brazilian Real,Brazil Real",
    "BSD : Bahamian Dollar,Bahamas Dollar",
    "BTC : Bitcoin,BTC, XBT",
    "BTN : Bhutanese Ngultrum,Bhutan Ngultrum",
    "BWP : Botswana Pula,Botswana Pula",
    "BYN : Belarusian Ruble,Belarus Ruble",
    "BYR : Belarusian Ruble,Belarus Ruble",
    "BZD : Belizean Dollar,Belize Dollar",
    "CAD : Canadian Dollar,Canada Dollar",
    "CDF : Congolese Franc,Congo/Kinshasa Franc",
    "CHF : Swiss Franc,Switzerland Franc,Liechtenstein,Campione d'Italia,Büsingen am Hochrhein",
    "CLF : Chilean Unit of Account",
    "CLP : Chilean Peso,Chile Peso",
    "CNY : Chinese Yuan Renminbi,China Yuan Renminbi",
    "COP : Colombian Peso,Colombia Peso",
    "CRC : Costa Rican Colon,Costa Rica Colon",
    "CUC : Cuban Convertible Peso,Cuba Convertible Peso",
    "CUP : Cuban Peso,Cuba Peso",
    "CVE : Cape Verdean Escudo,Cape Verde Escudo",
    "CZK : Czech Koruna,Czech Republic Koruna",
    "DJF : Djiboutian Franc,Djibouti Franc",
    "DKK : Danish Krone,Denmark Krone,Faroe Islands,Greenland",
    "DOP : Dominican Peso,Dominican Republic Peso",
    "DZD : Algerian Dinar,Algeria Dinar",
    "EGP : Egyptian Pound,Egypt Pound,Gaza Strip",
    "ERN : Eritrean Nakfa,Eritrea Nakfa",
    "ETB : Ethiopian Birr,Ethiopia Birr,Eritrea",
    "EUR : Euro,Euro Member Countries,Andorra,Austria,Azores,Baleares (Balearic Islands),Belgium,Canary Islands,Cyprus,Finland,France,French Guiana,French Southern Territories,Germany,Greece,Guadeloupe,Holland (Netherlands),Holy See (Vatican City),Ireland (Eire),Italy,Luxembourg,Madeira Islands,Malta,Monaco,Montenegro,Netherlands",
    "FJD : Fijian Dollar,Fiji Dollar",
    "FKP : Falkland Island Pound,Falkland Islands (Malvinas) Pound",
    "GBP : British Pound,United Kingdom Pound,United Kingdom (UK),England,Northern Ireland,Scotland,Wales,Falkland Islands,Gibraltar,Guernsey,Isle of Man,Jersey,Saint Helena and Ascension,South Georgia and the South Sandwich Islands,Tristan da Cunha",
    "GEL : Georgian Lari,Georgia Lari",
    "GGP : Guernsey Pound,Guernsey Pound",
    "GHS : Ghanaian Cedi,Ghana Cedi",
    "GIP : Gibraltar Pound,Gibraltar Pound",
    "GMD : Gambian Dalasi,Gambia Dalasi",
    "GNF : Guinean Franc,Guinea Franc",
    "GTQ : Guatemalan Quetzal,Guatemala Quetzal",
    "GYD : Guyanese Dollar,Guyana Dollar",
    "HKD : Hong Kong Dollar,Hong Kong Dollar",
    "HNL : Honduran Lempira,Honduras Lempira",
    "HRK : Croatian Kuna,Croatia Kuna",
    "HTG : Haitian Gourde,Haiti Gourde",
    "HUF : Hungarian Forint,Hungary Forint",
    "IDR : Indonesian Rupiah,Indonesia Rupiah,East Timor",
    "ILS : Israeli Shekel,Israel Shekel,Palestinian Territories",
    "IMP : Isle of Man Pound,Isle of Man Pound",
    "INR : Indian Rupee,India Rupee,Bhutan,Nepal",
    "IQD : Iraqi Dinar,Iraq Dinar",
    "IRR : Iranian Rial,Iran Rial",
    "ISK : Icelandic Krona,Iceland Krona",
    "JEP : Jersey Pound,Jersey Pound",
    "JMD : Jamaican Dollar,Jamaica Dollar",
    "JOD : Jordanian Dinar,Jordan Dinar",
    "JPY : Japanese Yen,Japan Yen",
    "KES : Kenyan Shilling,Kenya Shilling",
    "KGS : Kyrgyzstani Som,Kyrgyzstan Som",
    "KHR : Cambodian Riel,Cambodia Riel",
    "KMF : Comorian Franc,Comorian Franc",
    "KPW : North Korean Won,Korea (North) Won",
    "KRW : South Korean Won,Korea (South) Won",
    "KWD : Kuwaiti Dinar,Kuwait Dinar",
    "KYD : Caymanian Dollar,Cayman Islands Dollar",
    "KZT : Kazakhstani Tenge,Kazakhstan Tenge",
    "LAK : Lao Kip,Laos Kip",
    "LBP : Lebanese Pound,Lebanon Pound",
    "LKR : Sri Lankan Rupee,Sri Lanka Rupee",
    "LRD : Liberian Dollar,Liberia Dollar",
    "LSL : Basotho Loti,Lesotho Loti",
    "LTL : Lithuanian litas",
    "LVL : Latvia Lats",
    "LYD : Libyan Dinar,Libya Dinar",
    "MAD : Moroccan Dirham,Morocco Dirham,Western Sahara",
    "MDL : Moldovan Leu,Moldova Leu",
    "MGA : Malagasy Ariary,Madagascar Ariary",
    "MKD : Macedonian Denar,Macedonia Denar",
    "MMK : Burmese Kyat,Myanmar (Burma) Kyat",
    "MNT : Mongolian Tughrik,Mongolia Tughrik",
    "MOP : Macau Pataca,Macau Pataca",
    "MRU : Mauritanian Ouguiya,Mauritania Ouguiya",
    "MUR : Mauritian Rupee,Mauritius Rupee",
    "MVR : Maldivian Rufiyaa,Maldives (Maldive Islands) Rufiyaa",
    "MWK : Malawian Kwacha,Malawi Kwacha",
    "MXN : Mexican Peso,Mexico Peso",
    "MYR : Malaysian Ringgit,Malaysia Ringgit",
    "MZN : Mozambican Metical,Mozambique Metical",
    "NAD : Namibian Dollar,Namibia Dollar",
    "NGN : Nigerian Naira,Nigeria Naira",
    "NIO : Nicaraguan Cordoba,Nicaragua Cordoba",
    "NOK : Norwegian Krone,Norway Krone,Bouvet Island,Svalbard,Jan Mayen,Queen Maud Land,Peter I Island",
    "NPR : Nepalese Rupee,Nepal Rupee,India (unofficially near India-Nepal border)",
    "NZD : New Zealand Dollar,New Zealand Dollar,Cook Islands,Niue,Pitcairn Islands,Tokelau",
    "OMR : Omani Rial,Oman Rial",
    "PAB : Panamanian Balboa,Panama Balboa",
    "PEN : Peruvian Sol,Peru Sol",
    "PGK : Papua New Guinean Kina,Papua New Guinea Kina",
    "PHP : Philippine Peso,Philippines Peso",
    "PKR : Pakistani Rupee,Pakistan Rupee",
    "PLN : Polish Zloty,Poland Zloty",
    "PYG : Paraguayan Guarani,Paraguay Guarani",
    "QAR : Qatari Riyal,Qatar Riyal",
    "RON : Romanian Leu,Romania Leu",
    "RSD : Serbian Dinar,Serbia Dinar",
    "RUB : Russian Ruble,Russia Ruble,Tajikistan,Abkhazia,South Ossetia",
    "RWF : Rwandan Franc,Rwanda Franc",
    "SAR : Saudi Arabian Riyal,Saudi Arabia Riyal",
    "SBD : Solomon Islander Dollar,Solomon Islands Dollar",
    "SCR : Seychellois Rupee,Seychelles Rupee",
    "SDG : Sudanese Pound,Sudan Pound",
    "SEK : Swedish Krona,Sweden Krona",
    "SGD : Singapore Dollar,Singapore Dollar",
    "SHP : Saint Helenian Pound,Saint Helena Pound",
    "SLL : Sierra Leonean Leone,Sierra Leone Leone",
    "SOS : Somali Shilling,Somalia Shilling",
    "SRD : Surinamese Dollar,Suriname Dollar",
    "STN : Sao Tomean Dobra,São Tomé and Príncipe Dobra",
    "SVC : Salvadoran Colon,El Salvador Colon",
    "SYP : Syrian Pound,Syria Pound",
    "SZL : Swazi Lilangeni,eSwatini Lilangeni",
    "THB : Thai Baht,Thailand Baht",
    "TJS : Tajikistani Somoni,Tajikistan Somoni",
    "TMT : Turkmenistani Manat,Turkmenistan Manat",
    "TND : Tunisian Dinar,Tunisia Dinar",
    "TOP : Tongan Pa'anga,Tonga Pa'anga",
    "TRY : Turkish Lira,Turkey Lira,North Cyprus",
    "TTD : Trinidadian Dollar,Trinidad and Tobago Dollar,Trinidad,Tobago",
    "TWD : Taiwan New Dollar,Taiwan New Dollar",
    "TZS : Tanzanian Shilling,Tanzania Shilling",
    "UAH : Ukrainian Hryvnia,Ukraine Hryvnia",
    "UGX : Ugandan Shilling,Uganda Shilling",
    "USD : US Dollar,United States Dollar,America,American Samoa,American Virgin Islands,British Indian Ocean Territory,British Virgin Islands,Ecuador,El Salvador,Guam,Haiti,Micronesia,Northern Mariana Islands,Palau,Panama,Puerto Rico,Turks and Caicos Islands,United States Minor Outlying Islands,Wake Island,East Timor",
    "UYU : Uruguayan Peso,Uruguay Peso",
    "UZS : Uzbekistani Som,Uzbekistan Som",
    "VEF : Venezuelan Bolívar,Venezuela Bolívar",
    "VND : Vietnamese Dong,Viet Nam Dong",
    "VUV : Ni-Vanuatu Vatu,Vanuatu Vatu",
    "WST : Samoan Tala,Samoa Tala",
    "XAF : Central African CFA Franc BEAC,Communauté Financière Africaine (BEAC) CFA Franc BEAC,Cameroon,Central African Republic,Chad,Congo/Brazzaville,Equatorial Guinea,Gabon",
    "XAG : Silver Ounce,Silver",
    "XAU : Gold Ounce,Gold",
    "XCD : East Caribbean Dollar,East Caribbean Dollar,Anguilla,Antigua and Barbuda,Dominica,Grenada,The Grenadines and Saint Vincent,Montserrat",
    "XDR : IMF Special Drawing Rights,International Monetary Fund (IMF) Special Drawing Rights",
    "XOF : CFA Franc,Communauté Financière Africaine (BCEAO) Franc,Benin,Burkina Faso,Ivory Coast,Guinea-Bissau,Mali,Niger,Senegal,Togo",
    "XPF : CFP Franc,Comptoirs Français du Pacifique (CFP) Franc,French Polynesia,New Caledonia,Wallis and Futuna Islands",
    "YER : Yemeni Rial,Yemen Rial",
    "ZAR : South African Rand,South Africa Rand,Lesotho,Namibia",
    "ZMK : Zambian Kwacha,Zambia Kwacha",
    "ZMW : Zambian Kwacha,Zambia Kwacha",
    "ZWL : Zimbabwean Dollar,Zimbabwe Dollar",
]

# Function to handle currency conversion
def convert_currency():
    user_query = input(
        "Please specify the amount of currency to convert, from currency, to currency (with space in between).\nPress SHOW to see list of currencies available.\nPress Q to quit.\n"
    )
    if user_query.upper() == "Q":
        sys.exit()
    elif user_query.upper() == "SHOW":
        pprint(available_currencies)
        convert_currency()
    else:
        try:
            amount_to_convert, from_currency, to_currency = user_query.split(" ")
            from_currency = from_currency.upper()
            to_currency = to_currency.upper()
            amount_to_convert = float(round(int(amount_to_convert), 2))
            converted_amount = round(amount_to_convert * exchange_rates[to_currency] / exchange_rates[from_currency], 2)
            print(f"{amount_to_convert} of currency {from_currency} amounts to {converted_amount} of currency {to_currency} today")
        except KeyError:
            print("Invalid currency code entered. Please try again.")
            convert_currency()
        except ValueError:
            print("Invalid input format. Please follow the correct format: <amount> <from_currency> <to_currency>")
            convert_currency()

# Start the currency conversion process
convert_currency()
