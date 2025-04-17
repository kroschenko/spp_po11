from typing import List

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"

class Patient(Person):
    def __init__(self, name: str, age: int, patient_id: str):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.assigned_doctor = None
        self.status = "на лечении"
        self.treatments = []

    def assign_doctor(self, doctor):
        self.assigned_doctor = doctor
        print(f"Пациенту {self.name} назначен врач: {doctor.name}")

    def discharge(self, reason: str):
        self.status = f"выписан ({reason})"
        print(f"Пациент {self.name} выписан. Причина: {reason}")

    def __str__(self):
        return f"Пациент: {self.name}, ID: {self.patient_id}, Статус: {self.status}"

class Doctor(Person):
    def __init__(self, name: str, age: int, doctor_id: str, specialization: str):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def prescribe_treatment(self, patient, treatment_type: str, description: str):
        treatment = Treatment(treatment_type, description)
        patient.treatments.append(treatment)
        print(f"Врач {self.name} назначил пациенту {patient.name}: {treatment}")

    def __str__(self):
        return f"Врач: {self.name}, Специализация: {self.specialization}"

class Nurse(Person):
    def __init__(self, name: str, age: int, nurse_id: str):
        super().__init__(name, age)
        self.nurse_id = nurse_id

    def perform_treatment(self, patient):
        if patient.treatments:
            treatment = patient.treatments.pop(0)
            print(f"Медсестра {self.name} выполнила назначение для пациента {patient.name}: {treatment}")
        else:
            print(f"Для пациента {patient.name} нет назначений.")

    def __str__(self):
        return f"Медсестра: {self.name}, ID: {self.nurse_id}"

class Treatment:
    def __init__(self, treatment_type: str, description: str):
        self.treatment_type = treatment_type
        self.description = description

    def __str__(self):
        return f"{self.treatment_type}: {self.description}"

class Hospital:
    def __init__(self):
        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []
        self.nurses: List[Nurse] = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        print(f"Пациент {patient.name} добавлен в больницу.")

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)
        print(f"Врач {doctor.name} добавлен в больницу.")

    def add_nurse(self, nurse: Nurse):
        self.nurses.append(nurse)
        print(f"Медсестра {nurse.name} добавлена в больницу.")

    def assign_doctor_to_patient(self, patient: Patient, doctor: Doctor):
        patient.assign_doctor(doctor)
        print(f"Врач {doctor.name} назначен пациенту {patient.name}.")

if __name__ == "__main__":
    # Создаем больницу
    hospital = Hospital()

    # Создаем пациентов
    patient1 = Patient("Иван Иванов", 30, "P001")
    patient2 = Patient("Мария Петрова", 25, "P002")

    # Создаем врачей
    doctor1 = Doctor("Алексей Сидоров", 45, "D001", "Хирург")
    doctor2 = Doctor("Елена Кузнецова", 40, "D002", "Терапевт")

    # Создаем медсестру
    nurse1 = Nurse("Ольга Смирнова", 35, "N001")

    # Добавляем всех в больницу
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)
    hospital.add_nurse(nurse1)

    # Назначаем врачей пациентам
    hospital.assign_doctor_to_patient(patient1, doctor1)
    hospital.assign_doctor_to_patient(patient2, doctor2)

    # Врачи назначают лечение
    doctor1.prescribe_treatment(patient1, "операция", "Удаление аппендицита")
    doctor2.prescribe_treatment(patient2, "лекарство", "Антибиотики")

    # Медсестра выполняет назначения
    nurse1.perform_treatment(patient1)
    nurse1.perform_treatment(patient2)

    # Выписываем пациентов
    patient1.discharge("окончание лечения")
    patient2.discharge("нарушение режима")

    print("\nИнформация о пациентах:")
    print(patient1)
    print(patient2)
