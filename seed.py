from app.models import ClassModel, ServiceModel
from app.repositories import ClassRepository, ServiceRepository


services_data = [
    {
        "name": "Jiu-Jitsu",
        "category": "Saude e bem-estar",
        "monthly_price": 30.00,
        "schedules": [
            ("Terca", "19:00", "20:30"),
            ("Quinta", "19:00", "20:30"),
        ],
    },
    {
        "name": "Mat Pilates",
        "category": "Saude e bem-estar",
        "monthly_price": 30.00,
        "schedules": [
            ("Terca", "09:30", "10:30"),
            ("Quinta", "09:30", "10:30"),
            ("Terca", "17:00", "18:00"),
            ("Quinta", "17:00", "18:00"),
        ],
    },
    {
        "name": "Ginastica",
        "category": "Saude e bem-estar",
        "monthly_price": 35.00,
        "schedules": [
            ("Quarta", "08:00", "09:00"),
            ("Sexta", "08:00", "09:00"),
        ],
    },
    {
        "name": "Iogaterapia",
        "category": "Saude e bem-estar",
        "monthly_price": 25.00,
        "schedules": [("Sexta", "17:00", "19:00")],
    },
    {
        "name": "Danca Mix",
        "category": "Danca e expressao corporal",
        "monthly_price": 20.00,
        "schedules": [("Segunda", "09:00", "10:00")],
    },
    {
        "name": "Aula de K-POP",
        "category": "Danca e expressao corporal",
        "monthly_price": 30.00,
        "schedules": [("Sabado", "15:00", "16:30")],
    },
    {
        "name": "Bale",
        "category": "Danca e expressao corporal",
        "monthly_price": 40.00,
        "schedule_notes": "Dias e horarios a confirmar",
    },
    {
        "name": "Alfabetizacao e Letramento",
        "category": "Educacao e idiomas",
        "monthly_price": 50.00,
        "schedules": [
            ("Segunda", "08:30", "10:00"),
            ("Segunda", "10:00", "11:30"),
            ("Quarta", "17:30", "19:00"),
        ],
    },
    {
        "name": "Curso de Espanhol basico",
        "category": "Educacao e idiomas",
        "monthly_price": 30.00,
        "service_type": "curso",
        "schedules": [("Terca", "14:00", "15:30")],
    },
    {
        "name": "Curso de Esperanto basico",
        "category": "Educacao e idiomas",
        "monthly_price": 0.00,
        "is_free": True,
        "service_type": "curso",
        "schedules": [("Sabado", "09:00", "10:30")],
    },
    {
        "name": "Curso de Ingles basico",
        "category": "Educacao e idiomas",
        "monthly_price": 30.00,
        "service_type": "curso",
        "schedules": [("Sabado", "10:30", "12:00")],
    },
    {
        "name": "Curso de desenho",
        "category": "Cultura e artes",
        "monthly_price": 60.00,
        "service_type": "curso",
        "schedules": [("Segunda", "13:00", "15:00")],
    },
    {
        "name": "Curso de tranca",
        "category": "Cultura e artes",
        "monthly_price": 50.00,
        "service_type": "curso",
        "schedules": [("Terca", "14:00", "16:30")],
    },
    {
        "name": "Curso de croche",
        "category": "Cultura e artes",
        "monthly_price": 10.00,
        "service_type": "curso",
        "schedules": [("Terca", "15:00", "17:00")],
    },
    {
        "name": "Aula de artesanato",
        "category": "Cultura e artes",
        "monthly_price": 0.00,
        "is_free": True,
        "schedules": [("Terca", "15:00", "17:00")],
    },
    {
        "name": "Aula de violao",
        "category": "Cultura e artes",
        "monthly_price": 30.00,
        "schedules": [("Sabado", "09:00", "10:30")],
    },
    {
        "name": "Extensao de cilios, higienizacao capilar e escovacao",
        "category": "Servicos de beleza",
        "service_type": "servico",
        "notes": "Dias, horarios e valores confirmar no WhatsApp.",
        "schedule_notes": "Dias e horarios a confirmar",
    },
]


def seed_services_and_classes():
    service_repository = ServiceRepository()
    class_repository = ClassRepository()

    for service_data in services_data:
        existing_service = service_repository.find_by_name(service_data["name"])
        if existing_service:
            service_id = existing_service[0]["id"]
        else:
            service = ServiceModel(
                name=service_data["name"],
                category=service_data["category"],
                service_type=service_data.get("service_type", "aula"),
                monthly_price=service_data.get("monthly_price"),
                is_free=service_data.get("is_free", False),
                notes=service_data.get("notes"),
            )
            service_id = service_repository.insert_service(service)

        if class_repository.find_by_service_id(service_id):
            continue

        schedules = service_data.get("schedules", [])
        for day_of_week, start_time, end_time in schedules:
            class_repository.insert_class(
                ClassModel(
                    service_id=service_id,
                    day_of_week=day_of_week,
                    start_time=start_time,
                    end_time=end_time,
                )
            )

        schedule_notes = service_data.get("schedule_notes")
        if schedule_notes:
            class_repository.insert_class(
                ClassModel(service_id=service_id, schedule_notes=schedule_notes)
            )


if __name__ == "__main__":
    seed_services_and_classes()
    print("Servicos e aulas cadastrados com sucesso.")
