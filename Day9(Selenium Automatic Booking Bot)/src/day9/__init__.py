from Booking.Booking import Booking



with Booking(TearDown=False) as bot:
    bot.land_first_page()
    bot.select_place_to_go("London")
    bot.select_date("2025-07-07","2025-07-15")
    bot.select_adults(3)
    bot.submit_search()
    bot.apply_filtrations()
    input("Press Enter to exit")
