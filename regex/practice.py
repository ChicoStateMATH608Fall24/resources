rdf = pd.DataFrame({
    "license-plate": ["1ABC567", "0ZDK987", "2BNY365", "9APW235"], # parse middle three letters
    "zip-code": ["07438-2487", "95928", "95926", "95929-0001"], # parse only first five numbers; challenge parse both
    "date": ["2024/09/01", "2022/10/28", "2000-01-20", "1999-09-11"], # parse year, month, day
    "phone-number": ["(530)-555-5555", "(530)-888-9999", "(530)-999-0000", "530-222-0111"], # parse area code and last seven
    "address": ["133 Fake St.", "4 West First st", "330 Main St.", "2 E. First Ave"],# parse street name (no number, no street type)
})
