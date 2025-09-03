# 3) ამ dictionary-ში:
# countries = {
#     "kay": "Georgia",
#     "fr": "France",
#     "it": "Italy"
# }

# შეცვალე key "kay" → "ge" pop()-ის გამოყენებით.

# დატოვე value უცვლელი.




countries = {
    "kay": "Georgia",
    "fr": "France",
    "it": "Italy"
}

value = countries.pop("kay")

countries["ge"] = value

print(countries)