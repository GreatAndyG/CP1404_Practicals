"""Test Silver service taxi class"""



from prac_08.silver_service_taxi import SilverServiceTaxi



def main():
    """Test Silver Service Taxi"""
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
