from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "Toyota",
         "description": "Japanese automotive manufacturer"},
        {"name": "Honda",
         "description": "Japanese automaker known for reliability"},
        {"name": "Ford",
         "description": "American multinational automaker"},
        {"name": "BMW",
         "description": "German luxury vehicle manufacturer"},
        {"name": "Chevrolet",
         "description": "American automobile division of GM"},
    ]
    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']
            )
        )

    car_model_data = [
        {"name": "Camry", "type": "Sedan", "year": 2023,
         "car_make": car_make_instances[0]},
        {"name": "RAV4", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[0]},
        {"name": "Civic", "type": "Sedan", "year": 2023,
         "car_make": car_make_instances[1]},
        {"name": "CR-V", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[1]},
        {"name": "F-150", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[2]},
        {"name": "Mustang", "type": "Sedan", "year": 2023,
         "car_make": car_make_instances[2]},
        {"name": "X5", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[3]},
        {"name": "3 Series", "type": "Sedan", "year": 2023,
         "car_make": car_make_instances[3]},
        {"name": "Silverado", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[4]},
        {"name": "Malibu", "type": "Sedan", "year": 2023,
         "car_make": car_make_instances[4]},
    ]
    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year']
        )
